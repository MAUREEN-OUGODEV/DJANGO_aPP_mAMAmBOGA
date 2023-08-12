from django.shortcuts import render

from  .models import Vendor

from  .forms import VendorUploadForm
# Create your views here.
def vendor_details_views(request):
    if request.method=="POST":
     form=VendorUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=VendorUploadForm()
    return render(request,'vendor/vendor_details.html',{'form':form})