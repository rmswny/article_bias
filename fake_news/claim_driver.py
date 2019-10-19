import get_paragraphs as gp
import clean_paragraphs as cp
import sentence_weighing as sw
#
def main(input_url):
    ## get post request from hitting submitting button into main ! ##
    parsed_article = gp.paragraph_parse(input_url)
    cleansed_article = cp.para_to_file(parsed_article)
    sentence_scores,paragraph_score = sw.main(input_url, cleansed_article)
    a=5

main("https://www.nytimes.com/2019/04/10/us/politics/bernie-sanders-medicare-for-all.html?action=click&module=Top%20Stories&pgtype=Homepage")