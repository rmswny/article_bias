import re, nltk
#
# take a list of paragraphs
# summarize each one
# compare that summary to the title / headline
# sort a container based on the similary scoring
# return the top K based on similary scoring
# send those summarized paragraphs to a query function 
#
# test_encoded = "Senator Bernie Sanders stepped to the lectern on Wednesday, red-faced and rumpled as ever, with a placard screaming \xef\xbf\xbdMedicare for All,\xef\xbf\xbd and likened his quest for a government-run universal health plan to earlier movements for women\xef\xbf\xbds rights, civil rights, workers\xef\xbf\xbd rights and gay rights."
test_para = ['I ran for president; I got 13 million votes, going over 1,700 delegates to the Democratic convention, and got more young people�s votes than Clinton and Trump combined,� Mr. Sanders boasted in an interview in his Washington office. �And I thought that those 13 million people deserved a voice in Democratic leadership.� The Medicare for All Act unveiling � its fifth iteration � comes as Mr. Sanders�s $18 million fund-raising haul has made him an instant front-runner in a very crowded field. But in many ways he is still the �same old Bernie,� as many of his colleagues like to say � a gruff and sometimes grating presence in a chamber that prides itself on civility. He still knows how to rankle. He ran as a Democrat for president in 2016, then shunned the entreaties of Democratic leaders and sought re-election last year as an independent. His push for Medicare for All runs counter to the wishes of top Democrats like Senator Chuck Schumer, the minority leader, and Speaker Nancy Pelosi, who are trying to de-emphasize it. At the same time, Mr. Sanders � who has long cast himself as an outsider � has joined party leadership, which gives him a voice in plotting strategy. His post as �chair of outreach� � a job that did not exist until he and Mr. Schumer created it after the 2016 presidential election � has also given him license and a small budget to travel the country doing what he likes best: rallying the progressive left to resist President Trump.'
]
test_list = [
    'Senator Bernie Sanders stepped to the lectern on Wednesday, red-faced and rumpled as ever, with a placard screaming �Medicare for All,� and likened his quest for a government-run universal health plan to earlier movements for women�s rights, civil rights, workers� rights and gay rights.',
    'What we are involved in is not just health care legislation,� he declared, flanked by admiring doctors in lab coats, Democratic senators and one of his rivals for the Democratic presidential nomination, Senator Kirsten Gillibrand of New York. �We are involved in a great struggle',
    'Medicare for All is not passing this Congress. Its cost is still unknown, the mechanisms to pay for it still the subject of debate. But behind Mr. Sanders�s choreographed theatrics were the unmistakable politics of 2020 and his campaign for president, a campaign that never really ended with the election of Donald J. Trump.',
    'After the 2016 election, Democrats made efforts to pull Mr. Sanders, a political independent from Vermont, into the fold with a newly minted leadership post. But that has only bolstered his platform to seek the presidency � and gave him more power to disrupt the party�s status quo.',
    'I ran for president; I got 13 million votes, going over 1,700 delegates to the Democratic convention, and got more young people�s votes than Clinton and Trump combined,� Mr. Sanders boasted in an interview in his Washington office. �And I thought that those 13 million people deserved a voice in Democratic leadership.�',
    'The Medicare for All Act unveiling � its fifth iteration � comes as Mr. Sanders�s $18 million fund-raising haul has made him an instant front-runner in a very crowded field. But in many ways he is still the �same old Bernie,� as many of his colleagues like to say � a gruff and sometimes grating presence in a chamber that prides itself on civility. He still knows how to rankle.',
    'He ran as a Democrat for president in 2016, then shunned the entreaties of Democratic leaders and sought re-election last year as an independent. His push for Medicare for All runs counter to the wishes of top Democrats like Senator Chuck Schumer, the minority leader, and Speaker Nancy Pelosi, who are trying to de-emphasize it.',
    'At the same time, Mr. Sanders � who has long cast himself as an outsider � has joined party leadership, which gives him a voice in plotting strategy. His post as �chair of outreach� � a job that did not exist until he and Mr. Schumer created it after the 2016 presidential election � has also given him license and a small budget to travel the country doing what he likes best: rallying the progressive left to resist President Trump.',
    'More than a half-dozen members of Congress are running for president, but few have used their seats as adroitly as Mr. Sanders to burnish a brand. He announced his candidacy in 2015 on a patch of grass, known as the Swamp, outside the Capitol � an unusual locale given that senators are not supposed to mix official business with politics.',
    'Not long after the 2016 campaign, when some moderate Democrats worried he would help foster primary challenges against them, he brought his chief strategist, Jeff Weaver, to meet behind closed doors with his colleagues to tutor them on how to appeal to his millennial base.',
    'He went on CNN to debate tax policy with Senator Ted Cruz, Republican of Texas. He held dozens of rallies in 2017 to whip up opposition to Mr. Trump�s plan to repeal the Affordable Care Act.',
    '�I think he feeds off these crowds; there�s no question about it,� said Larry Cohen, chairman of Our Revolution, the organization that spun out of Mr. Sanders�s 2016 campaign. Mr. Cohen added that Mr. Schumer realized there was �a huge benefit� to bringing on Mr. Sanders: �You don�t just bring him back after that kind of relative success and just treat him as the junior senator from Vermont.�',
    'Bernie Sanders�s proposal has big implications for consumers and the health care industry.',
    'Mr. Sanders also staked out policy crusades to address concerns that arose during his 2016 campaign. Criticized for lacking foreign policy experience, he teamed with two Republicans � Mike Lee of Utah and Rand Paul of Kentucky � to pass a resolution calling for an end to American military involvement in Saudi Arabia�s war in Yemen. He also embraced a criminal justice overhaul after being accused of not being sensitive enough to issues of racial injustice.',
    'He shrewdly hired the Democratic operative Tyson Brody, who compiled opposition research on him for Hillary Clinton�s campaign in 2016. Representative Ro Khanna, Democrat of California and a co-chairman of Mr. Sanders�s 2020 campaign, calls Mr. Sanders �the perfect insider-outsider� who, unlike Mr. Trump, at least knows how Washington works',
    'The last time he embarked on a run for the White House, in April 2015, Mr. Sanders, was viewed by his colleagues as a kind of oddball figure � a self-identified democratic socialist on a Don Quixote, tilting-at-windmills quest.',
    'Now the senator has a different problem: So many Democrats sound so much like Bernie Sanders that some are asking why America needs Bernie Sanders. His Medicare for All bill is a case in point. Its co-sponsors include at least four Senate Democrats who are running against him: Ms. Gillibrand, Cory Booker of New Jersey, Elizabeth Warren of Massachusetts and Kamala Harris of California.',
    'But in planting a political stake in the ground with Medicare for All, Mr. Sanders is effectively challenging his Democratic rivals to follow suit, which could come back to haunt whomever is chosen as the party�s nominee, said David Krone, a former chief of staff to Harry Reid, the former Senate Democratic leader.',
    '�I�m very concerned that his campaign is creating a litmus test for other candidates and that�s a dangerous path,� Mr. Krone said.',
    'The Medicare for All Act would provide health insurance to all Americans under a single plan run by the government and financed by taxpayers; private insurers could remain in business but could only provide benefits, such as elective surgery, not covered by the government. The 2019 version includes coverage for long-term care, perhaps increasing its appeal but also its cost.',
    'The rollout � complete with Sanders-esque finger jabs and talk of �doctahs� and �dollahs� � was live-streamed from a packed room in the Dirksen Senate Office Building. After Mr. Sanders poked Mr. Trump, the president�s press secretary, Sarah Huckabee Sanders (no relation), poked back, denouncing �self-proclaimed socialist Bernie Sanders� for �proposing a total government takeover of health care.�',
    'We asked a handful of economists and think tanks to find out.',
    'The plan�s main drawback � and one that alarms many moderate Democrats and Democratic leadership � is the cost: as high as $32 trillion over 10 years, according to two different studies. But the Sanders camp cites various other studies, including one by the RAND Corporation, to back up its assertion that Medicare for All would save middle-class families money by decreasing their premiums and out-of-pocket costs.',
    'As to why America needs Bernie Sanders, Mr. Sanders�s answer is simple: He was there first.',
    '�Find out how many folks in the 1980s were going up to Canada to learn about Medicare for All,� he said, adding: �In 1999, I took a busload of Vermonters across the Canadian border to purchase low-cost prescription drugs in Canada. O.K., I was the first member of Congress to do that. So are other people talking about the greed of the pharmaceutical industry? Yes. Check out who was there first.�',
    'He also took a subtle swipe at another of his competitors, Senator Amy Klobuchar of Minnesota. Of her idea for a trillion-dollar infrastructure plan, he said, �Well, we were talking about that how many years ago? 2015?�',
    'Ms. Klobuchar then swiped back. �While a big infrastructure plan has been kicked around for years, I can get it done,� she wrote in an email message.',
    'Mr. Sanders has always been a scowling presence in the Senate. He plows through the Capitol corridors, always too busy to talk, stingy with his smiles. (�If you worked here, you wouldn�t smile either,� he said.)',
    'His official website offers a hint of where the job falls on his priority list. Until Wednesday, after this article pointed it out, it had not been updated to reflect his re-election in 2018 and still said he was �serving his second term after winning re-election in 2012.�',
    'He is thinner these days, having dropped 10 pounds on no particular diet � or at least none that he cares to share. (�By not eating,� he said, when asked how he did it.) And though his �national support has given Bernie more credibility,� in the words of Senator Richard J. Durbin of Illinois, the No. 2 Democrat, his colleagues say not much has changed.',
    '�He�s Bernie,� said Senator Tim Kaine of Virginia, who ran for vice president alongside Mrs. Clinton after she defeated Mr. Sanders for the 2016 Democratic nomination. �Whether that�s running or just being Bernie, he kind of does what he does.'
]
#
def write_para(paragraph):
    with open('tp.txt','a') as out_file: # append for the whole paragraph, clear after done with summary
        out_file.write(paragraph)
