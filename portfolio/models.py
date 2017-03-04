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
    picture = models.ImageField(upload_to= './static/img/')
    url = models.URLField()
    start_date = models.DateField()
    github_link = models.URLField()
    trello_link = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    packages = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.project_name
