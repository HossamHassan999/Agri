from django.db import models
from django.contrib.gis.db import models as gis_models

class LandPlot(models.Model):
    owner_name = models.CharField(max_length=255, blank= True , null=True)
    recorded_area = models.CharField(max_length=255, blank= True , null=True)
    parcel_code = models.IntegerField(blank= True , null=True)
    crop_type = models.CharField(max_length=255, blank= True , null=True)
    comment = models.CharField(max_length=255, blank= True , null=True)
    geom = gis_models.PolygonField(srid=4326 , blank= True , null=True) 
    
    def __str__(self):
        return self.owner_name 



        
