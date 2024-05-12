# Reddit Data Scraping and Sentiment Analysis Project

## Overview

This project involves scraping data from the Reddit, performing sentiment analysis on the posts and
comments, and generating personalized messages suggesting participation in clinical trials. The project ensures user
anonymity through tokenization of usernames and adheres to ethical guidelines regarding data privacy and user
engagement.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AishwaryaBalajee/Reddit-Data-Scraping-and-Sentiment-Analysis.git

2. **Install Dependencies**
   ```bash
   pip install praw textblob openai

3. **Set up Reddit API keys**  
   For a tutorial, please
   visit [Github Reddit Archive](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps).
4. **Set up OpenAI API environment**  
   Follow the steps [here](https://platform.openai.com/docs/quickstart?context=python) to set up the OpenAI API account.
5. **Run the Python code**
   ```bash
   python main.py

## Methodology

This project scrapes data from a specific subreddit of a condition relevant to the clinical trial. I categorize all the
posts and comments based on the author to evaluate their experiences. This is done to create personalized messages to
each individual. The author's names are tokenized to ensure user privacy.

The sentimental context of posts/comments made by each author is analyzed using Textblob, a python library used for
natural language processing (NLP) tasks. The polarity of the sentiment analysis is utilized to evaluate the degree of
positivity or negativity expressed in the author's data.

Using the content of each author's posts/comments as well as their aggregated sentiment, OpenAI's API is prompted to
create a personalized message to the individuals, informing them about the pros and cons of clinical trials and while
asking them about their willingness to participate in one.

My main challenge in creating this project was identifying individuals who might be open to clinical trials based on
sentiment analysis of their content. A positive sentiment might mean willingness to participate or contentness with the
current treatment plan, while a negative sentiment might mean disapproval of clinical trials or that they are unhappy
with the current treatment plan and are looking for new ventures.

Hence, instead of categorizing them, I have taken their messages into consideration and created a personalized message
based on each individual's situation.

## Examples of Collected Data

I chose diabetes as the subreddit to scrape, this code can be easily applied to other subreddits as well.

Here is one of the posts which was scraped and analyzed:

```markdown
My doctor added Farxiga to my medicine mix and it gave me stomach issues which took weeks to adapt to. The next month I
went to the pharmacy for my usual pickup and realized she didn’t give me any refills. It took her a week to respond to
me and the pharmacist’s multiple messages and send a refill. In that week my stomach got used to not dealing with the
issues. Now I got my prescription and my stomach is f’d up again. Starting the acclimation all over again.
```

The polarity generated for this text is -0.0625. The message generated for this user is as follows:

```markdown
Dear [Author's Username],

I hope you're managing well despite the recent challenges with your medication. Your experience with Farxiga sounds
tough, and it's unfortunate to hear about the stomach issues you're facing because of it. Your feedback sheds light on
the importance of effective communication and timely prescriptions in managing health conditions like diabetes.

Have you ever considered participating in clinical trials for new diabetes treatments? While it may not immediately
resolve your current issues, it could potentially offer alternative solutions in the long run. By participating, you
have the opportunity to contribute to medical advancements and potentially access cutting-edge treatments before they
reach the market. On the flip side, there may be uncertainties associated with new medications, potential side effects,
and the unpredictability of outcomes.

Considering your insights and experiences shared on the platform, I believe your perspective could be valuable in the
realm of clinical trials. Would you be interested in exploring this opportunity further?

Warm regards,
[Your Name]
```

Another post made by a user is shown below:

```markdown
Alcohol causes you liver to start working on processing the alcohol instead of releasing glucose.

If you are not careful, and especially if you are on insulin, it can cause you to go hypo.

Since I am no longer on insulin, I worry a bit less about it. I still have the odd beer or two, and it causes my levels
to go up and down a fair bit more than normal.

While on insulin, 2 low carb beers on an empty stomach and I was fighting a hypo an hour or so later. Just something to
be aware of..It is honestly a combination of genetics and lifestyle factors that seem to lead to most cases of T2
diabetes.

Historically, we have lived very active lives in comparison to today, and could handle eating a decent amount of carbs
even if our genetics favored the development of T2 diabetes simply because we were so active that we burnt it all off
during the day as we physically worked.

That has changed, as we have become less active, and turbocharged our consumption of sugars and carbs.

So it is a lie to say diet has nothing to do with T2 diabetes development.

However, it is really true to say it isn't your fault if you develop diabetes. Our society is built around the
consumption of lots of carbs and sugars in a low activity environment. It really isn't your fault that you went with the
flow of things and did as everyone else did ... you didn't have the knowledge of the harm it was doing nor the knowledge
or reason to fix it. And a non-trivial portion number of people get away with their horrible diets and inactive
lifestyles without developing diabetes..Yeah, but if the alarm went off and wasn't noticed, and your child got injured
due to that alarm not being resolved, then the school would be legally liable for damages.

There is no easy answer unfortunately, but, it is awesome that you are able to act rationally in the end :-).You sir,
are hereby forgiven..Nice hack.
```

The average polarity of this content is 0.1487. The generated message is as follows:

```markdown
Dear [Author's Name],

I hope this message finds you well. I have noticed your engaging and informative posts on Reddit's diabetes platform,
where you share valuable insights and experiences related to managing diabetes. Your positive attitude and willingness
to educate others in the community are truly commendable.

Given your interest and active involvement in discussing diabetes-related topics, I wanted to reach out to you with an
opportunity to potentially participate in clinical trials focused on diabetes management and treatment. Clinical trials
play a crucial role in advancing medical research and improving patient outcomes.

Here are some potential benefits of participating in clinical trials:

1. Access to cutting-edge treatments: By participating in a clinical trial, you may have the opportunity to receive
   innovative treatments that are not yet available to the general public.
2. Contributing to medical advancements: Your participation can help researchers gain valuable insights into diabetes
   management, leading to the development of better therapies for future generations.
3. Enhanced care and monitoring: Throughout the trial, you will receive close supervision and monitoring from healthcare
   professionals, ensuring that you receive high-quality care.

However, it's important to be aware of some potential drawbacks of participating in clinical trials:

1. Uncertainty of outcomes: The effectiveness of the treatment being studied may not be guaranteed, and there is a
   possibility of experiencing side effects or adverse reactions.
2. Time commitment: Participating in a clinical trial may require regular visits to the research facility and adherence
   to strict protocols, which can be time-consuming.
3. Limited control over treatment: In some trials, participants may not have control over the type of treatment they
   receive, as randomization is often used to ensure unbiased results.

Despite these considerations, participating in a clinical trial can be a rewarding experience that allows you to
contribute to the advancement of diabetes research and potentially benefit from cutting-edge treatments.

If you are interested in learning more about potential clinical trial opportunities or would like to discuss this
further, please feel free to reach out. Your unique insights and positive contributions to the diabetes community would
be highly valued in a research setting.

Thank you for your dedication to raising awareness and sharing your experiences with diabetes. Your active participation
in discussions is truly appreciated.

Warm regards,

[Your Name]
```