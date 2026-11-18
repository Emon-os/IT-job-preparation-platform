from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=200, unique=True)

    organization_type = models.CharField(
        max_length=100,
        blank=True
    )

    website = models.URLField(blank=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name