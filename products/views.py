from django.db.models import Q
from django.shortcuts import render, redirect

# HttpResponse, redirect
import datetime

from products.models import Product, Category
from products.forms import ProductCreateForm, CategoryCreateForm
from products.constants import PAGINATION_LIMIT


# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        pproducts = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        if search_text:
            pproducts = products.filter(Q(title__contains=search_text) | Q(description__contains=search_text))

        context_data = {
            'products': pproducts,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {'categories': categories
                        }

        return render(request, 'products/categories.html', context=context_data)


def product_details_view(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, 'products/detail.html')
        context_data = {
            'product': product
        }
        return render(request, 'products/detail.html', context=context_data)


def product_create_view(request):
    if request.user.is_anonymous:
        return redirect('/products/')

    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, file = request.POST, request.FILES
        form = ProductCreateForm(data, file)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price')
            )

            return redirect('/products/')
        return render(request, 'products/create.html', context={'form': form})


def category_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CategoryCreateForm
        }
        return render(request, 'products/categories.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = CategoryCreateForm(data)

        if form.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title')
            )
            return redirect('/products/')
        return render(request, 'products/categories.html', context={'form': form})
# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello! It's my project")
#
#
# def redirect_to_youtube_view(request):
#     if request.method == 'GET':
#         return redirect("https://youtube.com")
#
#
# def now_date_view(request):
#     if request.method == 'GET':
#         now = datetime.datetime.now()
#     return HttpResponse(now)
#
#
# def goodbye_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Goodbye user!")
