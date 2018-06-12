from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=100)
	logo = models.CharField(max_length=200)
	title=models.CharField(max_length=100)
	genre=models.CharField(max_length=50)

	def __str__(self):
		return self.artist + ' - ' +self.genre

class Song(models.Model):
	album = models.ForeignKey(Album ,on_delete = models.CASCADE)
	file_type=models.CharField(max_length=100)
	title=models.CharField(max_length=100)

	def __str__(self):
		return self.title