"""p3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from p3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('html_demo',views.html_demo,name='html_demo'),
    path('html_demo1',views.html_demo1,name='html_demo1'),
    path('html_demo2',views.html_demo2,name='html_demo2'),
    path('html_demo3',views.html_demo3,name='html_demo3'),
    path('html_demo4',views.html_demo4,name='html_demo4'),
    path("ab/<ab>",views.ab,name='ab'),
    path("gre/<num>",views.gre,name='gre'),
    path("add/<num>",views.add,name='add'),
    path("add1/<a>/<b>",views.add1,name="add1"),
    

]
