from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


#TODO  Topics for menu bar
# Education; Religion; Jobs/Careers; Health; Technology; Government #

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    date = models.DateField()
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default='DR',
    )

    class Meta:
        ordering = ('-publish',)
        indexes = [models.Index(fields=['-publish'])]
        db_table = 'blog_post'

    def __str__(self):
        return self.title
