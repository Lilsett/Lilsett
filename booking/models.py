from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_poster')
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=255)


class Theatre(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Seats(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.seat_number


class CustomerUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='booking_customeruser_set'  # Add related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='booking_customeruser_set'  # Add related_name
    )


class CustomerUserGroup(models.Model):
    customer_user = models.ForeignKey(
        'accounts.CustomerUser',
        on_delete=models.CASCADE,
        related_name='booking_customergroup_set'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='booking_customergroup_set'
    )


class CustomerUserPermission(models.Model):
    customer_user = models.ForeignKey(
        'accounts.CustomerUser',
        on_delete=models.CASCADE,
        related_name='booking_customerpermission_set'
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name='booking_customerpermission_set'
    )
