from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from braces.views import FormValidMessageMixin
from django_monitor.views import MonitorMixin

from livinglots_genericviews import AddGenericMixin


class BaseAddStewardNotificationView(FormValidMessageMixin, MonitorMixin,
                                     AddGenericMixin, CreateView):

    def get_form_valid_message(self):
        return _('Project submitted successfully. It will be posted once we '
                 'approve it.')

    def get_success_url(self):
        return self.get_content_object().get_absolute_url()

    def get_template_names(self):
        return ['livinglots/steward/add_stewardnotification.html',]
