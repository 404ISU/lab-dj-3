import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import CatImage
from ..myproject.settings import MEDIA_URL


def random_cat_image(request, count=1):
    cat_images=list(CatImage.objects.all())
    if count>len(cat_images):
        count=len(cat_images)
    random_images=random.sample(cat_images, count)

    if count==1:
        return JsonResponse({"source": f"http://{request.get_host()}{MEDIA_URL}{random_images[0].image}"}, safe=False)
    else:
        sources=[f"http://{request.get_host()}{MEDIA_URL}{image.image}" for image in random_images]
        return JsonResponse({"source":sources}, safe=False)

def index(requset):
    cat_images=CatImage.objects.all()
    return render(requset, 'cats/index.html',{'cat_images':cat_images})
