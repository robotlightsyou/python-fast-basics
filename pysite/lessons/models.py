from django.db import models
from django.urls import reverse
from django.utils import timezone

class Lesson(models.Model):
    name = models.CharField(max_length=256)
    id = models.AutoField(primary_key=True)
    custom_key = models.CharField(max_length=24, default=id)
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)

    class Meta():
        ordering = ["custom_key"]

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("lesson", kwargs={"slug":self.slug})

class Lesson_Content(models.Model):
    body = models.TextField()
    item_num = models.IntegerField(unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.lesson.name} {self.item_num}")

    

