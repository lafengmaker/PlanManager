from django.shortcuts import  redirect
from PlanManager.settings import STATICFILES_DIRS
import os
import Image
from  models import imgpic,article
from django.contrib.auth.decorators import login_required
import logging
from PlanManager.webUtil import my_render_to_response,getPfromRequest
#from django.core.urlresolvers import reverse
logger = logging.getLogger(__name__)
    
@login_required()
def images(request):
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
    return my_render_to_response(request,"blog/image.html",{"fl":images});

@login_required(redirect_field_name='prepage')
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

@login_required()
def doclist(request):
    articlelist=article.objects.all();
    return my_render_to_response(request,"blog/doclist.html",{"doclist":articlelist});

@login_required()
def showdoc(request,p):    
    doc=article.objects.get(id=p);
    return my_render_to_response(request,"blog/doc.html",{"doc":doc});
    
        