from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class CustomerUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        through='booking.CustomerUserGroup',
        verbose_name=_('groups'),
        blank=True,
        related_name='accounts_customeruser_set'  # Add related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        through='booking.CustomerUserPermission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='accounts_customeruser_set'  # Add related_name
    )


class CustomerUserGroup(models.Model):
    customer_user = models.ForeignKey(
        'accounts.CustomerUser',
        on_delete=models.CASCADE,
        related_name='accounts_customergroup_set'  # Add related_name
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='accounts_customergroup_set'  # Add related_name
    )


class CustomerUserPermission(models.Model):
    customer_user = models.ForeignKey(
        'accounts.CustomerUser',
        on_delete=models.CASCADE,
        related_name='accounts_customerpermission_set'  # Add related_name
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name='accounts_customerpermission_set'  # Add related_name
    )
