from django.shortcuts import render

# Create your views here.

def wyklad_1(request):
     return render(request, 'articles/wyklad1.html', {'title':'Wyklad 1'})


def wyklad_2(request):
    return render(request, 'articles/wyklad2.html', {'title':'Wyklad 2'})


def wyklad_3(request):
    return render(request, 'articles/wyklad3.html', {'title':'Wyklad 3'})


def wyklad_4(request):
    return render(request, 'articles/wyklad4.html', {'title':'Wyklad 4'})


def wyklad_5(request):
    return render(request, 'articles/wyklad5.html', {'title':'Wyklad 5'})


def wyklad_6(request):
    return render(request, 'articles/wyklad6.html', {'title':'Wyklad 6'})


def wyklad_7(request):
    return render(request, 'articles/wyklad7.html', {'title':'Wyklad 7'})


def wyklad_8(request):
    return render(request, 'articles/wyklad8.html', {'title':'Wyklad 8'})


def wyklad_9(request):
    return render(request, 'articles/wyklad9.html', {'title':'Wyklad 9'})