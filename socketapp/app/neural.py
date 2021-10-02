import time
import pymorphy2
import nltk
import spacy
import string
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sentimental import Sentimental

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


def get_language_key_code(message: str) -> str:
    for symbol in message.split()[0]:
        if symbol.lower() not in string.ascii_lowercase:
            return "ru"
    return "en"


def get_message_preprocessed_data_list(written_text_by_user: str) -> dict:
    language = get_language_key_code(written_text_by_user)

    written_text_by_user = nltk.word_tokenize(written_text_by_user)

    # Тут вся предобработка для английского
    if language == 'en':
        # Удаление stopwords на английском
        filtered_written_text_by_user = " ".join([word for word in written_text_by_user if word not in stop_words_en])

        # Лемматизация для английского
        doc = nlp(filtered_written_text_by_user)
        full_ready_text_by_user = " ".join([token.lemma_ for token in doc])

    # Тут вся предобработка для русского
    else:
        # Удаление stopwords на русском
        filtered_written_text_by_user = [word for word in written_text_by_user
                                         if word not in stop_words_rus]

        # Лемматизация для русского
        full_ready_text_by_user = []
        for word in filtered_written_text_by_user:
            russian_normalized = morph.parse(word)[0]
            full_ready_text_by_user.append(russian_normalized.normal_form)

        # Соединяем в целый текст для дальнейшей работы
        full_ready_text_by_user = " ".join(full_ready_text_by_user)

    full_ready_text_by_user = nltk.sent_tokenize(full_ready_text_by_user)

    # Модель предсказывания для английского
    if language == 'en':
        return sia.polarity_scores(" ".join(full_ready_text_by_user))

    # Модель для русского языка
    return sent.analyze(" ".join(full_ready_text_by_user))


if __name__ == "__main__":
    start_time = time.time()
    print(get_message_preprocessed_data_list("i love you. Send me later message"))
    print(time.time() - start_time)
