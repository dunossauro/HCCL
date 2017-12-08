from json import dump
from re import sub
from bs4 import BeautifulSoup as bs
from requests import get

from functions import dict_to_json

base_url = 'https://www.letras.mus.br/'
band = 'dead-fish/'
html = get('{}{}'.format(base_url, band)).text

page = bs(html, 'lxml')
xpto = page.find('ul', {'class': 'cnt-list'})
lines = xpto.find_all('li')

musics_links = {line.text: line.find('a').get('href') for line in lines}


def pretty_format(bs_list):
    return ''.join(map(lambda x: sub(r'</?(br|p)/?>', ' ', str(x)),
                       bs_list.find_all('p'))).replace('  ', ' ').strip()


def get_lirycs(base_url, musics_links, music):
    return bs(get('{}{}'.format(base_url, musics_links[music])).text,
              'lxml').find('article')


all_ = {music: pretty_format(get_lirycs(base_url, musics_links, music))
        for music in musics_links}


dict_to_json('bands/dead-fish', all_)
