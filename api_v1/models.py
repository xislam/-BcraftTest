from django.db import models


class Statistics(models.Model):
    date = models.DateField(verbose_name="date")
    views = models.IntegerField(verbose_name="number of impressions")
    clicks = models.IntegerField(verbose_name="number of faces")
    cost = models.DecimalField(decimal_places=2, verbose_name="cost")

    def __str__(self):
        return self.views
