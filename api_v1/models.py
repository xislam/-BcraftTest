from django.db import models


class Statistics(models.Model):
    date = models.DateField(verbose_name="date")
    views = models.IntegerField(verbose_name="number of impressions")
    clicks = models.IntegerField(verbose_name="number of faces")
    cost = models.IntegerField(verbose_name="cost")
    cpc = models.IntegerField(null=True, blank=True, verbose_name="cpc")
    cpm = models.IntegerField(null=True, blank=True, verbose_name="cpm")
    date_add = models.DateField(auto_now_add=True, verbose_name="date create")

    def __str__(self):
        return str(self.views)
