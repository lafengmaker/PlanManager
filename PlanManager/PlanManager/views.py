#encoding=utf-8
from django.shortcuts import redirect 
#from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import logout
#from django.template import RequestContext
#from django.core.context_processors import csrf
import logging
from webUtil import my_render_to_response 
log=logging.getLogger(__name__)
def index(request):
    return my_render_to_response(request,"index.html");
def mylogout(request):
    log.info("user log out");
    logout(request);
    return redirect('home')
    