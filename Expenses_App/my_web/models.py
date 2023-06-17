from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from Expenses_App.my_web.validators import validate_only_letters, validate_image_size


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MIN_LEN_MSG_ERROR = 'First name must be at least 2 chars!'

    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MIN_LEN_MSG_ERROR = 'First name must be at least 2 chars!'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN, FIRST_NAME_MIN_LEN_MSG_ERROR),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN, LAST_NAME_MIN_LEN_MSG_ERROR),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=0,
    )

    profile_image = models.ImageField(
        validators=(
            validate_image_size,
        ),
        blank=True,
        null=True,
    )

    def clean(self):
        if self.budget < 0:
            raise ValidationError("The budget should not be below 0!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
