from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse

from .models import *

"""
Запрос:
    При url http://(site name)/getUpdateInfo&version=(version))&name=(name)
    version - актуальная версия прошивки
    name - название устройства

Ответ:
    json формат
    Переменная ans:
        True - требуется обновление
        False - обновление не требуется
    Переменная url: есть только при ans = True
        Содержит url для скачивания обновления
"""
def getUpdateInfo(request, version, name):
    obj = list(update_info.objects.filter(name=name))
    if obj == []:
        return JsonResponse({'ans': 'false'})

    curr_vers = max([i.version for i in obj])

    if int(version) >= curr_vers:
        print(version, curr_vers)
        return JsonResponse({'ans': 'false'})

    if curr_vers != 0:
        obj = update_info.objects.filter(version = curr_vers).first()
        return JsonResponse({'ans': 'true', 'url': 'https://192.168.100.9/download&fname=' + obj.file})

"""
fname - полное имя с разрешением

const:
    path - путь ко всем бинарникам от manage.py
"""
def download(request, fname):
    path = "../data/BinFiles/"
    fl = open(path + fname, "rb")
    response = HttpResponse(fl, content_type="application/octet-stream")
    response["Content-Disposition"] = 'attachment; filename="' + fname + '"'
    return response
