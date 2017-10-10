from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
import selenium.webdriver.support.ui as ui
import xmltodict
from .my_keys import MY_SOCPUS_API_KEY, My_MAS_API_KEY1, My_MAS_API_KEY2
from random import random
import sys  
import subprocess
from lxml import html 

casper='/usr/bin/casperjs'
script='/home/gamechanger/Documents/se2/scholarengine/mainpage/try.js'

class articlesnode():
    def __init__(self,title=None,link=None,description=None):
        self.title=title
        self.link=link
        self.description=description

    def addtitle(self,title):
        self.title=title

    def addlink(self,link):
        self.link=link

    def adddescription(self,description):
        self.description=description            

def getResponseFromMAS(query,page_no) :
    return 'F'
    params=casper+' '+script+" --query="+"'"+query+"'"+" --page="+str(page_no)


    stdout_as_string=subprocess.check_output(params,shell=True)
    stdout_as_string=stdout_as_string.decode('utf-8')

    split=stdout_as_string.split('`')
    print(split)
    if split=='null':
        return None

    split.remove('"\n')
    split[0]=split[0][1:]

    mas=[]
    descriptions=[]
    links=[]

    for i in range(len(split)):
        node=articlesnode()
        if i==0 or i%3==0:
            node.addtitle(split[i])
            mas.append(node)    

        elif i in [2,5,8,11,14,17,20,23]:
            descriptions.append(split[i])

        else:
            links.append(split[i])            
        
    
    for i in range(len(descriptions)):        
        mas[i].addlink(links[i])
        mas[i].adddescription(descriptions[i])
        
    return mas

def getResponseFromGS(query,page_no) :
    
    gs_driver = webdriver.PhantomJS()
    query.replace(' ', '+')
    st=0+(page_no-1)*10
    url = 'https://scholar.google.co.in/scholar?start='+str(st)+'&q='+query+'&hl=en&as_sdt=0,5'
    gs_driver.get(url)
    #driver.implicitly_wait(16)
    wait = ui.WebDriverWait(gs_driver,25)
    html = gs_driver.page_source
    soup = BeautifulSoup(html,"lxml")
    mytitles = soup.findAll("h3", { "class" : "gs_rt" })

    time.sleep(7)
    mycitations=soup.findAll("div" ,{"class":"gs_fl"})
    mydescriptions=soup.findAll("div",{"class":"gs_rs"})
    gs_articles=[]
    # if len(mydescriptions)!=0:
    #     for i in mydescriptions:
    #         description.append(''.join(i.findAll(text=True)))

    #     print(description)    
    if not len(mytitles) == 0 :
        j=0
        k=0
        for i in mytitles :
            atag = i.a
            node=articlesnode()

            if not atag is None :
                node.adddescription(''.join(mydescriptions[j].findAll(text=True)))
                j+=1
                txt = ''.join(atag.findAll(text=True))
                node.addtitle(txt)                
                if atag.get('href') is not None:
                    node.addlink(atag.get('href'))
                

            else:
                atag=mycitations[k].a
                node.addtitle(i.text)
                if atag is not None:
                    node.addlink('https://scholar.google.co.in'+atag.get('href'))
                k+=1    
            gs_articles.append(node)    

    gs_driver.quit()            
    # print(gs_articles[1].title)
    # print(gs_articles[1].link)
    # print(gs_articles[1].description)
    # # print(gs_articles[0].description)

    return gs_articles

# if __name__=='__main__':
#     # driver = webdriver.PhantomJS()
#     file=open("popular_tags.txt","r")
#     driver=webdriver.PhantomJS()
#     for query in file:
#         mas_articles=getResponseFromGS(driver,query)
#         print(mas_articles[0])


