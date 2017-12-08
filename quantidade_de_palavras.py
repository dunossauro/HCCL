from os import listdir
from functions import json_to_dict, gen_graph


def path_dicts_to_list(path):
    return {file_.replace('.json', ''): json_to_dict('wordcount', file_)
            for file_ in listdir(path)}


bands_dict = path_dicts_to_list('bands')
bands = bands_dict.keys()
words_len = [len(bands_dict[x].values()) for x in bands_dict]

gen_graph(bands, words_len, range(len(bands)),
          'images/vocabulario_interbandas.png', 'Tamanho do vocabulário usado')
