from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        password2 = request.POST['确认密码']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html',{'用户名错误':'用户名已存在'})
        except User.DoesNotExist:
            if password1 == password2:
                User.objects.create(username=user_name, password=password1)
                return redirect('首页')
            else:
                return render(request, 'signup.html', {'密码错误':"你两次输入的密码不一致"})
