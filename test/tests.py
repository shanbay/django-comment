from __future__ import absolute_import
from django.test import TestCase
from django.contrib.auth.models import User
from comment.models import Comment
from test.models import Article


class CommentTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('test1', 'test1@test.com',
                                              '111111')
        self.user2 = User.objects.create_user('test2', 'test2@test.com',
                                              '111111')
        self.user3 = User.objects.create_user('test3', 'test3@test.com',
                                              '111111')

        self.article = Article.objects.create(user_id=0, content='Eso es un test')
        self.article2 = Article.objects.create(user_id=0, content='Eso es otro test')
        self.article.comments.create(user_id=self.user1.id,
                                     content="Aqui es un comentario")
        self.article2.comments.create(user_id=self.user2.id,
                                      content="Aqui es otro comentario")
        self.article.comments.create(user_id=self.user3.id,
                                     content="Aqui es el ultimo comentario")

    def tearDown(self):
        Article.objects.all().delete()
        Comment.objects.all().delete()
        User.objects.all().delete()

    def test_add_comment(self):
        content = 'Yeh ek comment hai'
        self.article.comments.create(user_id=self.user1.id, content=content)
        self.assertEqual(self.article.comments.count(), 3)
        self.assertEqual(self.article.comments.order_by('-id').first().content, content)

    def test_get_comments(self):
        return self.article2.comments.exists()

    def test_create_certain_comments(self):
        Article.comment_objects.create(user_id=self.user1.id,
                                       content="Aqui es un comentario especial",
                                       object_id=self.article.id)
        self.assertEqual(self.article.comments.count(), 3)

    def test_get_certain_comments(self):
        self.assertEqual(Article.comment_objects.last().content,
                         'Aqui es el ultimo comentario')

    def test_delete_comment(self):
        count = self.article.comments.count()
        self.article.comments.get(pk=1).delete()
        self.assertEqual(self.article.comments.count(), count-1)

    def test_user_comments(self):
        Comment.objects.filter(user_id=self.user1.id)
