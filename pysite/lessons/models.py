from django.db import models
from django.urls import reverse
from django.utils import timezone

class Lesson(models.Model):
    name = models.CharField(max_length=256)
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, unique=True)
    # bodies = Lesson_Content.objects.filter(lesson__name=self.name)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        # return reverse("lesson", kwargs={"pk":self.pk})
        return reverse("lesson", kwargs={"slug":self.slug})

class Lesson_Content(models.Model):
    body = models.TextField()
    item_num = models.IntegerField(unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.lesson.name} {self.item_num}")

    

