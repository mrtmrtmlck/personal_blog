from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.sitemaps import ping_google
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Label(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    summary = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails')
    label = models.ManyToManyField(Label)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    class Meta:
        ordering = ['-modified_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        ping_google()

    def display_label(self):
        return ', '.join(label.name for label in self.label.all())

    display_label.short_description = 'Label'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('article-detail', args=[self.slug])

    def __str__(self):
        return self.title
