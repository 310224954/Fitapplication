from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from datetime import datetime

from .forms import ArticleForm
from .models import Post
from Food.models import Products

# post.author
# post.tittle
# post.post_intro
# post.post_body
# post.post_summary
# post.image
# post.product_name
# post.creation_date


class PostListView(ListView):
    model = Post
    template_name = "Articles/article_list.html"#classes looking for app_name/model_view_type.html for example Articles_PostListView.html
    context_object_name = "posts" #by random it's objects_list    
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name="Articles/article_desc.html"

#CreateView
class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    template_name="Articles/article_add.html"
    form_class = ArticleForm
    success_url = reverse_lazy("art_list")

    #redirect_field_name = '/user/login/' Dont change that it works different !
    def form_valid(self, form):   
        tag_list = Products.objects.filter(pk__in=form.cleaned_data["tags"])  #tags = form.cleaned_data["tags"].values() 
        new_post = Post(tittle = form.cleaned_data["tittle"], 
            post_intro = form.cleaned_data["post_intro"],
            post_body = form.cleaned_data["post_body"], 
            post_summary = form.cleaned_data["post_summary"],             
            author=self.request.user,
            creation_date=datetime.today(),
            )
        new_post.save()         
        for tag in tag_list:
            new_post.tag.add(tag)
        return redirect(reverse_lazy("art_list"))

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name="Articles/article_update.html"
    fields = ["tittle", "post_intro", "post_body", "post_summary", "product_name"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object() 
        author = self.request.user
        if author == post.author or "admin" in str(author).lower():         
            return True
        else:
            False 



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name="Articles/article_delete.html"
    success_url = reverse_lazy("art_list")

    def test_func(self):#name of function is always the same ! 
        post = self.get_object() #getting the current updating post by pk
        author = self.request.user
        if author == post.author or "admin" in str(author).lower():         
            return True
        else:
            False #result 403 forbidden try to redirect it back to post description! 




#Old ones
# def post_list(request):
#   post = Post.objects.order_by("creation_date")   
#   context = {"posts":post}
#   return render(request, "Articles/article_list.html", context)

# def post_view(request, pk):
#   post = get_object_or_404(Post, pk=pk)   
#   context = {"post":post}
#   return render(request, "Articles/article_desc.html", context)


# @login_required
# def post_add(request):
#   pass


# @login_required
# def post_update(request, pk):
#   post = get_object_or_404(Post, pk=pk)   
#   context = {"post":post}
#   return render(request, "Articles/article_update.html", context)





# def get_object_or_404(request):
#    try:
#        obj = MyModel.objects.get(pk=1)
#    except MyModel.DoesNotExist:
#        raise Http404("No MyModel matches the given query.")
