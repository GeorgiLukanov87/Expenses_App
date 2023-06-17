from django.core import validators
from django.db import models

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


def validate_budget(value):
    if value < 0:
        raise ValidationError('Budget cannot be below 0!')


def validate_file_size_5mb(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MIN_LEN_MSG_ERROR = 'First name must be at least 2 chars!'

    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MIN_LEN_MSG_ERROR = 'First name must be at least 2 chars!'

    profile_image = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size_5mb,
        ),
        blank=False,
        null=False,
    )

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
        validators=(validate_budget,),
    )



class Expense(models.Model):
    EXPENSE_MAX_LEN = 30

    title = models.CharField(
        max_length=EXPENSE_MAX_LEN,
    )

    expense_image = models.URLField()
    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField()
