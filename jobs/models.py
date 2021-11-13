from django.db import models
from django.core.exceptions import ValidationError


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Job(AbstractModel):
    # TODO: Add a field for the job's location
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    application_link = models.URLField()
    salary_range_min = models.IntegerField()
    salary_range_max = models.IntegerField()

    def clean(self):
        if self.salary_range_min > self.salary_range_max:
            raise ValidationError("Salary range is invalid")

    def __str__(self):
        return f"{self.pk} - {self.company} - {self.position}"


# TODO: Add domain for job posting
# -> This will make it easier to search for jobs in a specific domain
# -> This will make it easier for recommending jobs to the user
