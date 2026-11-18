from django.db import models


class JobExam(models.Model):

    category = models.ForeignKey(
        'categories.JobCategory',
        on_delete=models.PROTECT,
        related_name='job_exams'
    )

    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.PROTECT,
        related_name='job_exams'
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    eligibility = models.TextField(blank=True)

    exam_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title