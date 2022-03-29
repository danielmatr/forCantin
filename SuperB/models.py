from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.PositiveSmallIntegerField(help_text="<em>сом.</em>", blank=False)
    barcode = models.PositiveIntegerField(unique=True, blank=False)

    def __str__(self):
        return f'{self.name}'


class Students(models.Model):

    id_student = models.PositiveIntegerField(unique=True, blank=False)
    name = models.CharField(max_length=60, blank=False)
    surname = models.CharField(max_length=60, blank=False)
    cash = models.PositiveIntegerField(help_text="<em>сом.</em>")

    def __str__(self):
        return f'{self.id_student}'