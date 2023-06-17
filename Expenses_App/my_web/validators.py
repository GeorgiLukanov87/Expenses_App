from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Ensure this value contains only letters.')


def validate_image_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError("Max file size is 5.00 MB")
