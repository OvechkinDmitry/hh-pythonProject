from django.db import models

class Geography(models.Model):
    table_one = models.TextField(blank=False, default='')
    table_two = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='geography/%Y/%m/%d', default=None)

    class Meta:
        verbose_name = 'Geography'
        verbose_name_plural = 'Geography'

    def __str__(self):
        return "Георгафия"


class Demand(models.Model):
    html = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='demand/', default=None)

    class Meta:
        verbose_name = 'Demand'
        verbose_name_plural = 'Demand'

    def __str__(self):
        return "Востребованность"


class Skills(models.Model):
    year = models.CharField(blank=False, default='', max_length=4)
    table = models.TextField(blank=False, default='')
    graph_image = models.ImageField(upload_to='skills/%Y/%m/%d', default=None)

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'
        ordering = ['-year']

    def __str__(self):
        return self.year

class IntroCards(models.Model):
    title = models.CharField(blank=False, default='', max_length=225)
    content = models.TextField(blank=False, default='')
    number = models.CharField(blank=False, default='', max_length=5)

    class Meta:
        verbose_name = 'IntroCards'
        verbose_name_plural = 'IntroCards'


    def __str__(self):
        return self.title