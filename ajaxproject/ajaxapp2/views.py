from django.http import JsonResponse
from django.shortcuts import render
from .models import Userdata,Entry
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# Create your views here.
# def check(request):
#     return render(request,'check.html')

# def save(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(name)
#         print(email)
#         print(password)      
#         # print('post request')

#     # return JsonResponse('success')
#     return HttpResponse('saved success')


# def save(request):
#     if request.method == 'GET':
#         age = request.GET['age']
#         return HttpResponse('saved success aa gyaa')

# def call(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')        
#         print(name,email,password)
#         print('successfully sent')
#     return HttpResponse('testing ho rha')

# def ajaxtest(request):
#     return render(request,'ajaxtest.html')

    # return JsonResponse()
# def check(request):
#     return render(request,'check.html')

# def home1(request):
#     return render(request,'home1.html')

# def call(request):
#     if request.method == 'POST':
#         age = request.POST.get('age')
#         print(age)
#         print('successfully sent it')
#     return HttpResponse('testing check')





# Create your views here.
def home1(request):
    return render(request,"home1.html")
    

def show(request):
    data = Entry.objects.all()
    return render(request,"show.html",{'data':data})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry(ID = ID,data1=data1,data2=data2).save()
        msg="Data Stored Successfully"
        return render(request,"home1.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    data1 = data2 = "Not Available"
    for data in Entry.objects.filter(ID=ID):
        data1 = data.data1
        data2 = data.data2
    return render(request,"edit.html",{'ID':ID,'id':id,'data1':data1,'data2':data2})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(ID=ID).update(data1=data1,data2=data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")