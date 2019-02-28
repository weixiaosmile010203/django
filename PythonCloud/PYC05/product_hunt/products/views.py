from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.




def products(request):
    return render(request, 'products.html')

@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publist.html')
    elif request.method == 'POST':
        title = request.POST["标题"]
        intro = request.POST["介绍"]
        url = request.POST["APP链接"]
        icon = request.FILES["APP图标"]
        image = request.FILES["大图"]
        #if title and intro and url and icon and image

        product = Product()
        product.title = title
        product.intro = intro
        product.url = url
        product.icon = icon
        product.image = image

        product.pub_date = timezone.datetime.now()
        product.hunter = request.user

        product.save()

        return redirect('首页')
