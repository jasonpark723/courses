from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Description, Comment
from datetime import datetime
import timeago
# Create your views here.


def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)


def new(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        print(description)
        new_course = Course.objects.create(name=name)
        Description.objects.create(
            description=description, course=new_course)
        print(new_course.name)
        print(new_course.description)
    return redirect('/')


def show_destroy(request, id):
    course = Course.objects.get(id=id)
    return render(request, 'destroy.html', {'course': course})


def destroy(request, id):
    if request.method == "POST":
        Course.objects.get(id=id).delete()
        return redirect('/')


def show_comments(request, id):
    course = Course.objects.get(id=id)
    course_time = course.created_at.replace(tzinfo=None)
    today = datetime.now()
    time_delta = (timeago.format(course_time, today))
    tdelta = []
    comments = course.comments.all().values()
    for comment in course.comments.all():
        tdelta.append(timeago.format(
            comment.created_at.replace(tzinfo=None), today))
    comments_delta = list(zip(comments, tdelta))
    for comment in comments_delta:
        print(comment)
    context = {
        'comments': list(comments_delta),
        'course_id': id,
    }
    return render(request, 'comment.html', context)


def new_comment(request):
    if request.method == "POST":
        author = request.POST['author']
        comment = request.POST['comment']
        course_id = int(request.POST['course_id'])
        print(course_id)
        course = Course.objects.get(id=course_id)
        Comment.objects.create(author=author, comment=comment, course=course)
        return redirect('/comment/'+str(course_id))


def delete_comment(request, id):
    if request.method == "POST":
        course_id = request.POST['course_id']
        comment = Comment.objects.get(id=id)
        comment.delete()
        return redirect('/comment/'+str(course_id))
