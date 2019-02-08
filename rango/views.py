from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
# Create your views here.

# def index(request):
#     category_list = Category.objects.order_by('-likes')[:5]
#     context_dict = {'categories': category_list}
#     return render(request, 'rango/index.html', context_dict)