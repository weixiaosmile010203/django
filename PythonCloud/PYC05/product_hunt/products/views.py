from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.




def products(request):
    products = Product.objects
    return render(request, 'products.html', {'products': products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product':product})

@login_required
def publish(request):
    if request.method == 'GET':
        return render(request, 'publist.html')
    elif request.method == 'POST':
        title = request.POST["标题"]
        intro = request.POST["介绍"]
        url = request.POST["APP链接"]
        try:
            icon = request.FILES["APP图标"]
            image = request.FILES["大图"]
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
        except Exception as err:
            return render(request, 'publist.html', {'错误':'请上传图片'} )
