from tkinter import *
import sqlite3
import nltk
import pickle
import random
import math
from nltk.corpus import wordnet as wn



time_hours=[num for num in range(1,13)]
time_minutes=[00,15,30,45]
time_am=[" a.m"," p.m."]
yes_no=["Yes", "No"]
probably=[",probably",",as far as I know",",I think",",in my opinion",",I am sure",",definitely",",of course",",though I am not sure",",you should confirm it by googling it."]
days=[num for num in range(1,31)]
months=["January","February","March","April","May","June","July",'August','September','October','November','December']
year=[num for num in range(2015,2021)]
why_did_you=["My choice","None of your business", "It's a free country","Mah LiFe , Mah Rulez","I don't need to explain myself to civilized monkeys like you","It's beyond primitive human comprehension"]
yes_really=["of course","what would I gain by lying to you?","I don't make mistakes like you humans","really","pinky swear"]
no_really=["I was just kidding","I just said that to see your reaction","I was joking","I would totally gain something by lying to you, right? *facepalm*"]

def Question(wordDict,wordlist):
#    print("inside")
#    print(ques)
    output=''
    try:
        inv_dict = {}
        main=''
        ind=0   
        go=0
        is_present={"you":0,'the':0,'will':0,'be':0,'to':0,'when':0,'why':0,'his':0,'your':0,'do':0,'did':0,'me':0,'my':0 ,'really':0 }
        for k, v in wordDict.items():
            inv_dict[v] = inv_dict.get(v, [])
            inv_dict[v].append(k)
            #        print(len(wordlist))
        for word in wordlist:
            #            print(wordDict[word])
            if word=='?':
                go=1
            if word in is_present.keys():
                is_present[word]=1
            if wordDict[word][0]=='N':
                #            print(word)
                main_type='noun'
                try:
                    if(wordDict[wordlist[wordlist.index(word)-1]][0]=='N' or ((wordDict[wordlist[wordlist.index(word)-1]]=='CC' or wordDict[wordlist[wordlist.index(word)-1]]=='IN') and wordDict[wordlist[wordlist.index(word)-2]][0]=='N')):
                        of=wordlist[wordlist.index(word)-1]
                        main=main+' '+of+' '+word
                        
                        #                    print(main)
                    elif(wordDict[wordlist[wordlist.index(word)-1]]=='DT'):
                        main=wordlist[wordlist.index(word)-1]+' ' +word
                        
                        #                    print(main)
                    else:
                        main=word
                    
                except:
                    main=word
            elif wordDict[word][0]=='J':
                main=word
                main_type='adjective'
            elif wordDict[word][:2]=='PR':
                main=word
                main_type='pronoun'
        if go==0:
    #        print("NO ?")
            return 0,output
        if(is_present['really']==1 and len(wordlist)==2):
            ans=random.choice(yes_no)
            if(ans=="Yes"):
                 output = "Yes, "+random.choice(yes_really)
            else:
                 output = "No, %s"%(random.choice(no_really))
                 
            return 1,output
        if(is_present['when']):
    #        print("wdt")
                
            if(is_present['you']==1 and is_present['be']==0):
    #            print(main)
    #            print(quality)
                if(is_present['will']==1):
                    try :
                        verb1=inv_dict['VB'][ind]
                        verb1=verb1+' '
                    except :
                        verb1=inv_dict['VBP'][0]
                        verb1=verb1+' '
                    try :
                        verb2=inv_dict['VBG'][0]
                        verb2=verb2+' '
                    except :
                        verb2=''
                        verb2=verb2+' '
                    try :
                        to=inv_dict['TO'][0]
                        to=to+' '
                    except :
                        to=''
                        
                    output = "I will %s%s%s%s on %d %s"%( verb1,verb2,to,main,random.choice(days),random.choice(months))
                    return 1,output
                elif(is_present['do']==1):
                    try :
                        verb1=inv_dict['VB'][ind]
                        verb1=verb1+' '
                    except :
                        verb1=inv_dict['VBP'][0]
                        verb1=verb1+' '
                    try :
                        to=inv_dict['TO'][0]
                        to=to+' '
                    except :
                        to=''
                    if(is_present['your']==1):
                        my='my '
                    else:
                        my=''
                    output = "I  %s%s%s%s at %d:%d %s"%(verb1,to,my,main,random.choice(time_hours),random.choice(time_minutes),random.choice(time_am))
                    return 1,output
                elif(is_present['did']==1):
                    try :
                        verb1=inv_dict['VB'][ind]
                    except:
                        verb1=inv_dict['VBP'][0]
                    try :
                        to=inv_dict['TO'][0]
                        to=to+' '
                    except :
                        to=''
                    if(is_present['your']==1):
                        my='my '
                    else:
                        my=''
                    verb1=verb_convert.verb_past(verb1)
    #                print(verb1)
                    
                    verb1=verb1+' '
                    output = "I  %s%s%s%s at %d:%d %s"%(verb1,to,my,main,random.choice(time_hours),random.choice(time_minutes),random.choice(time_am))
                    return 1,output
            elif(is_present['your']==1):
                    output = "My %s is on %d %s "%(main,random.choice(days),random.choice(months))
                    return 1,output
            else:
                output = "%s is on %d %s "%(main,random.choice(days),random.choice(months))
                return 1,output
            
                    
                    
         #   if(you_val==1 and will_val==1 and be_val==1):
        if(wordlist[0]=="is" or wordlist[0]=="are"):
            
            if(is_present['you']==1 and is_present['why']==1):
                ans=random.choice(yes_no)
                try:
                    inv_dict['VBD']
                    vbd=1;
                except:
                    vbd=0
                if(ans=="Yes"):
                    output = "Yes, that's why."
                elif(vbd==1):
                    output = "No,There were other reasons"
                else:
                    output = "No,There are other reasons"
            else:    
                output = "%s %s."%(random.choice(yes_no),random.choice(probably))
            return 1,output
        if(wordlist[0]=="can"):
            if wordlist[1]=='i':
                no_vb=0
                ans=random.choice(yes_no)
                me='me'
                my='my'
                if ans=="Yes":
                    nt=''
                else:
                    nt="'t"
                try :
                    verb=inv_dict['VB'][0]
                except:
                    no_vb=1
                
                if(no_vb==1):
                    try:
                        verb=inv_dict['VBP'][0]
                    except:
                        verb=inv_dict['RB'][0]
                if(is_present['you']==0):
                    me=''
                if(main_type!='noun'):
                    main=''
                if(is_present['your']==0):
                    my=''
                try:
                    verb_ing=inv_dict['VBG'][0]
                except:
                    verb_ing=''
                output = "%s ,you can%s %s %s %s%s %s"%(ans,nt,verb,verb_ing,me,my,main)
                return 1,output            
            elif(is_present['you']==1):
                no_vb=0
                ans=random.choice(yes_no)
                you='you'
                your='your'
                if ans=="Yes":
                    nt=''
                else:
                    nt="'t"
                try :
                    verb=inv_dict['VB'][0]
                except:
                    no_vb=1
                
                if(no_vb==1):
                    try:
                        verb=inv_dict['VBP'][0]
                    except:
                        verb=inv_dict['RB'][0]
                if(is_present['me']==0):
                    you=''
                if(main_type!='noun'):
                    main=''
                if(is_present['my']==0):
                    your=''
                try:
                    verb_ing=inv_dict['VBG'][0]
                except:
                    verb_ing=''
                output = "%s ,I can%s %s %s %s%s %s"%(ans,nt,verb,verb_ing,you,your,main)
                return 1,ouptut
            else:
                no_vb=0
                ans=random.choice(yes_no)
                if ans=="Yes":
                    nt=''
                else:
                    nt="'t"
                try :
                    verb=inv_dict['VB'][0]
                except:
                    no_vb=1
                
                if(no_vb==1):
                    try:
                        verb=inv_dict['VBP'][0]
                    except:
                        verb=inv_dict['RB'][0]
                try:
                    verb_ing=inv_dict['VBG'][0]
                except:
                    verb_ing=''
                output = "%s ,%s can%s %s %s %s"%(ans,wordlist[1],nt,verb,verb_ing,main)
                return 1,output
        if(is_present['why']==1 and is_present['did']==1 and is_present['you']==1):
            output = '%s'%(random.choice(why_did_you))
            return 1,output
        return 0,output
    except:
        return 0,output

