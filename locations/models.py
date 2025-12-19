from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.PointField(srid=4326)  # WGS 84 latitude/longitude
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
