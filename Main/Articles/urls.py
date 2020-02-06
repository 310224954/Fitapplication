from django.urls import path


from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
	)

urlpatterns = [
	path("",PostListView.as_view(), name="art_list"),
	path("art_add/",PostCreateView.as_view(), name="art_add"),
	path("art_desc/<int:pk>/",PostDetailView.as_view(), name="art_detail"),	
	path("art_desc/<int:pk>/update/",PostUpdateView.as_view(), name="art_update"),
	path("art_desc/<int:pk>/delete/",PostDeleteView.as_view(), name="art_delete"),
]