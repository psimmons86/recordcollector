from django.contrib import admin
from .models import Record, Listening

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'genre', 'release_date', 'album_cover')

admin.site.register(Record, RecordAdmin)
admin.site.register(Listening)
