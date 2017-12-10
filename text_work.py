from collections import Counter
from itertools import filterfalse, chain
from nltk import tokenize
from nltk.corpus import stopwords as ntlk_stopwords
from pt_stopwords import stopwords, default_punctation

from functions import dict_to_json, json_to_dict


def remove_stop_words(word_list: list, stopwords: list) -> list:
    """Filter stopwords on list."""
    return list(filterfalse(lambda x: x in stopwords, word_list))


multilang_stopwrods = list(chain(ntlk_stopwords.words('portuguese'),
                                 ntlk_stopwords.words('english'),
                                 default_punctation,
                                 stopwords))

musics = json_to_dict('bands', 'dead-fish.json')

lyrics = ' '.join(list(musics.values())).lower()

count = Counter(remove_stop_words(tokenize.casual_tokenize(lyrics),
                                  multilang_stopwrods))

dict_to_json('wordcount/dead-fish', count)
