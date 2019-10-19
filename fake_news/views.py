from django.shortcuts import render, redirect
from .models import Publisher
from . import forms
from .atricle_parser import * #article_parser_fn, article_smmry_fn
from textblob import TextBlob

## https://textblob.readthedocs.io/en/dev/index.html
## pip install -U textblob
## i think we can use this to train our model for biased words and return a predictive scoring:
## http://www.nltk.org/api/nltk.classify.html#module-nltk.classify.positivenaivebayes
## so we feed it a bunch of 'biased' articles and return our prediticve score

def index(request): 
    form = forms.FormName()
    ## creates a new form from our DB model in 'forms.py'
    context = { 'form':form, }
    ## context is a dictionary mapping template vars to py objects
    if request.method == 'POST':
    ## form method POST in 'index.html' html form tag (means post something)
        form = forms.FormName(request.POST)
        ## save the user submitted link to a python object
        form.save(commit=False)
        ## save the python object to the DB
        return redirect('forms_output', permanent=True)
        ## redirects to same page after save is made so that form is clear and resubmission will not repeate save
    return render(request, 'fake_news/home.html', context)
   ## render function takes: request obj, dictionary for vars, and an optional third argument

def forms_output(request):
    last_submitted_article = Publisher.objects.order_by('-date_submitted') 
    articleText = None
    article_summary = None
    article_keywords = None
    pol_score = None
    sub_score = None
    listz = []
    link = str(Publisher.objects.all().last())
    if link != 'None':
        articleText = article_parser_fn(link) ## should be changed to summary of each paragraph?
        #articleSMMRY = article_smmry_fn(link)
        #article_summary = articleSMMRY.sm_api_content
        #article_keywords = articleSMMRY.sm_api_keyword_array
        listz = generate_summary(articleText, 2)
        links = listz[0]
        summ = listz[1]
        blob = TextBlob(articleText)
        pol_score = blob.sentiment.polarity
        sub_score = blob.sentiment.subjectivity
    context = {
        'last_submitted_article': last_submitted_article,
        'articleText': articleText,
        'links': links,
        'summ': summ,
        #'article_summary': article_summary,
        #'article_keywords': article_keywords,
        'pol_score': pol_score,
        'sub_score': sub_score
        }
    return render(request, 'fake_news/output.html', context)