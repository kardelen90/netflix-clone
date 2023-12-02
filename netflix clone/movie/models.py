from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(verbose_name='Kategori Adı',max_length=30)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_pic')
    video = models.FileField(upload_to='movie_video')
    description = models.TextField()
    slug = models.SlugField(unique=True,blank=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    # Admin panelindeki ismini değiştirmek için.
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmler'





