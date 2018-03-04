from django.shortcuts import render


def view_main(request):
    return render(request, 'base.html')
