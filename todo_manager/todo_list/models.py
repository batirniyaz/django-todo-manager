from django.db import models


# Create your models here.
class ToDoItem(models.Model):

    class Meta:
        verbose_name = "ToDo Item"

    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
