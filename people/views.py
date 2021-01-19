from django.shortcuts import render,redirect
from .models import contactPerson
# Create your views here.


def home(request):
    contactP=contactPerson.objects.all()
    context={"contactP": contactP}
    return render(request, 'index.html', context)

def newcontact(request):
    if request.method=='POST':
        try:
            print(request.POST["savecontact"])
            contactPerson.objects.create(name=request.POST["n"],
                                         relationship=request.POST["r"],
                                         number=request.POST["num"],
                                         notes=request.POST["not"],)
            contactPerson.save()
        except:
            return redirect('/')
    return render(request, 'newcontact.html')

def viewcontact(request, pk):
    obj=contactPerson.objects.get(id=pk)
    context={"obj": obj}
    return render(request, 'viewcontact.html', context)

def delete(request, pk):
    obj=contactPerson.objects.get(id=pk)
    obj.delete()
    return redirect('/')