from django.db import models
from django.urls import reverse
from django.utils import timezone
from martor.models import MartorField


class Chapter(models.Model):
    name = models.CharField(max_length=30)
    custom_key = models.IntegerField(null=False, unique=True)
    id = models.AutoField(primary_key=True, unique=True)

    class Meta():
        ordering = ['custom_key']

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=256)
    id = models.AutoField(primary_key=True)
    custom_int = models.IntegerField(null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name="Last updated", auto_now=True)
    slug = models.SlugField(null=False, unique=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)

    class Meta():
        ordering = ["custom_int"]
        unique_together = ("custom_int", "chapter")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lesson", kwargs={"slug": self.slug})


class Lesson_Content(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    body = MartorField(blank=True, null=True)
    item_num = models.IntegerField(unique=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta():
        ordering = ["item_num"]
        unique_together = ("item_num", "lesson")
        verbose_name_plural = "Lesson Contents"

    def __str__(self):
        return str(f"{self.lesson}: {self.name} {self.item_num}")


    