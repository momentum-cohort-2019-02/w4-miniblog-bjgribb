from django.shortcuts import render
from django.views import generic
from blog.models import BlogPost, Blogger, Topic, BlogPostDetail

# Create your views here.

def index(request):
    """View fucntion for home page of site."""

    # Generate counts of some of the main objects.
    num_blogposts = BlogPost.objects.all().count()
    num_bloggers = Blogger.objects.count()

    context = {
        'num_blogposts': num_blogposts,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context) 

class BlogPostListView(generic.ListView):
    model = BlogPost
    # paginate_by = 3


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
