

from django.shortcuts import render

from  .models import Sign_in

from  .forms import SignUploadForm

def vendor_account(request):
    if request.method=="POST":
     form=SignUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=SignUploadForm()
    return render(request,'vendor/vendor_details.html',{'form':form})

