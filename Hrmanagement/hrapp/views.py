from django.shortcuts import render
from .models import Customuser,Role
from django.shortcuts import redirect
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import RoleSerializer
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

def index(request):

    if 'user_id' not in request.session:
      return redirect('signin')
    else:
      user_id=request.session['user_id']
      user = Customuser.objects.filter(id=user_id)
    
    context = {
      'user':user
    }
    return render(request,'dashboard.html',context)
    
def profile(request):
    user_id=request.session['user_id']
    user_detail = Customuser.objects.filter(id=user_id).first()

    context = {
      'user_detail':user_detail
   }
    return render(request,'profile.html', context)
  

def profileUpdate(request):
  if request.method =='POST':
   user_id = request.POST.get('user_id')
   user_detail = Customuser.objects.get(id=user_id)
   user_detail.first_name = request.POST.get('first_name')
   user_detail.last_name = request.POST.get('last_name')
   user_detail.email = request.POST.get('email')
   user_detail.mobile =request.POST.get('mobile')
   user_detail.address =request.POST.get('address')
   user_detail.password=request.POST.get('password')
    
   user_detail.save()
   return redirect('profile')

def updateimage(request):
  if request.method=='POST':
      user_id = request.POST.get('user_id')
      user_detail = Customuser.objects.get(id = user_id)
      # if len(request.FILES)!=0:
      #     os.remove(Customuser.image.path)
      if len(request.FILES)!=0:
       user_detail.image=request.FILES['image']

      user_detail.save()  
  return redirect('profile')
  
    

def signin(request):
   if request.method == 'GET':
            context = ''
            return render(request, 'sign-in.html', {'context': context})

   elif request.method == 'POST':
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            if Customuser.objects.filter(email=email, password=password).exists():
             user_detail = Customuser.objects.filter(email=email).first()

             #session set
             request.session['user_id'] = user_detail.id
             return redirect('index')
            else:
              messages.error(request,'Invalid Email or Password.')
              return render(request, 'sign-in.html')

def logout(request):
    try:
        del request.session['user_id']
        return redirect('signin')
    except:
        pass
    return HttpResponse("You're logged out.")

@csrf_exempt
def role_api(request):
  if request.method == 'GET':
    json_data=request.body
    stream=io.ByteIO(json_data)
    pythondata=JSONParser().parse(stream)
    id=pythondata.get('id',None)
    if id is not None:
      role=Role.objects.get(id=id)
      serializer=RoleSerializer(role)
      json_data=JSONRenderer().render(serializer.data)
      return HttpResponse(json_data,content_type='application/json')
    
    role = Role.objects.all()
    serializer = RoleSerializer(role,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

  if request.method == 'POST':
    json_data = request.body
    stream  = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = RoleSerializer(data = pythondata)
    if serializer.is_valid():
      serializer.save()
      res = {'msg' : 'Data Created'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data,content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')
      