from newspaper import Article
from smmryapi.smmryapi import SmmryAPI
import nltk
import numpy as np
import networkx as nx
from nltk.cluster.util import cosine_distance
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.corpus import stopwords
from googleapiclient.discovery import build
import json

def article_parser_fn(link):
    ##for all information regarding 'article' objects, please see newspaper3k documentation
    article = Article(link) ##creating an article object from the string link
    article.download() ##downloading the article object
    article.parse() ##'parsing' the article object
    return(article.text)

def article_smmry_fn(link):
    SMMRY_API_KEY = "93267E94CD"
    smmry = SmmryAPI(SMMRY_API_KEY)
    url = link
    s = smmry.summarize(url, sm_length=3, sm_keyword_count=5)
    return(s)

service = build("customsearch", "v1", developerKey="AIzaSyCR5BPcANHoawEeKzbaKFZdoJQqSR-GABY")
 
def read_article(file_text):
    #file = open(file_path, "r")
    ##INSERT FILE NAME IN FUNCTION CALL BELOW######
    #bcr = PlaintextCorpusReader(file_path, 'bernie.txt')
    filedata = file_text
    #filedata = bcr.raw()
    #for word in filedata.split():
    #    if word == 'Mr.':
    #        filedata[word] = 'Mr'
    article = filedata.replace("\n\n", '. ').replace('Mr.', 'Mr').replace("\r", ' ').replace('\n', ' ').split('. ')
    articlez = []
    for line in article:
        if line == '':
            continue
        if line[0] == '\n':
            line = line[1:]
        articlez.append(line)
    sentences = []
    for sentence in articlez:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: 
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    return similarity_matrix

def generate_summary(file_text, top_n=5):
    nltk.download("stopwords")
    stop_words = stopwords.words('english')
    summarize_text = []
    sentences =  read_article(file_text) 
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words) 
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)    
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))
    return(gather_sources(summarize_text))

def gather_sources(summarize_text):
    res = service.cse().list(q = summarize_text[0], cx = '006228756898570140581:ng9oxqpjpii').execute()
    links = []
    lenn = len(res['items'])
    if lenn > 3:
        lenn = 3
    for i in range(lenn):
        links.append(res['items'][i]['link'])
    for items in links:
        print(items)
    for items in summarize_text:
        print("---- " + items + '\n')
    print(summarize_text[0])
    return [links, summarize_text]
#####INSERT FILE PATH IN THE FUNCTION CALL BELOW!!!###########
#generate_summary( "C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\wapo\\by_article", 2)
