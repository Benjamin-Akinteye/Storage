from django.views import generic
from .models import Post

class PostList(generic.ListView):
	model = Post

class PostCreateView(generic.CreateView):
	model = Post
	fields = “__all__”
	success_url  = reverse_lazy(“blog:all”)

class PostDetail(generic.DetailView):
    model = Post

 class PostUpdateView(generic.PostUpdateView):
    model = Post
    fields = “__all__”
	success_url  = reverse_lazy(“blog:all”)

class PostDeleteView(generic.PostDeleteView):
    model = Post
    fields = “__all__”
	success_url  = reverse_lazy(“blog:all”)

