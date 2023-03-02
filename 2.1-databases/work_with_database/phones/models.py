from django.db import models
from django.urls import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    image = models.URLField()
    price = models.DecimalField(max_digits=19, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone_detail', args=[str(self.name)])
