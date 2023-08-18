from django.shortcuts import render
from .forms import RefundUploadForm

# Create your views here.
def refund_view(request):
    if request.method=="POST":
     form=RefundUploadForm(request.POST)
     if form.is_valid():
        form.save()
    else:
      form=RefundUploadForm()
    return render(request,'refund/refund.html',{'form':form})

