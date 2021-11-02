# from ajaxproject.ajaxapp import models
# from django.http.response import JsonResponse
from collections import UserDict
from django.http import JsonResponse
from django.shortcuts import render
# from django.http import request
from .forms import StudentRegistration
from .models import User
# Create your views here.

def home(request):
    frm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'home.html',{'form':frm,'data' : stud})


def save(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST) #whatever data is coming in form then we validate the form
        if form.is_valid():
            stuid = request.POST.get('stid')
            name = request.POST['name'] #under post ['name'] is coming from ajax.html which i used here mydata = {name: nm, email: em, password:pw };
            email = request.POST['email']
            password = request.POST['password']
            if(stuid == ''):
                usr = User(name = name, email=email, password=password)
            else:
                usr = User(id=stuid, name = name, email=email, password=password)
            usr.save()
            print("saved")
            stud = User.objects.values()
            # print(stud)
            stud_data = list(stud) 
            return JsonResponse({'status':'Save', 'studn_data':stud_data})
        else:
            print("error")
            return JsonResponse({'status': 'Error'})




def delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk=id)  #pk-primary key, get using only jis per we are clicked.
        pi.delete()
        print("this id is deleted : ", id)
        return JsonResponse({'status' : 'working'}) #console.log(data)- then showing status like.. {status: 'working'}
    else : 
        return JsonResponse({'status' : 'Not working'})

def edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(pk=id)
        stud_data= {"id": student.id, "name" : student.name, "email": student.email, "password" : student.password}
        return JsonResponse(stud_data)



# def save(request):
#     if request.method == "POST":
#         form = StudentRegistration(request.POST) #whatever data is coming in form then we validate the form
#         if form.is_valid():
#             pass
#         return JsonResponse('passed saved')
        #     name = request.POST['name'] #under post ['name'] is coming from ajax.html which i used here mydata = {name: nm, email: em, password:pw };
        #     email = request.POST['email']
        #     password = request.POST['password']
        #     usr = User(name = name, email=email, password=password)
        #     usr.save()
        #     print("saved")
        #     return JsonResponse({'status':'Save'})
        # else:
        #     print("error")
        #     return JsonResponse({'status': 'Error'})























# def sav_book(request):
#     nam = request.GET['name']
#     price = request.GET['price']
#     pag = request.GET['page']
#     bk = Book(name=nam, price=price, page=pag)
#     try:
#         bk.save();
#         print(bk)
#         return HttpResponse('success')
#     except:
#         return HttpResponse('fail')

# def getallbook(request):

#     getbook = Book.objects.all()
#     print(getbook)
#     serializer = BookSerializer(getbook[1])
#     print (serializer)

    # return JsonResponse({"data" : serializer})

