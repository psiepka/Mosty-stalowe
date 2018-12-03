from django.shortcuts import render


def error_404(request, exception):
    data = {'title':'404 Page dont found'}
    return render(request, 'home/error_404.html', data)

def error_500(request):
    data = {'title':'500 unexpected error'}
    return render(request, 'home/error_500.html', data)

def home(request):
    return render(request, 'home/home.html', {'title':'Strona główna'})
