from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=100)
    docs_link = models.URLField()

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    STATUS_CHOICES = (
        ('D', 'Designing'),
        ('A', 'Active'),
        ('C', 'Complete'),
    )
    project_url = models.CharField(primary_key=True, max_length=20)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    trello_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    packages = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.project_name
