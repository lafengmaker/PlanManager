from django.shortcuts import render_to_response
def my_render_to_response(request,responseTo,x={}):
    x["user"]=request.user;
    return render_to_response(responseTo,x);
def getPfromRequest(request,key="p"):
    if key in request.GET:
        return request.GET[key]