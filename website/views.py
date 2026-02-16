from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'website/home.html')


def book_table(request):

    return render(request, 'website/book_table.html')
