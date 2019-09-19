from django.db import models
from datetime import datetime
import timeago
# Create your models here.


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not len(postData['name']) > 5:
            errors['name'] = 'Name of the course must be at least 5 characters'
        if len(postData['description']) <= 15:
            errors['description'] = "description must be 15 characters or longer"
        return errors


class CommentManager(models.Manager):
    def time_converter(self, timestamp):
        pass


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    # .description
    # .comments


class Description(models.Model):
    description = models.TextField()
    course = models.ForeignKey(Course, related_name='description')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()


class Comment(models.Model):
    author = models.CharField(max_length=455)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name='comments')
