from django.db import models
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.name} {self.price}"


