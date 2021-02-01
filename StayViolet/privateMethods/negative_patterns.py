from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import random

stress_keywords = ['stress','anxiety','anxious','stressed','tired', 'scared', 'afraid', 'fear','need help','need support']
depression_keywords = ['end my life','depression','anxiety','anxious','depressed','I want to die','self harm','cut myself',"I don't wnat to live",'sad','mental health','suicide','kill myself']
school_keywords = ['school','homework','test','quiz','paper','subject']

gifs = ['https://media.discordapp.net/attachments/803257943645880323/805302433390788648/giphy_5.gif',
    'https://cdn.discordapp.com/attachments/805132413146759170/805461686479093780/giphy_24.gif',
    'https://cdn.discordapp.com/attachments/805132413146759170/805461542220988456/giphy_4.gif',
    'https://cdn.discordapp.com/attachments/805132413146759170/805461539737829376/giphy_6.gif']

# This message formulates and returns a message to a user message containing a depression pattern
def get_depression_response():
    intro = "Hey! Are you okay? If you're struggling with anything, you're not alone and help is available. Here are some resources:"
    resource1 = "  -  National Suicide Prevention Lifeline: call 800-273-8255 or visit https://suicidepreventionlifeline.org/"
    resource2 = "  -  If you want to talk to people, check out this Discord: https://discord.gg/9g98gZ9H" 
    resource3 = "  -  Please remember you are always loved: "
    resource3 = resource3 + random.choice(gifs)
    return "{intro}\n\n{resource1}\n{resource2}\n{resource3}".format(intro = intro, resource1 = resource1, resource2 = resource2, resource3 = resource3)

# This method determines if a message could contain a negative pattern of depression or anxiety
# It uses a combination of keywords and sentiment analysis
def contains_depression_traces(message_content):
    depression_keywords = ['hate myself','my life','end my life','depression','anxiety','anxious','depressed','I want to die','self harm','cut myself',"I don't wnat to live",'sad','mental health','suicide','kill myself']
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    if negative_sentiment > .93:
        return True
    message_is_depressing = negative_sentiment > .75 or (negative_sentiment > .5 and positive_sentiment < .5)
    for word in depression_keywords:
        if word in message_content :
            print(negative_sentiment)
            return message_is_depressing
    return False

def get_stress_response():
    intro = "Hey! Are you okay? You sound stressed. What's the problem? School, work, relationships? "
    intro = intro + random.choice(gifs)
    return intro

def contains_stress_traces(message_content):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    print(negative_sentiment)
    print(positive_sentiment)
    message_is_stressed = negative_sentiment > .75 or (negative_sentiment > .5 and positive_sentiment < .5)
    for word in stress_keywords:
        if word in message_content :
            return message_is_stressed
    return False
def contains_school_traces(message_content):
    schoolFound = False
    stressFound = False
    for word in school_keywords:
        if word in message_content:
            schoolFound = True
    for word in stress_keywords:
        if word in message_content:
            stressFound = True
    return schoolFound and stressFound

def contains_jobfinding_traces(message_content):
    jobfind_keywords = ['looking for a job','searchin for a job','need a job']
    for word in jobfind_keywords:
        if word in message_content:
            return True
    return False
def contains_jobarea_traces(message_content):
    jobfind_keywords = ['estee lauder','google cloud','webdeveloper','janitor']
    # salary_keywords = ['10k','20k','30k','40k']
    # distance_keywords = ['5 mi','10 mi', '20 mi', 'anywhere']
    for word in jobfind_keywords:
        if word in message_content:
            return True
    return False

def contains_schooltopic_traces(message_content):
    topic_keywords = ['geometry', 'triangles', 'biology', 'trigonometry']
    for word in topic_keywords:
        if word in message_content:
            return True
    return False

def contains_jobmanage_traces(message_content):
    manage_keywords = ['miscommunication', 'disorganized']
    for word in manage_keywords:
        if word in message_content:
            return True
    return False

def contains_relationship_traces(message_content):
    relationship_keywords = ['romantic', 'partner', 'special someone', 'friend', 'boyfrined', 'girlfriend', 'relationship']
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_analyzer.polarity_scores(message_content)
    negative_sentiment = sentiment_dict['neg']
    positive_sentiment = sentiment_dict['pos']
    message_has_stress = negative_sentiment > .25 and positive_sentiment < .25
    for word in relationship_keywords:
        if word in message_content and message_has_stress:
            return True
    return False
    