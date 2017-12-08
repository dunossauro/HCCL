from json import load, dump
import matplotlib.pyplot as plt


def json_to_dict(path, json):
    with open('{}/{}'.format(path, json)) as _file:
        return load(_file)


def dict_to_json(path, _dict):
    with open('{}.json'.format(path), 'w') as fp:
        dump(dict, fp, indent=2, ensure_ascii=False)


def gen_graph(sequence, height, x_names, path, text):
    plt.figure(figsize=(9, 4))
    plt.bar(sequence, height, align='center', alpha=0.5)
    plt.ylabel('Palavras')
    plt.title(text)

    plt.savefig(path)
    plt.close()
