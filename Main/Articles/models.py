from django.db import models
from datetime import date
from django.urls import reverse
from datetime import date
from multiselectfield import MultiSelectField

from Food.models import Products
from django.contrib.auth.models import User



class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.PROTECT)# remember to set user to inactive instead of deleting them ! 
	tittle = models.CharField(max_length = 50)
	post_intro = models.TextField(blank=True)
	post_body = models.TextField(blank=True)
	post_summary = models.TextField(blank=True)
	image = models.ImageField(default='default_for_articles.jpg', upload_to='article_pictures')
	creation_date = models.TimeField(blank=True, null=True)
	tag = models.ManyToManyField(Products)
	# tags = MultiSelectField(
	# 	('1', 'Test_1'),
 #        ('2', 'Test_2'),
 #    )	

	def __str__(self):
		return self.tittle

	def publish_post(self):
		self.creation_date = date.today
		self.safe


	@property	
	def short_description(self):
		post_intro = self.post_intro
		short_description = ""
		for i,element in enumerate(post_intro):
			if(i > 50 and element==" " or i ==70):
				break
			short_description += element
		return short_description


	def get_absolute_url(self):
		#return the whole URL to a specific post 
		#function connected with view to redirect to the exact url of newly created object(post) 
		return reverse("art_detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ["-creation_date"] # to reverse ordering just add - before 