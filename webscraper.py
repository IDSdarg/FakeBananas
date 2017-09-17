from eventregistry import *
from newspaper import Article
import numpy as np
import pandas as pd
import random

# Print a list of recently added articles mentioning entered words
api_key = 'eda39267-9017-481a-860d-0b565c6d8bf3'
er = EventRegistry(apiKey = api_key)

def get_articles(keywords):
    q = QueryArticlesIter(keywords=QueryItems.AND(keywords))
    q.setRequestedResult(RequestArticlesInfo(count= 199, sortBy="sourceImportance"))
    print keywords

    x = 0
    df = pd.DataFrame({'source':'test','url':'testing','text':'placeholers'}, index=[0])
    df.columns = ['source','url','text']

    res = er.execQuery(q)
    for article in res['articles']['results']:
        data = {
            'source': article['source']['title'].encode('utf-8'),
#             'title' : article['title'].encode('utf-8'),
            'url' : article['url'].encode('utf-8'),
            'text' : article['body'].encode('utf-8')
        }
        df_temp = pd.DataFrame(data,index=[x])
        df = pd.concat([df,df_temp])
        x += 1
    return df

def get_search_params(keywords):
    search_params = []
    while len(keywords) != 0:
        # Randomly select 3 words
        rm = random.sample(keywords,3)
        # add the list of 3 words to the searchable list
        search_params.append(rm)
        # remove words from the list
        for word in rm:
            keywords.remove(word)

        # put 1 or 2 random words back
        # if 3 words left just append to search_params
        if len(keywords) is 3:
            search_params.append(keywords)
            keywords = []
        # if no words left just exit
        elif len(keywords) is 0:
            keywords = []
        # if 1 word left, append 2 and search_params
        elif len(keywords) is 1:
            keywords.append(random.sample(rm,2)[0:2])
        else:
            keywords.append(random.sample(rm,1)[0])
    return search_params

def get_keywords(user_url):
    url = user_url.decode('utf-8')
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    keywords = article.keywords
    kl = []
    for word in keywords:
        kl.append(word.encode('utf-8'))
    return kl

def web_scrape(url):
    kl = get_keywords(url)
    params = get_search_params(kl)

    df = pd.DataFrame({'source':'test','url':'testing','text':'placeholers'}, index=[0])
    df.columns = ['source','url','text']

    for query in params:
        df = pd.concat([df,get_articles(query)])

    df = df.drop(df.index[[0,1]])
    df = df.reset_index(drop=True)
#     df.to_json(orient='index')
    df.to_csv('articles.csv')
    print df
