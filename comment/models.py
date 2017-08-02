from django.db import models
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType

from vote.models import VoteModel


class CommentManager(models.Manager):

    def filter(self, *args, **kwargs):
        if 'content_object' in kwargs:
            content_object = kwargs.pop('content_object')
            content_type = ContentType.objects.get_for_model(content_object)
            kwargs.update({
                'content_type': content_type,
                'object_id': content_object.pk
            })

        return super(CommentManager, self).filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        if 'content_object' in kwargs:
            content_object = kwargs.pop('content_object')
            content_type = ContentType.objects.get_for_model(content_object)
            kwargs.update({
                'content_type': content_type,
                'object_id': content_object.pk
            })

        return super(CommentManager, self).get(*args, **kwargs)


class Comment(VoteModel):
    user_id = models.BigIntegerField()
    content = models.TextField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    objects = CommentManager()

    class Meta:
        index_together = ('content_type', 'object_id')

    def reply(self, user_id, content):
        pass


class CommentModel(models.Model):
    comments = GenericRelation(Comment)
    total_number = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.total_number = self.comments.count()
        super(CommentModel, self).save(*args, **kwargs)
