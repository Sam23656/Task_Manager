from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return f"{self.Name}"

    def get_priority(self):
        priority = 0
        if self.Priority == "sm":
            priority += 1
        elif self.Priority == "md":
            priority += 2
        elif self.Priority == "hg":
            priority += 3
        date = self.End_date - self.Creation_date
        if date.days > 12:
            priority += 1
        elif date.days < 10:
            priority += 2
        elif date.days < 5:
            priority += 3
        elif date.days < 2:
            priority += 4
        return priority

    @classmethod
    def sorted_by_name(cls):
        lst_cls_false = []
        lst_cls_true = []
        for cl in cls.objects.all():
            if cl.Status == "false":
                lst_cls_false.append(cl)
            else:
                lst_cls_true.append(cl)
        return sorted(lst_cls_false, key=lambda obj: -obj.get_priority()) + sorted(lst_cls_true, key=lambda obj: -obj.get_priority())

    def get_absolute_url(self):
        return reverse("Task", args=self.pk)
