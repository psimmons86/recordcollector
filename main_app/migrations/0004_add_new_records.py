from django.db import migrations

def add_records(apps, schema_editor):
    Record = apps.get_model('main_app', 'Record')
    records = [
        {"name": "Petrichor", "artist": "070 Shake", "genre": "Hip Hop", "release_date": "2024-01-15"},
        {"name": "Hurry Up Tomorrow", "artist": "The Weeknd", "genre": "R&B", "release_date": "2024-02-01"},
        {"name": "In Waves", "artist": "Jamie XX", "genre": "Electronic", "release_date": "2024-01-20"},
        {"name": "Evergreen", "artist": "Soccer Mommy", "genre": "Indie Rock", "release_date": "2024-01-10"},
        {"name": "Balloonerism", "artist": "Mac Miller", "genre": "Hip Hop", "release_date": "2024-01-05"},
    ]
    for record in records:
        Record.objects.create(**record)

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_record_album_cover'),
    ]

    operations = [
        migrations.RunPython(add_records),
    ]
