from django import forms
from django.forms import ModelForm
from multiselectfield import MultiSelectField

from .models import Post
from Food.models import Products

#forms.Form
#forms.ModelForm
class ArticleForm(forms.Form):
	tittle = forms.CharField(max_length = 50)
	
	post_intro = forms.CharField(max_length=350, min_length=100,
		widget=forms.Textarea(
			attrs={
				"placeholder":"Please give at first the introduction, about what article topic.",
				"class":"new-form",
				"rows":10,
				"cols":50
			}
		)
		)
	post_body =  forms.CharField(max_length=500, min_length=100, 
		widget=forms.Textarea(
			attrs={
				"placeholder":"Please enter the main part of the article.",
				"class":"new-form",
				"rows":20,
				"cols":50
			}
		)
		)
	post_summary =  forms.CharField(max_length=350, min_length=100, 
		widget=forms.Textarea(
			attrs={
				"placeholder":"Please sum up here your article.",
				"class":"new-form",
				"rows":10,
				"cols":50,
				"background-color":"#8585ad"
			}
		)
		)
	tags = forms.ModelMultipleChoiceField(#forms.CheckboxSelectMultiple,	#forms.RadioSelect
		Products.objects.all(),
		widget=forms.CheckboxSelectMultiple(
			attrs={}),
	)
	
	class Meta:
		fields = ["tittle", "post_intro", "post_body", "post_summary", "tag"]


