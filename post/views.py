from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView, )
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin, )
from .models import Post


# Post App - Home(Index) Page
def home(request):
    return render(request, "post/home.html", {"posts": Post.objects.all(),
                                              "title": "Home",
                                              })


# Post App - Home(Index) Page Class ( List View )
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/home.html"  # <app>/<model>_<view_type>.html
    context_object_name = "posts"
    ordering = "-created"
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/user_post.html"  # <app>/<model>_<view_type>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-created")


# Post App - Individual Post Detail Page Class ( Detail View )
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Post App - About Page
def about(request):
    return render(request, "post/about.html", {"title": "About.jax"})
