"""shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from appShelter import views

# Шаблон включает в себя символы ^ и $. Они являются символами регулярного выражения, которые имеют особое значение:
# ^ означает «требовать, чтобы шаблон совпадал с начала строки», а $ означает «требовать, чтобы шаблон совпадал до конца строки».
#
# Данный подход лучше объяснять на примере. Если бы мы использовали шаблон '^hello/' (без завершающего $), тогда любой URL,
# начинающийся с /hello/ совпадал бы с шаблоном. Например, такие как /hello/foo и hello/bar, а не только /hello/. Аналогично,
# если бы мы опустили начальный ^ (т.е., 'hello/$'), Django будет обрабатывать любой URL, который оканчивается на hello/.
# Например, такой как foo/bar/hello/. Если бы мы просто указали в качестве шаблона 'hello/', без символов ^ и $, тогда шаблону бы
# соответствовал любой URL, содержащий hello/. Например, такой как /foo/hello/bar. Следовательно, мы используем оба этих специальных
# символа для точного определения нашего шаблона. Он должен совпадать только с /hello/, не больше и не меньше.

urlpatterns = [
    path('^admin/$', admin.site.urls),
    path('^index/$', views.index, name = 'index'),
    path('^modelindex/$', views.modelindex,  name = 'modelindex')

]
