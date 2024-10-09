from django.shortcuts import render
import requests

def index(request):
    dog_images=[]
    for _ in range(10):
        response=requests.get('https://dog.ceo/api/breeds/image/random')
        if response.status_code==200:
            data=response.json()
            dog_images.append(data['message'])
    return render(request, 'gallery/index.html', {'dog_images':dog_images})
def about(request):
    return render(request, 'gallery/about.html')

