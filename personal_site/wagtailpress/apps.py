from django.apps import AppConfig

# from django.utils.translation import lazy_gettext as _
from django.utils.translation import ugettext_lazy as _


class WagtailpressConfig(AppConfig):
    name = "wagtailpress"
    verbose_name = _("WagtailPress")
