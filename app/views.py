from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form_data=ContactForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'contact.html',context={'form':form})