wordval={}

def connectDB():                                    #function that connects to the database and returns the connection and its cursor.
    connect = sqlite3.connect('chats.sqlite')
    cur = connect.cursor()
    return connect, cur

connect, cur = connectDB()

def admin():                                     #admin function serves to feed responses as admin.
    user = ''
    while user!='bye':
        cur.execute('SELECT Input FROM sents WHERE Response1 IS NULL;') #select an input for which response is not known.
        resp = cur.fetchone()
        cur.execute('select id from sents where Response1 IS NULL;')
        r = cur.fetchone()
        if not resp:
            print('All queries addressed. Thank You')  
            return
        resp = resp[0]
        lil=resp
        print('Pal: '+ lil)
        cur.execute('select sentkey from words where id>? and id = ?;', (0,r[0]))  #sentence key corresonding to the input which was found aas the closest match in program run.
        respgiven = cur.fetchone()
        cur.execute('select Response1 from sents where id>? and id=?;', (0, respgiven[0])) 
        sentgiven = cur.fetchone()
        print('I gave the answer:', sentgiven[0]) #this is what the bot gave the answer as.
        print('Do you want to keep this? (y/n)')
        take = input()
        if take == 'n':   #admin wants to change it.
            print('Admin:')
            user=input()
            cur.execute('update sents set Response1 =? where id=?;', (user, r[0]))  #update response.
            cur.execute('update words set sentkey=? where id=?;', (r[0], r[0]))   #update sentence key.
        else:
            cur.execute('update sents set Response1=? where id=?;', (sentgiven[0], r[0]))  #if admin wants to keep the response, store it. 
        connect.commit()
    exit()

