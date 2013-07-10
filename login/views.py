from django.template import RequestContext
import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def index(request):
    if request.method == "POST":
	form = forms.LoginForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
	    if user is not None:            
		if user.is_active:
                    login(request, user)
		    return redirect('/login/?next=%s' % request.path)  
            	    #return HttpResponse("user is valid and login success.")
                else:
                    return HttpResponse("user is not valid.")
            else:
		return HttpResponse("username and password is incorrect.")
        else:
            return HttpResponse("input is not valid.") 
    else:
        form = forms.LoginForm()
        logout(request)
        return render_to_response('login.html',{'form':form},RequestContext(request))

