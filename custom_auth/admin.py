from django.contrib import admin
from django.utils.html import format_html
from django.template.defaultfilters import pluralize  # Correct import for pluralize
from .models import User, Activity

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username", "email", "is_staff", "is_active", "is_beneficiary", "is_food_bank_staff",
        "is_volunteer", "is_system_administrator", "group_list", "activity_count"
    )
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "groups")
    filter_horizontal = ("groups", "user_permissions")  # Allows easier management of groups
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    def group_list(self, obj):
        """Display a comma-separated list of group names."""
        return ", ".join(group.name for group in obj.groups.all())
    group_list.short_description = "Groups"

    def activity_count(self, obj):
        """Display the number of activities associated with the user."""
        count = obj.activities.count()
        if count > 0:
            return f"{count} {pluralize(count, 'Activity,Activities')}"  # Use pluralize here
        return count
    activity_count.short_description = "Activities"

    def is_beneficiary(self, obj):
        return obj.is_beneficiary()
    is_beneficiary.boolean = True
    is_beneficiary.short_description = "Beneficiary"

    def is_food_bank_staff(self, obj):
        return obj.is_food_bank_staff()
    is_food_bank_staff.boolean = True
    is_food_bank_staff.short_description = "Food Bank Staff"

    def is_volunteer(self, obj):
        return obj.is_volunteer()
    is_volunteer.boolean = True
    is_volunteer.short_description = "Volunteer"

    def is_system_administrator(self, obj):
        return obj.is_system_administrator()
    is_system_administrator.boolean = True
    is_system_administrator.short_description = "System Admin"


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "activity_type", "description", "timestamp", "metadata_summary"
    )
    list_filter = ("activity_type", "timestamp")
    search_fields = ("user__email", "description", "metadata")
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)

    def metadata_summary(self, obj):
        """Display a summary of the metadata field."""
        if obj.metadata:
            return ", ".join(f"{k}: {v}" for k, v in obj.metadata.items())
        return "-"
    metadata_summary.short_description = "Metadata"

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"