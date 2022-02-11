from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import profileform
from .models import erormsg

# Create your views here.
def modelview(request):
    ProfileForm=profileform()
    if request.method=="POST":
        ProfileForm=profileform(request.POST)
        if ProfileForm.is_valid():
            Erormsg=erormsg(name=ProfileForm.cleaned_data['name'],
                            family=ProfileForm.cleaned_data['family'])

            erormsg.save()
            # ProfileForm=profileform()
            # return HttpResponse('o')
        # else:
        #     print (ProfileForm.errors)
    

    context={
        "formdata":ProfileForm
    }
    return render(request,'ermsgg/err.html',context)
   
