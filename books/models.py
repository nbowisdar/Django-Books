from django.db import models

LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('FR', 'French'),
    ('DE', 'German'),
    ('ZH', 'Chinese'),
    ('JA', 'Japanese'),
]

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    cover = models.URLField(null=True, blank=True)
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='EN',
    )

    def __str__(self):
        return self.title