#all the functions below that correspond to parts of speech, help in storing the respective word in the database in its proper place.

def check(word, cur, m):
    one = word + '.n' + '.01'
    if not wn.synsets(word):
        return
    try:
        left = wn.synset(one)
    except:
        return
    for i in range(1, m):
        arr = []
        cur.execute('select noun1 from words where id>? and id=?;', (0, i))
        noun = cur.fetchone()
        if noun and noun[0]!=None:
            if wn.synsets(noun[0]):
                noun = noun[0] + '.n.01'
                try:
                    right = wn.synset(noun)
                    arr.append(1/left.path_similarity(right))
                except:
                    pass
                #print('check4')
        cur.execute('select noun2 from words where id>? and id=?;', (0, i))
        noun = cur.fetchone()
        if noun and noun[0]!=None:
            if wn.synsets(noun[0]):
                noun = noun[0] + '.n.01'
                try:
                    right = wn.synset(noun)
                    arr.append(1/left.path_similarity(right))
                except:
                    #print('error')
                    pass
                
        cur.execute('select noun3 from words where id>? and id=?;', (0, i))
        noun = cur.fetchone()
        if noun and noun[0]!=None:
            if wn.synsets(noun[0]):
                noun = noun[0] + '.n.01'
                try:
                    right = wn.synset(noun)
                    arr.append(1/left.path_similarity(right))
                except:
                    pass
                #print('check4')
        cur.execute('select noun4 from words where id>? and id=?;', (0, i))
        noun = cur.fetchone()
        if noun and noun[0]!=None:
            if wn.synsets(noun[0]):
                noun = noun[0] + '.n.01'
                try:
                    right = wn.synset(noun)
                    arr.append(1/left.path_similarity(right))
                except:
                    pass
                
                #print('check4')
        if arr:
            #print('check3')
            for j in range(1, 5):
                query = 'select similar' + str(j) + ' from words where id=' + str(i)
                cur.execute(query)
                sim = cur.fetchone()
                if not sim or sim==None:
                    if j==4:
                        j=5
                    continue
                else:
                    break
            if j<5:
                query = 'update words set similar' + str(j) + '=' + str(min(arr)) + ' where id=' + str(i)
                cur.execute(query)
    connect.commit()
        

def Noun(word, cur, m):
    check(word, cur, m)
    cur.execute('select id from words where noun1 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun1=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun2 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun2=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun3 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun3=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun4 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun4=? where id=?;',  (word, d[0]))
        return

def Pronoun(word, cur, m):
    cur.execute('select id from words where noun1 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun1=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun2 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun2=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun3 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun3=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where noun4 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set noun4=? where id=?;',  (word, d[0]))
        return


def Adjective(word,cur, m):
    cur.execute('select id from words where adj1 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set adj1=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where adj2 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set adj2=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where adj3 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set adj3=? where id=?;',  (word, d[0]))
        return


def Modal(word,cur, m):
    cur.execute('select id from words where modal IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set modal=? where id=?;',  (word, d[0]))
        return


def Verb(word,cur, m):
    cur.execute('select id from words where verb1 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set verb1=? where id=?;',  (word, d[0]))
        return

    cur.execute('select id from words where verb2 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set verb2=? where id=?;',  (word, d[0]))
        return
    cur.execute('select id from words where verb3 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set verb3=? where id=?;',  (word, d[0]))
        return



