# imports #
import bs4, requests, re
from bs4 import BeautifulSoup
#
def lowercase_paragraph(paragraph):
    string_p = str(paragraph)
    para = ""
    for index, char in enumerate(string_p):
        char = char.lower()
        para+=char
    # print(para)
    return para
#
def make_article(article_by_paragraphs):
    full_article = ""
    for para in article_by_paragraphs:
            full_article += para
    return full_article
#
def write_paragraph(para_text):
    # simple function works #
    with open("temp_para.txt",'w') as output_file:
        output_file.write(para_text)
    output_file.close()
#
def get_article(url_link):
    article_request = requests.get(url_link)
    return article_request
#
def paragraph_parse(test_url):
    if "nytimes" not in test_url:
        print("Incorrect Article Type: Not NY Times.")
        return
    else:
        article_request = get_article(test_url) # gets JSON request from valid URL
        content_req = article_request.content #begins beautiful soup process
        content_soup = BeautifulSoup(content_req, features="lxml")
        parsed_article = content_soup.find_all("p", attrs={'class' : re.compile('css')}) # parse JSON by p tags
        article_by_paragraphs = [] # list to hold each paragraph from the article
        counter = 1
        for paragraph in parsed_article:
            if counter > 1:
                article_by_paragraphs.append(paragraph.text)
            counter+=1
        return article_by_paragraphs # list of paragraphs in the atrticle
        # return full_article
#
def main():
    # force NYT only for accurate testing #
    test_url = "https://www.nytimes.com/2019/04/10/us/politics/bernie-sanders-medicare-for-all.html?action=click&module=Top%20Stories&pgtype=Homepage"
    paragraph_parse(test_url)
#
if __name__ == "__main__":
    main()