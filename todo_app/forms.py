from django import forms

from todo_app.models import Task


class TaskCreationChangeForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        )
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags",)
