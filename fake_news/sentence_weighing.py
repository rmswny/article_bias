# imports 
import nltk, requests, Levenshtein as lev, bs4, sklearn, jellyfish
#
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
from operator import itemgetter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
# from nltk.stem import PorterStemmer
#
# This file will remove stop words, stem and compare sentences to the article title (and summary)
# and use their value as comparison for the most comparable 
# and later use these sentences/paragraphs to query google / etc
#
# test_title = 'Medicare for All and Beyond, Sanders Uses the Senate as His Launching Pad'
test = ''
test_para = 'I ran for president; I got 13 million votes, going over 1,700 delegates to the Democratic convention, and got more young peoples votes than Clinton and Trump combined, Mr Sanders boasted in an interview in his Washington office. And I thought that those 13 million people deserved a voice in Democratic leadership. The Medicare for All Act unveiling  its fifth iteration  comes as Mr Sanderss $18 million fund-raising haul has made him an instant front-runner in a very crowded field.  But in many ways he is still the same old Bernie, as many of his colleagues like to say  a gruff and sometimes grating presence in a chamber that prides itself on civility.  He still knows how to rankle.  He ran as a Democrat for president in 2016, then shunned the entreaties of Democratic leaders and sought re-election last year as an independent.  His push for Medicare for All runs counter to the wishes of top Democrats like Senator Chuck Schumer, the minority leader, and Speaker Nancy Pelosi, who are trying to de-emphasize it. At the same time, Mr Sanders  who has long cast himself as an outsider  has joined party leadership, which gives him a voice in plotting strategy.  His post as chair of outreach  a job that did not exist until he and Mr Schumer created it after the 2016 presidential election  has also given him license and a small budget to travel the country doing what he likes best: rallying the progressive left to resist President Trump.'
test_url = 'https://www.nytimes.com/2019/04/10/us/politics/bernie-sanders-medicare-for-all.html?action=click&module=Top%20Stories&pgtype=Homepage'
#
def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    altered_string = []
    for word in word_tokens:
        if word not in stop_words:
            altered_string.append(word)
    print(altered_string)
    # temp = stem_text(altered_string)
    return altered_string
#
def sentence_parse(paragraph):
    list_of_sentences = []
    pos_start = 0
    pos_period = paragraph.find('.')
    if pos_period == -1:
        return paragraph.strip()
    else:
        while pos_period != -1:
            temp = paragraph[pos_start:pos_period+1]
            list_of_sentences.append(str(temp.strip()))
            pos_start = pos_period+1
            pos_period = paragraph.find('.',pos_start+1)
    # for s in list_of_sentences:
        # print(s)
    return list_of_sentences
#
def get_title(url):
    requester = requests.get(url)
    content = requester.content
    bs_content = BeautifulSoup(content, features='lxml')
    title_unparsed = bs_content.title.string
    pos = title_unparsed.find("- The New York Times")
    title = title_unparsed[0:pos]
    return title
#
def calc_jaro(title,sentence):
    value =  jellyfish.jaro_distance(title,sentence)
    return value
#
def calc_jaro_winkler(title,sentence):
    value = jellyfish.jaro_winkler(title,sentence)
    return value
def calc_cosine(title, paragraph):
    # this function does not break it down by sentences as the results for entire paragraph are better/higher #
    # simple for loop and different input changes this no problem #
    title = [title]
    title.append(paragraph)
    tfidf_vectorizer  = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(title)
    result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    value = round(result_cos[0][1],4)
    # value_rounded = round(value,4)
    # print('Complete: ' + str(value))
    # print('Complete: ' + str(value_rounded))
    return (paragraph,value)
#
def calc_fuzzy(title, sentence):
    fuzz_ratio = fuzz.ratio(title.lower(),sentence.lower()) / 100
    fuzz_partial_ratio = fuzz.partial_ratio(title.lower(),sentence.lower()) / 100
    fuzz_token_sort_ratio = fuzz.token_sort_ratio(title,sentence) / 100
    fuzz_token_set_ratio = fuzz.partial_token_set_ratio(title,sentence) / 100
    # tuple_all = (sentence, fuzz_ratio,fuzz_partial_ratio,fuzz_token_sort_ratio,fuzz_token_set_ratio) # unsure if separate is better than averaged results
    tuple_combined = ((fuzz_ratio+fuzz_partial_ratio+fuzz_token_sort_ratio+fuzz_token_set_ratio)/4) # averages the result from the four methods
    return tuple_combined
#
def calc_lev(title, sentence):
    ratio = lev.ratio(title.lower(),sentence.lower())
    return ratio
#
def gather_results(title, paragraph):
    #
    lev_result_list =[]
    fuzzy_result_list = []
    jaro_result_list = []
    jarowinkler_result_list = []
    aggregate_list = []
    #
    sentence_list = sentence_parse(paragraph)
    for sentence in sentence_list:
        lev,fuzzy,jaro,winkler = calc_lev(title,sentence),calc_fuzzy(title,sentence),calc_jaro(title,sentence),calc_jaro_winkler(title,sentence)
        average_results = (lev+fuzzy+jaro+winkler) / 4
        temp_tuple = (sentence,average_results)
        aggregate_list.append(temp_tuple)
    aggregate_list.sort(key=itemgetter(1),reverse=True)
    return aggregate_list
#
def main(url,para_list):
    all_sentences = []
    all_paragraphs = []
    title = get_title(url)
    for p in para_list:
        results_by_sentences = gather_results(title,p) # returns a list of all sentences in the paragraph, sorted by their weight
        for sentence in results_by_sentences:
            print(sentence)
            all_sentences.append(sentence)
        cosine_p = calc_cosine(title,p)
        all_paragraphs.append(cosine_p)
        # next iteration
    # done with loop here
    all_sentences.sort(key=itemgetter(1),reverse=True) # sentences are now sorted by value
    all_paragraphs.sort(key=itemgetter(1),reverse=True) # paragraphs are now sorted by value
    return all_sentences,all_paragraphs


    # old functionality # 
    # sentence_parse(test_para)
    # title = get_title(test_url)
    # gather_results(title,test_para)
    # gather_results(get_title(test_url),test_para)
#