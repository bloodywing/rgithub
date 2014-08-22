# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 12:01:47 2014

@author: pierre
"""

import urls
import urllib.request
import json
import textwrap
import random

max_repos = 3
max_page=33
WIDTH = 79

def load_top_repository(url):
    query = {
        'q': 'language:Python',
        'sort': 'stars',
        'order': 'desc'
    }
    request = urllib.request.urlopen(url + '?' + urllib.parse.urlencode(query))
    text = request.read().decode('utf-8')
    repos = json.loads(text)['items']
    for r in repos[0:max_repos]:
        process(r)
        
def load_rand_repository(url):
    randpage = random.randint(2, max_page)
    query = {
        'q': 'language:Python',
        'page': randpage
    }
    request = urllib.request.urlopen(url + '?' + urllib.parse.urlencode(query))
    text = request.read().decode('utf-8')
    repos = json.loads(text)['items']
    for r in repos[0:max_repos]:
        process(r)

def process(r):
    print('{o}/{n}   (watchers: {w}, forks: {f}, updated: {u})' \
        .format(o=r['owner']['login'], n=r['name'], w=r['watchers'], 
                f=r['forks'], u=r['pushed_at'][:10]))
    desc = '\n'.join(textwrap.wrap(r['description'], WIDTH))
    print('{d}'.format(d=desc))
    print('{url}'.format(url=r['url']), end=' ')
    if 'homepage' in r and r['homepage']:
        print('/  {hp}'.format(hp=r['homepage']))
    else:
        pass
    print("----------\n")
    
if __name__ == '__main__':
    load_top_repository(url=urls.GITHUB_SEARCH_REPO)
    load_rand_repository(url=urls.GITHUB_SEARCH_REPO)