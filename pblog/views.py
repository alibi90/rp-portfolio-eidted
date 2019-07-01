from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from pblog.models import Post, Comment, Category
from pblog.forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'pblog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_on')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'pblog/detail.html'
    context_object_name = 'post'

    def formfill(request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)

        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post,
                )
                comment.save()

        context = {
            "post": post,
            "comments": comments,
            "form": form
        }

        return render(request, "pblog/detail.html", context)



class CategoryView(generic.ListView):
    template_name = 'pblog/category.html'
    context_object_name = 'posts'
    model = Category

    def get_queryset(self):
        return Post.objects.filter(
        categories__name__contains='category'
    ).order_by(
        '-created_on'
    )
