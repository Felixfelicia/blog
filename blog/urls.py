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
from products.views import main_view, products_view, categories_view, product_details_view, product_create_view, category_create_view

# hello_view, redirect_to_youtube_view, goodbye_view, now_date_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('categories/', categories_view),
    path('products/<int:pk>/', product_details_view),
    path('products/create/', product_create_view),
    path('categories/create/', category_create_view)

    # path('hello/', hello_view),
    # path('youtube/', redirect_to_youtube_view),
    # path('now_date/', now_date_view),
    # path('goodbye/', goodbye_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