def getResponseFromSemantic(query,page_no):
    query.replace(" ","+")

    url="https://www.semanticscholar.org/search?q="+query+"&sort=relevance&page="+str(page_no)+"&ae=false"
    driver=webdriver.PhantomJS()
    driver.get(url)
    # wait = ui.WebDriverWait(driver,25)
    html = driver.page_source

    semantic_article=[]

    soup = BeautifulSoup(html,"lxml")
    
    content=soup.findAll("a",{"class":"","data-selenium-selector":"title-link"})

    description=soup.findAll("span",{"class":"abstract"})
    if len(content)!=0:
        j=0
        for i in content:
            node=articlesnode()
            if len(description)==len(content):
                a=''.join(description[j].findAll(text=True))
                a.replace("(More)",'')
                node.adddescription(a)
            node.addlink('https://www.semanticscholar.org'+i.get('href'))    
            a=''.join(i.findAll(text=True))
            node.addtitle(a)
            j+=1
            semantic_article.append(node)
    time.sleep(7)

    # print(semantic_article[0].title)
    # print(semantic_article[0].description)
    driver.quit()
    return semantic_article


def getResponseFromScopus(query,page):
    query = query.replace(' ', '+')
    SCOPUS_SCHOLAR_SITE = 'http://api.elsevier.com/content'
    hdrs = {'Accept': 'application/json', 'X-ELS-APIKey': MY_SOCPUS_API_KEY}
    SCOPUS_SCHOLAR_QUERY_URL = SCOPUS_SCHOLAR_SITE + '/search/scopus?' \
                               + 'query=title-abs-key(' + query + ')&SUBJAREA(COMP)&field=description,title,url,identifier&start='+str((page-1)*10)+'&count=' + str(
        10)
    resp = requests.get(url=SCOPUS_SCHOLAR_QUERY_URL, headers=hdrs)
    scopus_response = resp.json()

    
    scopus_articles = []
    scopus_prism_urls = []
    scopus_urls = []
    description=[]
    scopus=[]
    j=0
    if 'search-results' in scopus_response.keys():
        if 'entry' in scopus_response['search-results'].keys():
            for ss in scopus_response['search-results']['entry']:
           
                if 'dc:title' in ss.keys():
                    node=articlesnode()
                    node.addtitle(ss['dc:title'])
                    scopus.append(node)

                if 'dc:description' in ss.keys():
                    node.adddescription(ss['dc:description'])    

                else:
                    check = 1
                if 'prism:url' in ss.keys():

                    scopus_prism_urls.append(ss['prism:url'])
        else:
            check = 1

    for j in range(len(scopus_prism_urls)):
        file = urlopen(scopus_prism_urls[j])
        data = file.read()
        file.close()
        
        data = xmltodict.parse(data)
        data = data['abstracts-retrieval-response']['coredata']['link']
        scopus_urls.append(data[1]['@href'])
        scopus[j].addlink(data[1]['@href'])
    # for j in range(len(scopus_urls)):
    #     r=requests.get(scopus_urls[j])
    #     soup=BeautifulSoup(r.content,"lxml")
    #     des=soup.findAll("p")
    #     scopus[j].adddescription(des[4].text) 
   

    #print(des)
    # print(json.dumps(scopus_response, sort_keys=True, indent=4, separators=(',', ': ')))
    return scopus


def main(query,page,gs1,ma1,ss1,scopus1):
    acadict={}
    if gs1=='T':
        acadict['gs'] = getResponseFromGS(query, page)
    else:
        acadict['gs'] = None

    if ma1=='T':
        acadict['ma'] = getResponseFromMAS(query,page)
    else:
        acadict['ma']=None

    if scopus1=='T':
        acadict['scopus']=getResponseFromScopus(query,page)
    else:
        acadict['scopus'] = None

    if ss1=='T':
        acadict['semantic']=getResponseFromSemantic(query,page)
    else:
        acadict['semantic'] = None

    if gs1==None and ss1==None and scopus1==None and ma1==None:
        #acadict['semantic'] = getResponseFromSemantic(query, page)
        #acadict['scopus'] = getResponseFromScopus(query, page)
        #acadict['ma'] = getResponseFromMAS(query, page)
        #acadict['gs'] = getResponseFromGS(query, page)
        acadict['semantic'] = None
        acadict['scopus'] = None
        acadict['ma'] = None
        acadict['gs'] = None
    #ma=getResponseFromMAS(query,page)
    #print(scopus[0])
    #print(ma[3].title)    
    # print(ma[3].link)
    # print(ma[3].description)
    #print(semantic[1].title)
    return acadict

























