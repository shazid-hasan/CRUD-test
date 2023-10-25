from django.shortcuts import render,HttpResponse
#from newapp.models import Employees

def home(request):
    if request.method=='GET':
        name=request.GET.get('name')
        email=request.GET.get('email')
        phone=request.GET.get('phone')

        emp={
            'name':name,
            'email':email,
            'phone':phone
        }


        return render(request,'index.html',{'emp':emp})
        #return redirect('crud.html')

# Create your views here.
def crud(request):
    if request.method=='GET':
        name=request.GET.get('name')
        email=request.GET.get('email')
        phone=request.GET.get('phone')

        emp={
            'name':name,
            'email':email,
            'phone':phone
        }


        return render(request,'crud.html',{'emp':emp})