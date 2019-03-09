from django.db import models
from django.urls import reverse

# Create your models here.

class Topic(models.Model):
    """Model representing a blog post topic."""
    name = models.CharField(max_length=50, help_text='Please enter the topic of the blog. (i.e. Science, Business, Travel)')

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    """Model representing a blog-post."""

    """Name or title of the post."""
    post = models.CharField(max_length=200, help_text='Enter the blog post title here.')

    # Foreign Key used because a post will only have one blogger but a blogger could have multiple blogs.
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    # This represents the actual content of the blogpost.
    content = models.TextField(max_length=2000, help_text='Write your post here.')

    # This represents the written date (posted date)
    post_date = models.DateField()

    # This allows the selection of a blogpost topic.
    topic = models.ManyToManyField(Topic, help_text='Select the topic for this post.')

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("(blogpost-detail)", args=[str(self.id)])
    

class Blogger(models.Model):
    """Model representing the author of the blogpost."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=1200, help_text='Enter a little something about yourself.')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author."""
        return reverse("blogger-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    


