from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Caregory,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title