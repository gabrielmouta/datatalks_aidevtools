from django.contrib import admin
from .models import Todo, Tag


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	list_display = ("title", "owner", "resolved", "due_date", "created_at")
	list_filter = ("resolved", "due_date")
	search_fields = ("title", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	search_fields = ("name",)
