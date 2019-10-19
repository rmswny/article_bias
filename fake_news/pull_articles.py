import newspaper, os, sys, io
from newspaper import Article
## to f: article text  ##  news_pool, 
## to g: article url (article.url), date, article text (article.text), article title (article.title)
breit_paper = newspaper.build('https://breitbart.com/', memoize_articles=False, language='en', fetch_images=False)
infowars_paper = newspaper.build('https://www.infowars.com/', memoize_articles=False, language='en', fetch_images=False)
nytimes_paper = newspaper.build('https://www.nytimes.com/', memoize_articles=False, language='en', fetch_images=False)
wapo_paper = newspaper.build('https://www.washingtonpost.com/', memoize_articles=False, language='en', fetch_images=False)

if breit_paper:
    f = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\breitbart\\long\\long.txt', 'a', encoding="utf-8")
    c = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\breitbart\\by_article\\count.txt', 'r', encoding="utf-8")
    i = int(c.read())
    c.close()
    for z in range(1,len(breit_paper.articles)):
        file_name = 'C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\breitbart\\by_article\\breit_article'
        g = io.open(file_name + str(i) + '.txt', 'w', encoding="utf-8")
        urls = breit_paper.articles[z].url
        articlez = Article(urls)
        articlez.download()
        articlez.parse()
        if articlez.text:
            f.write(articlez.text)
            f.write('\n\n\n')
            g.write(articlez.url)
            g.write('\n')
            g.write(articlez.title)
            g.write('\n')
            g.write(articlez.text)
            g.write('\n\n\n')
            g.close()
        i = int(i)
        i = i + 1
    c = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\breitbart\\by_article\\count.txt', 'r', encoding="utf-8")
    c.write(i)
    c.close()
    f.close()
if infowars_paper:
    h = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\infowars\\long\\long.txt', 'a', encoding="utf-8")
    d = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\infowars\\by_article\\count.txt', 'r', encoding="utf-8")
    j = int(d.read())
    d.close()
    for zz in range(1,len(infowars_paper.articles)):
        file_name = 'C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\infowars\\by_article\\infowars_article'
        k = io.open(file_name + str(j) + '.txt', 'w')
        urls = infowars_paper.articles[zz].url
        articlez = Article(urls)
        articlez.download()
        articlez.parse()
        s = articlez.text.replace('\ufeff', '')
        s = s.encode('ascii', 'ignore').decode('ascii')
        h.write(s)
        h.write('\n\n\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n\n\n')
        k.close()
        j = int(j)
        j = j + 1
    d = open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\infowars\\by_article\\count.txt', 'w', encoding="utf-8")
    d.write(j)
    d.close()
    h.close()
if nytimes_paper:
    h = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\nytimes\\long\\long.txt', 'a', encoding="utf-8")
    d = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\nytimes\\by_article\\count.txt', 'r', encoding="utf-8")
    j = int(d.read())
    d.close()
    for zz in range(1,len(nytimes_paper.articles)):
        file_name = 'C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\nytimes\\by_article\\nytimess_article'
        k = io.open(file_name + str(j) + '.txt', 'w')
        urls = nytimes_paper.articles[zz].url
        articlez = Article(urls)
        articlez.download()
        articlez.parse()
        s = articlez.text.replace('\ufeff', '')
        s = s.encode('ascii', 'ignore').decode('ascii')
        h.write(s)
        h.write('\n\n\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n\n\n')
        k.close()
        j = int(j)
        j = j + 1
    d = open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\nytimes\\by_article\\count.txt', 'w', encoding="utf-8")
    d.write(str(j))
    d.close()
    h.close()
if wapo_paper:
    h = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\wapo\\long\\long.txt', 'a', encoding="utf-8")
    d = io.open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\wapo\\by_article\\count.txt', 'r', encoding="utf-8")
    j = int(d.read())
    d.close()
    for zz in range(1,len(wapo_paper.articles)):
        file_name = 'C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\wapo\\by_article\\wapo_article'
        k = io.open(file_name + str(j) + '.txt', 'w')
        urls = wapo_paper.articles[zz].url
        articlez = Article(urls)
        articlez.download()
        articlez.parse()
        s = articlez.text.replace('\ufeff', '')
        s = s.encode('ascii', 'ignore').decode('ascii')
        h.write(s)
        h.write('\n\n\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n')
        k.write(s)
        k.write('\n\n\n')
        k.close()
        j = int(j)
        j = j + 1
    d = open('C:\\Users\\matthew.kirshy\\Desktop\\CSE-442-Fake-News-Web-Application\\article_db\\wapo\\by_article\\count.txt', 'w', encoding="utf-8")
    d.write(str(j))
    d.close()
    h.close()