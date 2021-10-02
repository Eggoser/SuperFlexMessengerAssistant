import time
import pymorphy2
import nltk
import spacy
import string
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sentimental import Sentimental
import requests
import bs4
import urllib.parse
import json


# nltk.download([
#     "names",
#     "stopwords",
#     "state_union",
#     "twitter_samples",
#     "movie_reviews",
#     "averaged_perceptron_tagger",
#     "vader_lexicon",
#     "punkt",
#     "wordnet",
# ])


nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
morph = pymorphy2.MorphAnalyzer()
sent = Sentimental()
sia = SentimentIntensityAnalyzer()
stop_words_en = stopwords.words('english')
stop_words_rus = stopwords.words('russian')


def get_translate(phrase):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; '
                      'rv:20.0) Gecko/20100101 Firefox/20.0'
    }
    data = {
        "format": "text",
        "from": "rus",
        "input": phrase,
        "options": {
            "origin": "contextweb",
            "languageDetection": True
        },
        "languageDetection": True,
        "origin": "contextweb",
        "to": 'eng'
    }

    response = requests.post("https://api.reverso.net/translate/v1/translation", headers=headers, data=json.dumps(data))
    return response.json()["translation"][0]


def get_language_key_code(message: str) -> str:
    for symbol in message.split()[0]:
        if symbol.lower() not in string.ascii_lowercase:
            return "ru"
    return "en"


def get_message_preprocessed_data_list(written_text_by_user: str) -> dict:
    language = get_language_key_code(written_text_by_user)

    if language != "en":
        written_text_by_user = get_translate(written_text_by_user)
        language = "en"

    written_text_by_user = nltk.word_tokenize(written_text_by_user)



    # Удаление stopwords на английском
    filtered_written_text_by_user = " ".join([word for word in written_text_by_user if word not in stop_words_en])

    # Лемматизация для английского
    doc = nlp(filtered_written_text_by_user)
    full_ready_text_by_user = " ".join([token.lemma_ for token in doc])


    full_ready_text_by_user = nltk.sent_tokenize(full_ready_text_by_user)

    # Модель предсказывания для английского
    return sia.polarity_scores(" ".join(full_ready_text_by_user))



if __name__ == "__main__":
    start_time = time.time()
    print(get_message_preprocessed_data_list("i love you. Send me later message"))
    print(time.time() - start_time)