def wh(word,cur, m):
    cur.execute('select id from words where wh IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set wh=? where id=?',  (word, d[0]))
        return


def Adverb(word,cur, m):
    cur.execute('select id from words where adv1 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set adv1=? where id=?;',  (word, d[0]))
        return

    cur.execute('select id from words where adv2 IS NULL and new = 1;')
    d = cur.fetchone()
    if d:
        cur.execute('update words set adv2=? where id=?;',  (word, d[0]))
        return

weights = {}      #the dictionary of weights assigned. This is updated for every new input.

ratings = {'N':8, 'V': 10, 'P':6, 'J': 0.8, 'R':0.4, 'W':6, 'M': 6}  #relative ratings of the parts of speech.

def finddenom(worddict, cur):
                #function to find the total weight of the current sentence.
    global wordval
    total = 0
    for word in worddict:
        if word in wordval:
            weights[word] = 1/wordval[word]      #weight = 1/(its occurence in the corpora)
        else:
            weights[word]=0.1
    for i in worddict:
        pos = worddict[i]
        pos = pos[0]
        if pos in ratings:
            weights[i] = weights[i]*ratings[pos]   #weights * rating of the POS.
            total = total+ weights[i]
    cur.execute('update words set denom=? where new=?;', (total, 1))
    return total, weights

def findW(cur, m, connect):
    for j in range(1, 5):
        q = 'select similar' + str(j) + ' from words where id=1;'
        cur.execute(q)
        d = cur.fetchone()
        if not d or d==None:
            j = j-1
            break
    for i in range(1, m):
        try:
            W = 0
            for k in range(1, j+1):
                q = 'select similar' + str(k) + ' from words where id>0 and id=' + str(i)
                cur.execute(q)
                e = cur.fetchone()
                if not e or e[0]==None:
                    pass
                else:
                    if e[0]==2:
                        f=2.5
                    else:
                        if e[0]==1:
                            f = 2
                        else:
                            f = e[0]
                    W = W + 1/f
        except:
            continue
        cur.execute('update words set W=? where id=?;', (W, i))
    connect.commit()

def findN(m):       #function to find best match from the database.
    conn = sqlite3.connect('chats.sqlite')
    conn.row_factory = sqlite3.Row      #this makes fetchone() return a row.
    c = conn.cursor()
    #print(m)
    rowtot = 0
    for i in range(1, m):
        try:
            c.execute('update words set rowtot=? where id=?', (0, i))
            c.execute('select * from words where new =? and id=?', (0, i))
            r = c.fetchone()
            r = dict(r)     #convert the row to a dictionary: 'column name': word.
            for j in r:
                if r[j] in weights:
                    rowtot = rowtot + weights[r[j]]     #add word's weight to the rowtotal.
            c.execute('select denom from words where id>? and id=?;', (0, i))
            denom = c.fetchone()[0]
            rowtot = rowtot/denom       #rowtotal/sentence's total weight (%match)
            c.execute('update words set rowtot=? where id=?;', (rowtot, i))
            #print(rowtot, i)
            rowtot = 0
        except:
            continue
    conn.commit()
    conn.close()
        
def ngrams(new_sent,match_words):

        new_words = nltk.word_tokenize(new_sent)
        match_words = nltk.word_tokenize(match_words)

        a=len(new_words)
        b=len(match_words)

        
        new_list = []
        for i in range(0,a):
                new_list.append(0)
                
        match_list = []
        for i in range(0,b):
                match_list.append(0)
                
        mtc = []
        mtc1 = []
        for i in range(0,a):
                mtc.append(-1)
                mtc1.append(0.5)	
                for j in range(0,b):
                        if(new_words[i]==match_words[j]):
                                mtc[i]=j
                                mtc1[i]=j-i			
                                break


        ur=0
        next=0
        count=1
        ngram = []
        sind1 = []
        eind1 = []
        k=0
        for i in range(0,a-1):
                if (mtc1[i]==mtc1[i+1]) and (mtc[i]!=-1) :
                        count=count+1
                        """#check7
                        print('p')"""
                else:
                        if(count!=1):
                                ngram.append(count)
                                sind1.append(mtc[i]-count+1)
                                eind1.append(mtc[i])			
                                """#check6
                                print(ngram[k])"""
                                k=k+1
                                count=1
                        else:
                                continue
                if (i==a-2) and (count!=1):
                        ngram.append(count)
                        sind1.append(mtc[i]-count+2)
                        eind1.append(mtc[i]+1)
                        k=k+1
                        """#check6
                        print(ngram[k])"""
        """#check
        print(k)"""

        if(ngram):

                sind = sorted(sind1)
                eind = sorted(eind1)

                start = sind[0]
                end = eind[0]
                ngram1=[]

                
                if(k>1):
                        for i in range(1,k):
                                """#check
                                print('p')"""

                                if(sind[i]==eind[i-1]+1):
                                        end=eind[i]
                                else:	
                                        ngram1.append(end-start+1)
                                        start=sind[i]
                                        end=eind[i]
                                if(i==k-1):
                                        """#check
                                        print(start)
                                        print(end)"""
                                        ngram1.append(end-start+1)
                
                else:
                        ngram1=ngram

                l=len(ngram1)
                
                
                weight=0
                for i in range(0,l):
                        weight = weight + math.sqrt(ngram1[i])

                weight = weight*weight/b

                return weight/2

                #return weight
        else:
                weight = 0
                return weight/2

