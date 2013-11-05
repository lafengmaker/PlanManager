from django.shortcuts import render_to_response ,redirect
from PlanManager.settings import STATICFILES_DIRS
import os
import Image
from  models import imgpic
import logging
logger = logging.getLogger(__name__)
def getPfromRequest(request,key="p"):
    if key in request.GET:
        return request.GET[key]
def images(resquest):
    imagedir=STATICFILES_DIRS[0]+"/showimg/"
    files = os.listdir(imagedir)
    deaultx=850.0
    deaulty=650.0
    images=[]
    for f in files:
        if(os.path.isfile(imagedir + '/' + f)):#need add some file name filter
            img = Image.open(imagedir + '/' + f)
            tup=img.size;
            pic=imgpic()
            pic.url=f;      
            x,y=tup
            logger.info("x====================%i y=======================%i"%(x,y))
            if x<deaultx and y<deaulty :
                pic.x=x
                pic.y=y
            else:
                if (x/deaultx)>(y/deaulty):
                    pic.x=deaultx
                    pic.y=(y/(x/deaultx))
                else:
                    pic.x=(x/(y/deaulty))
                    pic.y=deaulty            
            images.append(pic);
    return render_to_response("blog/image.html",{"fl":images});


def turn90(request):
    imagedir=STATICFILES_DIRS[0]+"/showimg/"
    src=getPfromRequest(request)
    logger.info("ppppppp=====%s"%src)
    if src :
        fname=src.split("/")[-1]
        logger.info("fname=====%s"%fname)
        img=Image.open(imagedir+fname);
        xxx=img.transpose(Image.ROTATE_90);
        
        xxx.save(imagedir+fname)
    return redirect("images")
        