from django.db import models
from comment.models import CommentModel


# Create your models here.
class Article(CommentModel):
    user_id = models.BigIntegerField()
    content = models.TextField()
    num_vote = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
