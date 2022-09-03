from django.db import models

class Account (models.Model):
    name = models.CharField(max_length = 100)
    regno = models.CharField(max_length = 10)
    password = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f"{self.name}"