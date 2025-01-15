from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core import validators


@deconstructible
class EmailValidator(validators.RegexValidator):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    message = "email is not valid"


class User(AbstractUser):
    username_validator = EmailValidator()
    class Type(models.IntegerChoices):
        ADMIN = 1
        OPERATOR = 2
        NORMAL = 3

    type_id = models.IntegerField(
        null=False,
        choices=Type.choices,
        default=3
    )
    username = models.CharField(
        verbose_name="username",
        max_length=255,
        validators=[username_validator],
        unique=True,
        null=False,
        blank=False,
        help_text="Enter email.",
    )
    # Password is otp number
    password = models.CharField(
        'password',
        max_length=128,
        unique=False,
        null=False,
        blank=False,
        help_text='Enter otp number.',
    )
    password_updated_at = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
    )

    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except IntegrityError as err:
            raise ValidationError(err)
