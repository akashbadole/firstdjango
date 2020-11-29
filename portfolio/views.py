from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     "va1" : "akash first program"
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("contact page")