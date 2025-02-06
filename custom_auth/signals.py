from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Activity, User

@receiver(post_save, sender=Group)
def log_group_creation(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=None,  # No specific user for group creation
            activity_type='GROUP_CREATION',
            description=f"Group '{instance.name}' was created.",
            metadata={'group_id': instance.id}
        )


@receiver(post_save, sender=User)
def log_user_creation_or_update(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(
            user=instance,
            activity_type='USER_CREATION',
            description=f"User '{instance.email}' was created."
        )
    else:
        Activity.objects.create(
            user=instance,
            activity_type='USER_UPDATE',
            description=f"User '{instance.email}' was updated."
        )