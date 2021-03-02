from django.shortcuts import render,redirect
from Content.models import Ideas,Photo,ICategory
from django.forms import formset_factory
from .forms import IdeasForm,PhotoToIdeas,RatingForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .permissions import AuthorPermissionsMixin
from django.views import View


@login_required(login_url='login')
def home(request):
    user = request.user
    ideas = Ideas.objects.filter(author=user)
    return render(request, 'Content/dashboard.html',{'posts':ideas})

def addI(request):
    
    if request.method == "POST":
        photo = formset_factory(PhotoToIdeas, extra=2)
        photoset = photo(request.POST or None, request.FILES or None)
        form = IdeasForm(request.POST)
        if form.is_valid() and photoset.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            for f in photoset:
                try:
                    phoi = Photo(ideas=new_post,photo=f.cleaned_data['photo'])
                    phoi.save()
                except Exception as e:
                    raise

            return redirect('ideas:home')
        else:
            print("yt lefkjc,")
    else:
        form = IdeasForm()
        photo = formset_factory(PhotoToIdeas, extra=2)
    return render(request,'Content/addI.html',{'form':form,'formset':photo})

class IdeasUpdateView(AuthorPermissionsMixin, UpdateView):
    model = Ideas
    form_class = IdeasForm
    template_name = 'Content/update.html'
    success_url = reverse_lazy('ideas:home')


class DetailView(View):
    
    def get(self,request,id):
        idea = Ideas.objects.get(id=id)
        ratings = idea.rating.all()
        for rating in ratings:
            if rating.user.id == request.user.id:
                rat = rating
                check = True
            else:
                rat = "Nothing"
                check = False
        return render(request,"idea/detailView.html",{"idea":idea,"check":check,'rat':rat})

def listIdea(request,id):

        category = ICategory.objects.get(id=id)

        return render(request,"idea/listView.html",{"category":category})

def rateIdea(request,id):

    if request.method == "POST":

        form = RatingForm(request.POST)
        b = request.POST.get('idea')
        u = request.POST.get('user')
        
        if form.is_valid():
            idea = Ideas.objects.get(id=id)
            ratings = idea.rating.all()
            for rating in ratings:
                if rating.user.id == request.user.id:
                    rat = rating
                    check = True
                else:
                    rat = "Nothing"
                    check = False
            form.save()
            return redirect('home')