from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import ImageSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        validators=[
            ImageSizeValidator(5)
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ]
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
        null=True,
    )
    date_of_publication = models.DateField(
        auto_now=True
    )
