from django.db import models

from category.models import Category


class Vacancy(models.Model):
    STATUS_CHOICES = (
        ("open", "Открытая"),
        ("close", "Закрытая"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resume_collect = models.FileField(upload_to='resumes/',blank=True)
    city = models.CharField(max_length=255)
    motivation_desc = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    def __str__(self):
        return self.title
