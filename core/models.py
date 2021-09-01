from django.db import models


class Task(models.Model):

    class TaskTypes(models.TextChoices):
        DEVELOPMENT = ('Desenvolvimento'),
        SERVICE = ('Atendimento'),
        MAINTENANCE = ('Manutenção'),
        URGENT_MAINTENANCE = ('Manutenção Urgente'),

    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    type = models.CharField(
        max_length=50,
        choices=TaskTypes.choices
        )

    def __str__(self):
        return self.title
