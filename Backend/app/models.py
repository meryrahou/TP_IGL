# yourappname/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Keyword(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author)
    institutions = models.ManyToManyField(Institution)
    keywords = models.ManyToManyField(Keyword)
    references = models.ManyToManyField(Reference)
    full_text = models.TextField()
    pdf_url = models.URLField()

    def __str__(self):
        return self.title
    

class CustomUser(AbstractUser):
        
    USER_TYPE_CHOICES = [
    ('user', 'User'),
    ('administrator', 'Administrator'),
    ('moderator', 'Moderator'),
    ]

    user_type = models.CharField(
        max_length=15,
        choices=USER_TYPE_CHOICES,
        default='user',
    )

    # Add related_name to resolve the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )