from django.db import models

class Geography(models.Model):
    html = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='geography/%Y/%m/%d', default=None)

    class Meta:
        verbose_name = 'Geography'
        verbose_name_plural = 'Geography'


class Demand(models.Model):
    html = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='demand/', default=None)

    class Meta:
        verbose_name = 'Demand'
        verbose_name_plural = 'Demand'


class Skills(models.Model):
    html = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='skills/%Y/%m/%d', default=None)

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'

