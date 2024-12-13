"""
URL configuration for FreshShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from myshop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_product/',views.add_product, name='add_product'),
    path('cart/', views.cart_view, name='cart'),
     path('auth/', include('dj_rest_auth.urls')),  # Login/logout
    path('auth/registration/', include('dj_rest_auth.registration.urls')), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
