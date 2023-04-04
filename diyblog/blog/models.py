from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField('Post date', null=True, blank=True)
    author = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField('Description', max_length=1000)

    def __str__(self) :
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self) :
        """
        Returns the url to access a particular book instance.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    """
        Model representing an blogger.
        """
    name = models.CharField(max_length=100)
    bio = models.TextField('Bio', max_length=1000)

    def get_absolute_url(self) :
        """
        Returns the url to access a particular author instance.
        """
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self) :
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)

    class Meta :
        ordering = ['name']


class Comment(models.Model):
    description = models.TextField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)

