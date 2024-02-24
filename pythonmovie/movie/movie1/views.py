from django.shortcuts import render
from django.db.models import Q
# Create your views here.




# Create your views here.
def card(request):
    return render(request,'card.html')
def addmovie(request):
    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        b = Movie.objects.create(title=t, author=a, price=p,)
        b.save()
        return viewmovie(request)
    return render(request, 'add movie.html')
