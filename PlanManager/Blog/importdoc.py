#encoding=utf-8
import re
from models import  article
import datetime
def getDocList(file):    
    doclist=[];
    r=re.compile("标 题:")
    b=re.compile(" ")
    c="first";
    art= article()
    art.title=c
    art.text=""
    for line in file.readlines():
        m=r.match(line)
        if m :
            print line+",,,,,,,,,,,,,,,,,,,,,,"
            z= r.sub("",line)
            c=b.sub("",z)
            doclist.append(art);
            art=article()
            art.title=c
            art.text=""
        else:
            line=b.sub("",line)                
            art.text=art.text+line
    doclist.append(art);
    return doclist
def importsave(list):
    for doc in list:
        templ=article.objects.filter(title__exact=doc.title)
        n=len(templ)
        if n==0:
            doc.cdate=datetime.datetime.now();
            print doc.title
            doc.save()
        #doc.save();
        
            


