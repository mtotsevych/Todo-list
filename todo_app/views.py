from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "tags",)
    success_url = reverse_lazy("task_app:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags",)
    success_url = reverse_lazy("task_app:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_app:task_list")


def complete_and_incomplete_task(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    task = Task.objects.get(pk=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("task_app:task_list"))


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("task_app:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("task_app:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_app:tag_list")
