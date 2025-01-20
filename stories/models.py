from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now


STATUS = (
    (0, "Draft"),
    (1, "Published"),
)


class Story(models.Model):
    """
    Represents a story with a title, location, content, author, and status.
    Includes functionality for generating unique slugs,
    retrieving absolute URLs,
    and tracking creation and update timestamps.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="stories")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Custom save method to generate a unique slug
        based on the title if not provided.
        """
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Story.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the absolute URL for the story detail page.
        """
        return reverse('story_detail', kwargs={'slug': self.slug})

    def __str__(self):
        """
        Returns the string representation of the story (its title).
        """
        return self.title
