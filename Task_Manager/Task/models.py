from django.db import models


# Create your models here.

class Task(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Creation_date = models.DateField()
    End_date = models.DateField()
    priority_list = [
        ("sm", "Малый"),
        ("md", "Средний"),
        ("hg", "Высокий")
    ]
    Priority = models.CharField(max_length=50, choices=priority_list)
    status = [
        ("true", "Сделано"),
        ("false", "Не Сделано")
    ]
    Status = models.CharField(max_length=50, choices=status)
