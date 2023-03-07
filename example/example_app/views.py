import os
import xxhash

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import etag


def index(request):
    return render(request, 'index.html')


# ETAG GENERATORS

def get_css_etag(request, filename):
    filepath = os.path.join(os.getcwd(), 'static', 'css', filename)
    with open(filepath, "rb") as f:
        hex = xxhash.xxh32_hexdigest(f.read())
    return hex

def get_js_etag(request, filename):
    filepath = os.path.join(os.getcwd(), 'static', 'js', filename)
    with open(filepath, "rb") as f:
        hex = xxhash.xxh32_hexdigest(f.read())
    return hex


# STATIC VIEWS

@etag(get_css_etag)
def static_css(request, filename):
    filepath = os.path.join(os.getcwd(), 'static', 'css', filename)
    if os.path.exists(filepath):
        response = HttpResponse(open(filepath))
        response['Cache-Control'] = 'no-cache'
        response['Content-Type'] = 'text/css'
        return response
    else:
        return HttpResponse(status=404)
    
@etag(get_js_etag)
def static_js(request, filename):
    filepath = os.path.join(os.getcwd(), 'static', 'js', filename)
    if os.path.exists(filepath):
        response = HttpResponse(open(filepath))
        response['Cache-Control'] = 'no-cache'
        response['Content-Type'] = 'text/javascript'
        return response
    else:
        return HttpResponse(status=404)

def static_images(request, filename):
    filepath = os.path.join(os.getcwd(), 'static', 'images', filename)
    if os.path.exists(filepath):
        image_format = filename.rsplit('.', 1)[1]
        response = HttpResponse(open(filepath, 'rb'))
        response['Cache-Control'] = 'public, max-age=302400'
        response['Content-Type'] = f'image/{image_format}'
        return response
    else:
        return HttpResponse(status=404)
