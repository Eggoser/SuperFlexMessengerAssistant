import re
from pprint import pprint

import nltk
import spacy
from detoxify import Detoxify
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from langdetect import detect

#nltk.download([
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

nlp = spacy.load("en_core_web_sm")


# written_text_by_user = передача текста из мессенджера
def get_messege_processing_info(written_text_by_user: str):
    print("start")
    written_text_by_user_for_toxic = written_text_by_user ### Если надо будет проверять на связность
    # Разделяем на слова (токенизируем)
    written_text_by_user = " ".join(nltk.word_tokenize(written_text_by_user))
    # en = english

    # Определяем язык для дальнейшей работы с текстом

    language = detect(written_text_by_user)
    if language != 'en':
        print(language)
        return

    # Удаление stopwords на английском
    filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('english')]

    # Соединяем в текст целиком для леммы на английском
    filtered_written_text_by_user = " ".join(filtered_written_text_by_user)

    # Лемматизация для английского
    sentence = filtered_written_text_by_user
    doc = nlp(sentence)
    full_ready_text_by_user = " ".join([token.lemma_ for token in doc])

    full_ready_text_by_user = nltk.sent_tokenize(full_ready_text_by_user)
    # print('Результат предобработки =', full_ready_text_by_user)

    written_text_by_user_for_toxic = nltk.sent_tokenize(written_text_by_user_for_toxic)
    # print('Результат для токсичности in English=', written_text_by_user_for_toxic)

    sia = SentimentIntensityAnalyzer()

    dict_of_results = []
    list_of_dicts = []

    for number in range(len(full_ready_text_by_user)):
        dict_of_results = sia.polarity_scores(full_ready_text_by_user[number])
        # Токсичность текста
        dict_of_results_tox = Detoxify('original').predict(written_text_by_user_for_toxic[number])
        dict_of_results.update(dict_of_results_tox)
        list_of_dicts.append(dict_of_results)

    negative = 0
    toxic = 0
    bad_words = 0
    rasizm = 0
    threat = 0
    comparative = 0
    for dict_ in list_of_dicts:
        # print(dict_)
        negative += dict_["neg"] - dict_["pos"]
        toxic += dict_["toxicity"] + dict_["severe_toxicity"]
        bad_words += dict_["insult"] + dict_["obscene"]
        rasizm += dict_["identity_hate"]
        threat += dict_["threat"]

    return negative, toxic, bad_words, rasizm, threat, comparative

