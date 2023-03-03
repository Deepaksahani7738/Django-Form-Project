from django.shortcuts import render,HttpResponse,redirect
from .models import students
from .forms import postdata



def index(request):
    if request.method=='POST':
        data=postdata(request.POST)
        if data.is_valid():
            res=data.save()
            res.save()
            return redirect('home')
    else:
        form=postdata()
        result={'form':form}
        return render(request,'index.html',result)




# Create your views here.
