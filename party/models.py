from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Party(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    submission_deadline = models.DateTimeField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Compo(models.Model):
    name = models.CharField(max_length=255)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'party']

    def __str__(self):
        return f"{self.party} - {self.name}"


class Submission(models.Model):
    name = models.CharField(max_length=255)
    sub_file = models.FileField(upload_to="uploads/")
    thumbnail = models.FileField(upload_to="uploads/")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    compo = models.ForeignKey(Compo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_num = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order_num} - {self.author} - {self.name} - {self.compo}"