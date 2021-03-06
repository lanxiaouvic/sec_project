"""secondtreasures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
import bookstore.views

urlpatterns = [
    url(r'^$', bookstore.views.index, name='index'),
    url(r'^booklist/$', bookstore.views.jlist, name='jlist'),
    url(r'^books/$', bookstore.views.BookList.as_view(), name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', bookstore.views.BookDetail.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]

