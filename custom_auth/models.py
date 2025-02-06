from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def is_beneficiary(self):
        return self.groups.filter(name='Beneficiaries').exists()

    def is_food_bank_staff(self):
        return self.groups.filter(name='Food Bank Staff').exists()

    def is_volunteer(self):
        return self.groups.filter(name='Volunteers').exists()

    def is_system_administrator(self):
        return self.groups.filter(name='System Administrators').exists()


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('ROLE_ASSIGNMENT', 'Role Assignment'),
        ('PROFILE_UPDATE', 'Profile Update'),
        ('INTERACTION', 'Interaction'),
        ('NOTE', 'Note'),
        ('GROUP_CREATION', 'Group Creation'),  # Add this for group creation
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities',
        null=True,  # Allow NULL for activities not tied to a specific user
        blank=True,  # Allows empty values in forms
    )
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=now)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.activity_type} - {self.user.email if self.user else 'System'} ({self.timestamp})"
    class Meta:
        verbose_name = "Activity"  # Singular name
        verbose_name_plural = "Activities"  # Plural name