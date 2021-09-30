import re
import pymorphy2
from pprint import pprint

import nltk
import spacy
from detoxify import Detoxify
# from pymorphy2 import MorphAnalyzer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from langdetect import detect
from sentimental import Sentimental

nltk.download([
     "names",
     "stopwords",
     "state_union",
     "twitter_samples",
     "movie_reviews",
     "averaged_perceptron_tagger",
     "vader_lexicon",
     "punkt",
     "wordnet",
 ])


# written_text_by_user = передача текста из мессенджера
def get_messege_processing_info(written_text_by_user: str):
    written_text_by_user_for_toxic = written_text_by_user ### Если надо будет проверять на связность
    # Разделяем на слова (токенизируем)
    written_text_by_user = nltk.word_tokenize(written_text_by_user)
    # en = english

    # Определяем язык для дальнейшей работы с текстом

    language = detect(written_text_by_user)
    print(language)

    if language == 'en' or 'it' :

    # Удаление stopwords на английском
        filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('english')]

    # Соединяем в текст целиком для леммы на английском
        filtered_written_text_by_user = " ".join(filtered_written_text_by_user)

    # Лемматизация для английского
        nlp = spacy.load('en', disable=['parser', 'ner'])
        sentence = filtered_written_text_by_user
        doc = nlp(sentence)
        full_ready_text_by_user = " ".join([token.lemma_ for token in doc])

    ### Тут вся предобработка для русского
    else :

    # Удаление stopwords на русском
        filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('russian')]

    # Лемматизация для русского
        morph = pymorphy2.MorphAnalyzer()
        full_ready_text_by_user = []
        for word in filtered_written_text_by_user:
            russian_normalized = morph.parse(word)[0]
            full_ready_text_by_user.append(russian_normalized.normal_form)

    # Соединяем в целый текст для дальнейшей работы
        full_ready_text_by_user = " ".join(full_ready_text_by_user)


    full_ready_text_by_user = nltk.sent_tokenize(full_ready_text_by_user)
    print('Результат предобработки =', full_ready_text_by_user)

    written_text_by_user_for_toxic = nltk.sent_tokenize(written_text_by_user_for_toxic)
    print('Результат для токсичности in English=', written_text_by_user_for_toxic)


    if language == 'en' or 'it' :
        sia = SentimentIntensityAnalyzer()

        dict_of_results = []
        list_of_dicts = []

        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sia.polarity_scores(full_ready_text_by_user[number])
            # Токсичность текста
            dict_of_results_tox = Detoxify('original').predict(written_text_by_user_for_toxic[number])
            dict_of_results.update(dict_of_results_tox)
            list_of_dicts.append(dict_of_results)

        #results_for_connection = sia.polarity_scores(written_text_by_user_for_connection) ### В начале тоже закомментил, если понадобится потом допилю

    else:
        sent = Sentimental()

        dict_of_results = []
        list_of_dicts = []

        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sent.analyze(full_ready_text_by_user[number])
            list_of_dicts.append(dict_of_results)

    negative = 0
    toxic = 0
    bad_words = 0
    rasizm = 0
    threat = 0
    comparative = 0
    if language == 'en' or 'it' :
        for dict_ in list_of_dicts :
            negative += dict_["neg"] - dict_["pos"]
            toxic += dict_["toxicity"] + dict_["server_toxicity"]
            bad_words += dict_["insult"] + dict_["obscene"]
            rasizm += dict_["identity_hate"]
            threat += dict_["threat"]
    else:
        for dict_ in list_of_dicts:
            comparative += dict_["comparative"]
    return negative, toxic, bad_words, rasizm, threat, comparative