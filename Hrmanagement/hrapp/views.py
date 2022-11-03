from django.shortcuts import render
from .models import Customuser
from django.shortcuts import redirect
from django.shortcuts import render,HttpResponse
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
    return render(request,'profile.html')

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
                return render(request, 'sign-in.html')

def logout(request):
    try:
        del request.session['user_id']
        return redirect('signin')
    except:
        pass
    return HttpResponse("You're logged out.")
