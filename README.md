# Boards Application

This is a simple discussion boards application built with Django. Users can create boards, topics within boards, and posts within topics. The application enforces specific relationships between boards, topics, posts, and users.

## Project Structure

```
myproject/
 |-- myproject/
 |    |-- boards/                <-- our new Django app!
 |    |    |-- migrations/
 |    |    |    +-- __init__.py
 |    |    |-- __init__.py
 |    |    |-- admin.py
 |    |    |-- apps.py
 |    |    |-- models.py
 |    |    |-- tests.py
 |    |    +-- views.py
 |    |-- myproject/
 |    |    |-- __init__.py
 |    |    |-- settings.py
 |    |    |-- urls.py
 |    |    |-- wsgi.py
 |    +-- manage.py
 +-- venv/
```

## Class Diagram

![Class Diagram](class Diagram.png)

## Models

### Board

```python
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
```

### Topic

```python
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
```

### Post

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
```

## Model Relationships

### Topic and Board Association

A Topic must be associated with exactly one Board (which means it cannot be null), and a Board may be associated with many Topics or none (0..*). This means a Board may exist without a single Topic.

### Topic and Post Association

A Topic should have at least one Post (the starter Post), and it may also have many Posts (1..*). A Post must be associated with one, and only one Topic (1).

### Topic and User Association

A Topic must have one, and only one User associated with it: the topic starter User (1). A User may have many or none Topics (0..*).

### Post and User Association

A Post must have one, and only one User associated with it: created by (1). A User may have many or none Posts (0..*). The second association between Post and User is a direct association, meaning we are interested only in one side of the relationship which is what User has edited a given Post. The multiplicity says 0..1, meaning the updated by field may be null (the Post wasn’t edited) and at most may be associated with only one User.

## Wireframes

### Homepage

The homepage lists all available boards.

![Boards Project Wireframe Homepage](https://via.placeholder.com/300)

### Topics

When a user clicks on a board, it should list all the topics.

![Boards Project Wireframe Topics](https://via.placeholder.com/300)

### New Topic

The "new topic" screen.

![New Topic Screen](https://via.placeholder.com/300)

### Posts

The topic screen displaying the posts and discussions.

![Topic Posts Listing Screen](https://via.placeholder.com/300)

### Reply

The reply topic screen with a summary of the posts in reverse order (newest first).

![Reply Topic Screen](https://via.placeholder.com/300)

To draw your wireframes, you can use the draw.io service, which is free.

## Conclusion
