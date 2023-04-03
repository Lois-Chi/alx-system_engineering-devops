#!/usr/bin/python3
"""Recursive function that parses the titles of all hot searches"""

import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """ prints a sorted count of given keywords"""
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                    'count':0}))
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko; Google Web Preview) \
            Chrome/27.0.1453 Safari/537.36"
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
        keywords_matched = 0
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
