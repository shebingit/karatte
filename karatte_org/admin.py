from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(videos, MyModelAdmin)
admin.site.register(hbgimg)
admin.site.register(imagefolder)
admin.site.register(images)
admin.site.register(blackbelt_holders)
admin.site.register(affiliation)
admin.site.register(carousel)
admin.site.register(members)
admin.site.register(news)
admin.site.register(register_members)
admin.site.register(pdfimg)
admin.site.register(contents)
admin.site.register(moreconts)
admin.site.register(HistoyrPdf)