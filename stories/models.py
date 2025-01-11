from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

class Story(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title