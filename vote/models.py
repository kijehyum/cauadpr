from django.db import models

# Create your models here.
class Ad_video(models.Model):
	name = models.CharField(max_length = 20)
	number = models.IntegerField(default = 0)
	result = models.IntegerField(default=0)
	video_url = models.CharField(max_length=500)


class Ad_outdoor(models.Model):
	name = models.CharField(max_length = 20)
	number = models.IntegerField(default = 0)
	result = models.IntegerField(default=0)
	# img_url = models.CharField(max_length=500)
	# image = models.ImageField(null=True, blank=True)


class Ad_ent(models.Model):
	name = models.CharField(max_length = 20)
	number = models.IntegerField(default = 0)
	result = models.IntegerField(default=0)
	# img_url = models.CharField(max_length=500)
