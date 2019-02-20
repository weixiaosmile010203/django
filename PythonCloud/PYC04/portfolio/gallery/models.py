from django.db import models

# Create your models here.


class Gallery(models.Model):
	description = models.CharField(max_length=100)
	image = models.ImageField(default='default.png',upload_to='images/')
	title = models.CharField(default="作品名称", max_length=20)

	def __str__(self):
		return self.title