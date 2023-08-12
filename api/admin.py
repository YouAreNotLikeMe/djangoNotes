from django.contrib import admin
from .models import User, Note


# Register your models here.


@admin.register(User)
class UserAdminPanel(admin.ModelAdmin):
    list_display = ['id', 'userName', 'userPass']
    list_editable = ['userName', 'userPass']
    ordering = ['id']


@admin.register(Note)
class NoteAdminPanel(admin.ModelAdmin):
    list_display = ['id', 'userIdConnect', 'noteTitle', 'textNote', 'noteColor']
    list_editable = ['userIdConnect', 'noteTitle', 'textNote']
