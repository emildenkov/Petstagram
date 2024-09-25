from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageSizeValidator:

    def __init__(self, image_size, message=None):
        self.image_size = image_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.__message = f'The image should be below or equal to {self.image_size}MB'
        else:
            self.__message = value

    def __call__(self, value):
        if value.size > self.image_size * 1024 * 1024:
            raise ValidationError(self.message)
