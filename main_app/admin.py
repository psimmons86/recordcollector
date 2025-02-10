from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'genre', 'release_date', 'album_cover')

admin.site.register(Record, RecordAdmin)
from .models import Record

