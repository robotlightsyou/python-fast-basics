from django.db import models
from django.urls import reverse
from django.utils import timezone

class Lesson(models.Model):
    name = models.CharField(max_length=256)
    id = models.AutoField(primary_key=True)
    custom_key = models.CharField(max_length=24, default=id)
    pub_date = models.DateTimeField(verbose_name="Last updated", auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta():
        ordering = ["custom_key"]

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("lesson", kwargs={"slug":self.slug})

class Lesson_Content(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    item_num = models.IntegerField(unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta():
        ordering = ["item_num"]

    def __str__(self):
        return str(f"{self.lesson}: {self.name} {self.item_num}")