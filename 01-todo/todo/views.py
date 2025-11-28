from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Todo


class TodoListView(ListView):
	model = Todo
	template_name = "todo/todo_list.html"
	context_object_name = "todos"
	paginate_by = 10

	def get_queryset(self):
		qs = super().get_queryset()
		return qs.order_by("-created_at")


class TodoCreateView(CreateView):
	model = Todo
	fields = ["title", "description", "due_date", "resolved"]
	template_name = "todo/todo_form.html"
	success_url = reverse_lazy("todo:todo_list")


class TodoUpdateView(UpdateView):
	model = Todo
	fields = ["title", "description", "due_date", "resolved"]
	template_name = "todo/todo_form.html"
	success_url = reverse_lazy("todo:todo_list")


class TodoDeleteView(DeleteView):
	model = Todo
	template_name = "todo/todo_confirm_delete.html"
	success_url = reverse_lazy("todo:todo_list")


def mark_resolved(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	todo.resolved = True
	todo.save()
	return redirect("todo:todo_list")
