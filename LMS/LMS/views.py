from django.shortcuts import redirect,render


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    return render(request,'Main/home.html')


def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')


def CONTACT_US(request):
    return render(request,'Main/contact_us.html')


def ABOUT_US(request):
    return render(request,'Main/about_us.html')