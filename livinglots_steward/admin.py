from django.contrib import admin
from django.core.urlresolvers import reverse

from admin_enhancer.admin import EnhancedModelAdminMixin


class StewardAdminMixin(EnhancedModelAdminMixin):

    def stewarded_target(self, obj):
        try:
            return '<a href="%s" target="_blank">%s</a>' % (
                obj.content_object.get_absolute_url(),
                obj.content_object
            )
        except Exception:
            return ''
    stewarded_target.allow_tags = True


class StewardNotificationAdminMixin(StewardAdminMixin, admin.ModelAdmin):

    fields = ('stewarded_target', 'name', 'use', 'support_organization',
              'land_tenure_status', 'include_on_map', 'phone', 'email', 'type',
              'url', 'facebook_page',)
    list_display = ('pk', 'name', 'stewarded_target',)
    readonly_fields = ('content_type', 'object_id', 'stewarded_target',)


class StewardProjectAdminMixin(StewardAdminMixin, admin.ModelAdmin):

    fields = (
        ('project_name', 'use',),
        ('stewarded_target',),
        'organizer', 'steward_notification_link',
        ('support_organization', 'land_tenure_status',),
        ('started_here', 'include_on_map',),
        ('date_started', 'external_id',),
    )
    list_display = ('pk', 'project_name', 'stewarded_target', 'organizer',
                    'use', 'include_on_map',)
    list_filter = ('use', 'include_on_map',)
    readonly_fields = ('stewarded_target', 'steward_notification_link',)
    search_fields = ('project_name',)

    def steward_notification_link(self, obj):
        try:
            return '<a href="%s" target="_blank">%s</a>' % (
                reverse('admin:steward_stewardnotification_change',
                        args=(obj.steward_notification.pk,)),
                obj.steward_notification,
            )
        except Exception:
            return '(none)'
    steward_notification_link.allow_tags = True
