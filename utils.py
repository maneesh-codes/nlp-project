from textblob import TextBlob
import pandas as pd
import nltk
nltk.download('punkt')

caption_block = """

Natural language processing (NLP) refers to the branch of computer science and more specifically, the branch of artificial intelligence or AI concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

"""


sentiment_sample_text = '''
McLaren's Lando Norris : I was pretty happy with my laps. It's a tricky circuit; not easy to put everything together but it's so quick around here and the smallest mistake can take a big amount of lap time. I'm happy. It's been a good day and good positions for tomorrow.
'''


def get_sentiment(text: str, threshold: float = 0.3):
    '''
    This function will output the sentiment
    '''
    blob = TextBlob(text)
    sentiment: float = blob.sentiment.polarity
    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return ('😍😃😊🥰', sentiment)

    elif sentiment <= hostile_threshold:
        return ('😢😡😭😞', sentiment)
    else:
        return ('😐😑😒😕', sentiment)


def get_sentence_sentiment(text: str, threshold: float = 0.3):
    '''
    This function split the input into sentences and compute the sentiment score 😀
    '''
    blob = TextBlob(text)
    result = []
    for sen in blob.sentences:
        res = ''
        p = sen.sentiment.polarity
        if p > threshold:
            res = '😍'
        elif p < -threshold:
            res = "😭"
        else:
            res = '😐'
        # concat
        res = res + " : " + str(sen)
        result.append(res)

    return result


def spell_check(text: str):
    blob = TextBlob(text)
    return blob.correct()


def get_pos(text: str):
    '''
    Part-of-speech Tagging
    '''
    blob = TextBlob(text)
    tags = {}
    for x, y in blob.tags:
        tags[y] = x

    df = pd.DataFrame(data=tags, index=['words'])
    return df
