## Django Comment

``django-comment`` is a simple Django app to add comments for your django model.

This project is inspired by [django-taggit](https://github.com/alex/django-taggit) and directly derived from [django-vote](https://github.com/shanbay/django-vote)

[![Build Status](https://travis-ci.org/shanbay/django-comment.svg)](https://travis-ci.org/shanbay/django-comment)
[![Codecov](https://codecov.io/gh/shanbay/django-comment/coverage.svg?branch=master)](https://codecov.io/gh/shanbay/django-comment?branch=master)
[![PyPI version](https://badge.fury.io/py/django-comment.svg)](https://badge.fury.io/py/django-comment)

### Quick start


#### Add `'comment'` to your `INSTALLED_APPS` setting like this

```python
INSTALLED_APPS = (
  ...
  'comment',
)
```

#### Add `CommentModel` to the model you want to comment

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

# Use comment_objects like a native manager
Review.comment_objects.filter(user_id=user_id).limit(10)

# Override auto_time and auto_time_add in model fields
from comment.utils import override_autotime
with override_autotime():
    com = review.comments.create(user_id, content, created_at=your_timestamp)
print(com.created_at) # your timestamp

```
