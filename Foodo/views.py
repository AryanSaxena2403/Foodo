from django.shortcuts import render,redirect

def home(request):
    print('Hello')
    return render(request,'index.html')
def menu(request):
    return render(request,'menu.html')
def orders(request):
    return render(request,'orders.html')
