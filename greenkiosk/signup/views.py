from django.shortcuts import render

from  .models import Signup

from  .forms import SignUploadForm

def update_account(request):
    if request.method=="POST":
     form=SignUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=SignUploadForm()
    return render(request,'customer/sign_up.html',{'form':form})
