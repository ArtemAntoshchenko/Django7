from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .forms import FeedbackForm


def BooleanField(request):
    if request.method == 'GET':
        form=FeedbackForm()
        return render(request, 'bool.html', {'form':form})
    else:
        form=FeedbackForm(request.POST)
        if form.is_valid():
            check=form.cleaned_data['check']
            if (check):
                return HttpResponse('Да')
            else:
                return HttpResponse('Нет')
        else:
            return HttpResponse('something')






