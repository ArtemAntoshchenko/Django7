from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .forms import FeedbackForm
import time
import asyncio

async def feedback(request):
    if request.method=='GET':
        feedbackform=FeedbackForm()
        return render(request,'Feedback_form.html', {"form":feedbackform})
    else:
        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # message=request.POST.get('message')
        # print(HttpResponse(f'<h2>Name: {name} email: {email}</h2> <p>message:{message}</p>'))
        # await asyncio.sleep(2)
        return HttpResponsePermanentRedirect('thanks/') 
    
def feedback_thanks(request):
    return render(request,'Feedback_thanks.html')

