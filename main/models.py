from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='static/images/')
    short_bio = models.TextField()
    description = models.TextField()
    instagram_link = models.URLField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
