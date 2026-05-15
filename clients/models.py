from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Meta:
    ordering = ['name']
