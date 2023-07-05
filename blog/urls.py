"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from blog import settings
from products.views import MainCBV, ProductsCBV, CategoriesCBV, ProductDetailCBV, ProductCreateCBV, CategoryCreateCBV
from users.views import RegisterCBV, LoginCBV, LogoutCBV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainCBV.as_view()),
    path('products/', ProductsCBV.as_view(template_name='products/products.html')),
    path('categories/', CategoriesCBV.as_view(template_name='products/categories.html')),
    path('products/<int:pk>/', ProductDetailCBV.as_view(template_name='products/detail.html')),
    path('products/create/', ProductCreateCBV.as_view(template_name='products/create.html')),
    path('categories/create/', CategoryCreateCBV.as_view(template_name='products/categories.html')),

    path('users/register/', RegisterCBV.as_view(template_name='users/register.html')),
    path('users/login/', LoginCBV.as_view(template_name='users/login.html')),
    path('users/logout/', LogoutCBV.as_view())


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