def findB(cur, m, user, connect):
    for i in range(1, m):
        try:
            cur.execute('select Input from sents where id>? and id=?;', (0, i))
            samp = cur.fetchone()[0]
            B = ngrams(user, samp)
            cur.execute('update words set B=? where id=?;', (B, i))
        except:
            continue
    connect.commit()

def findbest(cur, m, connect):
    for i in range(1, m):
        try:
            x = 35
            y = 33
            z = 40
            cur.execute('select rowtot from words where id>? and id=?;', (0, i))
            n= cur.fetchone()
            cur.execute('select B from words where id>? and id=?;', (0, i))
            b= cur.fetchone()
            cur.execute('select W from words where id>? and id=?;', (0, i))
            w= cur.fetchone()
            if not n or n[0]==None:
                n[0] = 0
            if not b or b[0]==None:
                b[0] = 0
            if not w or w[0]==None:
                w[0] = 0
            cur.execute('select denom from words where id>? and id=?;', (0, i))
            den = cur.fetchone()[0]
            cur.execute('select Input from sents where id>? and id=?;', (0, i))
            sent = cur.fetchone()[0]
            sent = nltk.word_tokenize(sent)
            length = len(sent)
            if length<=5:
                x = 25
                y = 30
            elif length<=10:
                x = 30
                y = 25
            else:
                y = 20
            if den < 0.004:
                x = x/50
            elif den < 0.01:
                x = x/10
            elif den < 0.05:
                x = x/3
            elif den < 0.1:
                x = 2*x/3
            cur.execute('select Input from sents where id>? and id=?;', (0, i))
            sent = cur.fetchone()[0]
            sent = nltk.word_tokenize(sent)
            length = len(sent)
            if length<=5:
                x = 25
                y = 30
            elif length<=10:
                x = 30
                y = 25
            else:
                y = 20
            total = x*n[0] + y*b[0] + z*w[0]
            cur.execute('update words set total=? where id=?;', (total, i))
        except:
            continue
    cur.execute('select max(total) from words;')
    ma = cur.fetchone()[0]
    cur.execute('select id from words where total>? and total=?;', (0, ma))
    match = cur.fetchone()[0]
    connect.commit()
    return match

def stop_remove(sent):       
    from nltk.corpus import stopwords
    stop=stopwords.words('english')
    final={}
    for i in sent:
        if i in ['.', '?', ',','!']:
            continue
        if i not in stop:
            final[i]=sent[i]    
    return final
    
