from django.db import models
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType

from vote.models import VoteModel


class CommentManager(models.Manager):
    def get_queryset(self):
        content_type = ContentType.objects.get_for_model(self.model)
        return Comment.objects.filter(content_type=content_type)

    def create(self, **kwargs):
        content_type = ContentType.objects.get_for_model(self.model)
        Comment.objects.create(content_type=content_type, **kwargs)

    def get_or_create(self, **kwargs):
        try:
            return self.get(**kwargs), False
        except Comment.DoesNotExist:
            return self.create(**kwargs), True


class Comment(VoteModel):
    user_id = models.BigIntegerField()
    content = models.TextField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    # objects = CommentManager()

    class Meta:
        index_together = ('content_type', 'object_id')

    def reply(self, user_id, content):
        pass


class CommentModel(models.Model):
    comments = GenericRelation(Comment)
    total_number = models.IntegerField(default=0)
    objects = models.Manager()
    comment_objects = CommentManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.total_number = self.comments.count()
        super(CommentModel, self).save(*args, **kwargs)
