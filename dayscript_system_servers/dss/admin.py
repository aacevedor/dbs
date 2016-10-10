from django.contrib import admin

from .models import Server
from .models import Command
from .models import Server_group
from .models import Server_history




admin.site.register(Server)
admin.site.register(Command)
admin.site.register(Server_group)
admin.site.register(Server_history)



# Register your models here.
