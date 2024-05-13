from django.contrib import admin

from party.models import Submission, Party, Compo

# Register your models here.
admin.site.register(Party)
admin.site.register(Compo)
admin.site.register(Submission)