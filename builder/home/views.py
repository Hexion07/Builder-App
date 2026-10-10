from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
    'variable1' : "Hello,",
    'variable2' : "Harry"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")