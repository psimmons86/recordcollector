from django.db import models
from django.urls import reverse

class Label(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.name} ({self.country})"
        
    def get_absolute_url(self):
        return reverse('label-detail', kwargs={'pk': self.id})

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night')
)


class Record(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    album_cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return f"{self.name} - {self.genre} - {self.release_date}"
        
    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'record_id': self.id})

class Listening(models.Model):
    date = models.DateField('Listening date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
