from django.shortcuts import render,redirect
from .models import Movies
from .forms import MovieForm
# Create your views here.
def homeview(request):
    movies = Movies.objects.all()
    if request.method == 'POST':
        movie = request.POST.get('Mov')
        direc = request.POST.get('Dir')
        image = request.FILES['Img']
        des = request.POST.get('Des')
        obj = Movies(name=movie, director=direc,image=image,desc=des)
        obj.save()
    return render(request,'home.html',{'movies':movies})

def details(request,m_id):
    obj = Movies.objects.get(id=m_id)

    context = {
        'obj':obj,
    }
    return render(request, 'details.html',context)

def update(request,mv_id):
    mv = Movies.objects.get(id=mv_id)
    upd = MovieForm(request.POST or None, request.FILES,instance=mv)

    if upd.is_valid():
        upd.save()
        return redirect('/')
    else:
        return render(request, 'update.html',{'form':upd})

def delete(request,d_id):
    if request.method == 'POST':
        obj = Movies.objects.get(id=d_id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')