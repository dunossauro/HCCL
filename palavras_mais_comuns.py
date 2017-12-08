from collections import Counter, OrderedDict
from itertools import filterfalse, chain
from os import listdir
from nltk import tokenize
from nltk.corpus import stopwords as ntlk_stopwords
from functions import json_to_dict, gen_graph
from pt_stopwords import stopwords, default_punctation

multilang_stopwrods = list(chain(ntlk_stopwords.words('portuguese'),
                                 ntlk_stopwords.words('english'),
                                 default_punctation,
                                 stopwords))


def remove_stop_words(word_list: list, stopwords: list) -> list:
    """Filter stopwords on list."""
    return list(filterfalse(lambda x: x in stopwords, word_list))


def gen_top10(band):
    musics = json_to_dict('bands', '{}.json'.format(band))

    lirycs = ' '.join(list(musics.values())).lower()

    count = Counter(remove_stop_words(tokenize.casual_tokenize(lirycs),
                                      multilang_stopwrods))

    return OrderedDict({word: count for word, count in count.most_common(10)})


for band in listdir('bands'):
    top_10 = gen_top10(band[:-5])
    gen_graph(list(top_10.keys()), list(top_10.values()), list(top_10.keys()),
              'images/{}_top10.png'.format(band[:-5]),
              '10 palavras mais usadas')
