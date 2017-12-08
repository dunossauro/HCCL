from collections import Counter
from os import listdir

from functions import json_to_dict


def path_dicts_to_list(path):
    return [json_to_dict('wordcount', file_) for file_ in listdir(path)]


xpto = path_dicts_to_list('bands')

full_count = ' '.join(sum(list(map(lambda x: list(x.keys()), xpto)), []))

# Contagem de aparição de palavras em todas as bandas
count = Counter(full_count.split())
