from django.http import HttpResponse 
def aboutUs(request):
    return HttpResponse("This is About Us Page");
def dynamicUrl(rqeuest,id):
   return HttpResponse(f"This is dynamic URL Number is {id}")