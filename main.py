# Import necessary libraries
import praw
from collections import defaultdict
from textblob import TextBlob
from openai import OpenAI
import uuid

# Insert your Reddit API details here to set up environment for scraping Reddit
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
)

# Insert your OpenAI API key here
api_key = ''

# Choose the required subreddit
subreddit = 'diabetes'



# In order to ensure anonymity of users, the usernames are tokenized.
def generate_token():
    return str(uuid.uuid4())

# Function to scrape data while tokenizing the usernames
def scrape_data(subreddit, limit=1000):
    token_map = {}  
    subreddit = reddit.subreddit(subreddit)
    posts = []
    authors_data = defaultdict(list)
    
    # Words to look out for, if the post or comment does not exist anymore
    removed_words = ['removed', 'deleted']

    # Get post information 
    for post in subreddit.hot(limit=limit):
        post_author = post.author.name if post.author else 'Anonymous'
        if post_author not in token_map:
            token_map[post_author] = generate_token()
        token_post_author = token_map[post_author]
        
        post_info = {
            "type": "post",
            "title": post.title,
            "body": post.selftext,
            "author": token_post_author
        }
        
        # Add post to the author's data if the post has not been removed
        post_removed = any(word in post_info["body"].lower() for word in removed_words)
        if not post_removed:
            authors_data[token_post_author].append({
                "type": "post",
                "title": post.title,
                "body": post.selftext
            })

        # Get all comments of the post
        post.comments.replace_more(limit=0)
        
        # Get information of each of the comments for the post
        for comment in post.comments.list():
            if hasattr(comment, 'body'):
                comment_author = comment.author.name if comment.author else 'Anonymous'
                if comment_author not in token_map:
                    token_map[comment_author] = generate_token()
                token_comment_author = token_map[comment_author]
                
                comment_info = {
                    "type": "comment",
                    "body": comment.body,
                    "post_title": post.title
                }
                
                # Add comment to the author's data
                comment_removed = any(word in comment_info["body"].lower() for word in removed_words)
                if not comment_removed:
                    authors_data[token_comment_author].append({
                        "type": "comment",
                        "body": comment.body,
                        "post_title": post.title
                    })
        
        posts.append(post_info)
    
    return posts, authors_data

# Function to get the polarity of each post/comment made by individual authors using TextBlob
def get_sentiments(authors_data):
    authors_sentiment = defaultdict(list)
    for author, entries in authors_data.items():
        for entry in entries:
            sentiment = TextBlob(entry['body']).sentiment
            authors_sentiment[author].append({'body': entry['body'], 'polarity':sentiment.polarity})
    return authors_sentiment

# Function to summarize the author's comments and get the aggregated polarity of all messages by the author
def create_author_summary(authors_sentiment):
    author_summary = {}
    for author, sentiments in authors_sentiment.items():
        combined_texts = ".".join([entry['body'] for entry in sentiments])
        average_polarity = sum(entry['polarity'] for entry in sentiments) / len(sentiments)
        author_summary[author] = {
            'messages': combined_texts,
            'average_polarity': average_polarity
        }
    return author_summary

# Scrape the data from Reddit
data, authors_data = scrape_data(subreddit, limit=100)
print('Data extracted')

# Get the sentiment of posts and comments made by author and aggregate it
authors_sentiment = get_sentiments(authors_data)
author_summary = create_author_summary(authors_sentiment)

# Setup OpenAI API
client = OpenAI(api_key = api_key)

# To aid AI in discerning the author's perception of the condition, the polarity has been generally classified and included in the prompt
for author, content in author_summary.items():
    if content['average_polarity'] > 0:
        overall_sentiment = 'positive'
    else:
        overall_sentiment = 'negative'
    
    # This is the prompt to generate the message. If there is a specific clinical trial which has to be recomended, please amend the prompt as such
    prompt = f"""Based on the following contents of the posts and comments of this author on reddit's diabetes platform and the average polarity score of the sentiment 
        of these posts, please generate a personalized message asking them their willingness to participate in clinical trials, while highlighting it's pros and cons. 
        The contents of this author's messages are: "{content['messages']}" and the average polarity of the messages is: {content['average_polarity']}, indicating 
        an overall {overall_sentiment} sentiment."""
    
    # Generate personalized messages suggesting clinical trials for each author
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content":  prompt}
    ]
    )
    # If the post details are required, please uncomment the print lines below
    
    # print(author)
    # print(content['messages'])
    # print(content['average_polarity'])
    print(completion.choices[0].message.content)
    print("\n---\n")