#
def clear_file():
    open("tp.txt",'w').close()
#
# def remove_stopwords(sentence):
#     stop_words = set(stopwords.words('english'))
#     word_tokens = word_tokenize(sentence)
#     filtered_sentence = [w for w in word_tokens if not w in stop_words]
#     sentence = ""
#     for word in filtered_sentence:
#         sentence+=word+" "
#     return sentence
#
def filter_sentence(sentence):
    filtered_sentence = ""
    splitted = sentence.split()
    for word in splitted: # all words in the sentence
        if word.find("b'") != -1 and word.find("\\x") != -1:
            pos_b = word.find("b'")
            temp = word[0:pos_b] # whole string before b'
            temp+=word[pos_b+2:len(word)] # string after b'
            length  = 4 # \x123 is example escape sequence
            t = ""
            start_pos = 0
            inc_pos = temp.find("\\x")
            while inc_pos != -1:
                t += temp[start_pos:inc_pos] # everything before tag
                start_pos = inc_pos+length
                inc_pos = temp.find("\\x",start_pos)
            filtered_sentence = t # should be trimmed string
        elif word.find("b'") != -1:
            temp = ""
            start_pos = 0
            inc_pos = word.find("b'")
            while inc_pos != -1:
                temp += word[start_pos:inc_pos] # substring from start to before b'
                start_pos = inc_pos+2 # length of 'b
                inc_pos  = word.find("b'", start_pos) # finds next one
                if inc_pos == -1:
                    temp += word[start_pos:len(word)]
            filtered_sentence+=temp+" "
        elif word.find("\\x") != -1:
            temp = ""
            start_pos = 0
            inc_pos = word.find("\\x")
            while inc_pos != -1:
                temp +=word[start_pos:inc_pos]
                start_pos=(inc_pos+4)
                inc_pos = word.find("\\x",start_pos)
                if inc_pos == -1:
                    temp += word[start_pos:len(word)]
            filtered_sentence+=temp+" "
        else: # no bad characters
            filtered_sentence+=word+" "
    # print("filtered: " + filtered_sentence)            
    return filtered_sentence
#
def para_to_file(parag_list):
    # 3rd index has more than one period for testing
    cleansed_article = []
    full_paragraph = ""
    counter = len(parag_list)
    for p in parag_list:
        print("Paragraphs remaning: "+str(counter))
        sentences_in_paragraph = p.split('.')
        for word in sentences_in_paragraph:
            temp = str(word.encode('utf-8'))
            fn_temp = filter_sentence(temp)
            full_paragraph+=fn_temp+'. '
        cleansed_article.append(full_paragraph)
        full_paragraph=""
        counter-=1
    print('Complete.')
    return cleansed_article