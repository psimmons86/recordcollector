from django.contrib import admin
from .models import Record, Listening, Label

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'genre', 'release_date', 'album_cover')

class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')

admin.site.register(Record, RecordAdmin)
admin.site.register(Listening)
admin.site.register(Label, LabelAdmin)
