from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length=400)
    likes = GenericRelation("Like")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=130)
    likes = GenericRelation("Like")

    def __str__(self) -> str:
        return f"{(self.post.id)}-comment#{self.id}"

class Like(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, default=None, null=True)
    object_id = models.PositiveIntegerField(default=None, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    created_at = models.DateTimeField(default=timezone.now)