cats = { 'N' : Noun,
         'J' : Adjective,
         'M' : Modal,
         'V' : Verb,
         'W' : wh,
         'R' : Adverb,
         'P' : Pronoun,
}
flag=0  
li=[]  
def main(str1):
    global cur,flag,connect,m, weights, cats
    user=str1
    if 1>0:
        flag=1
        #user input taken.
        if str1 == 'admin':
            admin()
            exit()
    li=[str1]
        
    if 1>0:
        num = random.randint(0, 2)
        cur.execute('select id from sents where Input=?;', li)
        #print('check1')
        l = cur.fetchone()
        
        #resp = cur.fetchone()
        if not l or l[0]==None:           #if exact match not found.
            #print('check2')
            wordlist = nltk.word_tokenize(str1)
            q_wordlist = nltk.word_tokenize(user)
            worddict = nltk.pos_tag(wordlist)       #pos tagged dictionary of the words of the sentence.              
            worddict = dict(worddict)               #duplicates removed.
            wordlist = list(worddict.keys())   #duplicates have been removed now, both in wordlist and worddict.
            newdict = stop_remove(worddict)
            index = 0
            a,b=Question(worddict,q_wordlist)
            if a==1:
                return b

            cur.execute('select max(id) from sents;')
            n = cur.fetchone()[0]
            q = 'insert into words(id) values(' + str(n+1) + ');'
            cur.execute(q)
            cur.execute('update words set new=? where id=?;', (1, n+1))
            for i in range(1, n+1):
                cur.execute('update words set similar1=NULL where id>? and id=?;', (0, i))
                cur.execute('update words set similar2=NULL where id>? and id=?;', (0, i))
                cur.execute('update words set similar3=NULL where id>? and id=?;', (0, i))
                cur.execute('update words set similar4=NULL where id>? and id=?;', (0, i))
                cur.execute('update words set W=0 where id>? and id=?;', (0, i))
                cur.execute('update words set B=0 where id>? and id=?;', (0, i))
            connect.commit()
            m = n+1
            ##        cur.execute('select id from words where new=1;')
            ##        m = cur.fetchone()
            ##        m = m[0]
            while(index<len(wordlist)):
                #cur.execute('select id from words where new = 1;')
                #Id = cur.fetchone()
                #Id = Id[0]
                word = wordlist[index]
                char = worddict[word]
                char = char[0]            #current word's pos tag
                if char[0] not in cats.keys():
                    index = index+1
                    continue
                cats[char](word, cur, m)     #function call corresponding to the pos tag to insert the word in the right column in a new record in the database,
                index = index+1
            connect.commit()
            #cur.execute('select * from words where id = 2')
            output = open('density.txt', 'rb')      #file containing the dictionary of frequency of words in the corpora is opened.
            global wordval
            wordval = pickle.load(output)
            inpval, weights = finddenom(worddict, cur)      #find the weight of the current sentence, for future use.
            connect.commit()
            connect.close()
            findN(m)     #find the best match.
            #print(best)
            connect, cur = connectDB()
            findW(cur, m, connect)
            findB(cur, m, user, connect)
            best = findbest(cur, m, connect)
            cur.execute('select sentkey from words where new = ? and id =?;', (0, best))
            key = cur.fetchone()
            l = key
            key = key[0]
            #print(key)
            cur.execute('update words set sentkey=? where id=?;', (key, m))      #set sentence key temporarily to the best match found.
            q = 'insert into sents(id) values(' + str(m)  + ');'
            cur.execute('insert into sents(id) values(' + str(m)  + ');')                                                         #insert the new sentence into the sents DB.
            cur.execute('update sents set Input=? where id=?;', (user, m))
            cur.execute('update words set new = ? where id=?', (0, m))       #update new to 0.
            connect.commit()
        resp = None
        while not resp or resp[0]==None:
            if num==-1:
                resp = ('Please change the topic',)
            else:
                q = 'select Response' + str(num+1) + ' from sents where id=' + str(l[0])
                cur.execute(q)
                resp = cur.fetchone()
                num = num-1
            
        resp = resp[0]
        weights = {}
        return resp
    


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")
        self.text.insert(0.0,'hi everyone')

    def createWidgets(self):
        
        self.text=Text(self,bg='#2c3e50',fg='#3ed8ba',width=70,height=17,wrap=WORD,font=30)
        self.text.grid(row=1,sticky=W)
        self.text.insert(0.0,'Ivana : Hello\n')

        self.photo=PhotoImage(file='bot.png')
        self.myButton = Label(self,image = self.photo)
        self.myButton.grid(row=0)

        self.enter=Entry(self,width=70,font=25)
        self.enter.grid(row=2, sticky=W)
        def reveal(enter):
            str1 = self.enter.get()
            self.text.insert(END, ('User : '+str1 + '\n') )
            self.enter.delete(0,END)
            if str1.lower()=='bye':
                connect.close()
                exit()
            str2 = main(str1.lower())
            self.text.insert(END,('Ivana : '+str2 + '\n'))
            self.text.see(END)
	    
        self.enter.bind('<Return>',reveal)

        
    def __init__(self,master=None):
        Frame.__init__(self, master,background='#26bd9f')
        self.master.title('Ivana : The Chatbot')
        self.master.geometry("700x580+400+100")
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

            
