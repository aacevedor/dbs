from django.conf import settings
from django.utils.translation import ugettext_lazy as _

INTERFACE_STATUS = (
    ('0', _('Inactive')),
    ('1', _('Active'))
)


HISTORY_STATUS = (
    ('0', _('Incomplete')),
    ('1', _('Complete'))
)

GROUP_COMMANDS = (
    ('0', _('mysql')),
    ('1', _('files')),
    ('2', _('history')),
    ('3', _('others'))
)

OPERATIVE_SYSTEM = (
    ('Linux Ubuntu', _('Linux Ubuntu')),
    ('Linux Centos', _('Linux Centos')),
    ('Linux Fedora', _('Linux Fedora')),
    ('Linux Mandriba', _('Linux Mandriba'))
)
