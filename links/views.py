from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse
from .models import Link
from .forms import LinkForm
from datetime import date 
# Create your views here.

def index(request):
    links = Link.objects.all()
    current_date = date.today()
    context = {
        "links" : links ,
        "current_date" : current_date
    }

    return render(request , 'links/index.html' , context)

# oursite.com/google -> www.google.com
# shortened url -> longer final destination
def root_link(request , link_slug):
    link = get_object_or_404(Link , slug=link_slug)
    link.click() # this will increment the clicked filed (on Models)

    return redirect (link.url) 

def add_link (request):
    if request.method == "POST":
        # form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            # save data and return to homepage
            form.save()
            return redirect(reverse("home"))
    else:
        form = LinkForm()
    
    context = {
        "form" : form
    }
    return render(request , 'links/create.html' , context)