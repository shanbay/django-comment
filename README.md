## Django Comment

``django-comment`` is a simple Django app to add comments for your django model.

This project is inspired by [django-taggit](https://github.com/alex/django-taggit) and directly derived from [django]


### Quick start


#### Add `'vote'` to your `INSTALLED_APPS` setting like this

```python
INSTALLED_APPS = (
  ...
  'comment',
)
```

#### Add `VoteModel` to the model you want to vote

```python
from comment.models import CommentModel

class ArticleReview(CommentModel):
    ...
```

#### Run migrate

```shell
manage.py makemigrations
manage.py migrate
```


#### Use comment API

```python
review = ArticleReview.objects.get(pk=1)

# Add comment for an object
review.comments.create(user_id, content)

# Removes a comment from the object
review.comments.get(pk=comment_id).delete()

# Check if the user commented the object
review.comments.filter(user_id=user_id).exists()

# Returns the number of comments for the object
review.comments.count()

# Returns all comments by user
review.comments.filter(user_id=user_id)

```
