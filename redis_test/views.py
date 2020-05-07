from django.shortcuts import render,HttpResponse
from django.views.decorators.cache import cache_page
import time
# Create your views here.

@cache_page(10*60)
def check_redis(request,*args,**kwargs):
    t = time.time()
    return HttpResponse("%s"%t)


# tern模块 celery

