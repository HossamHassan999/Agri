from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import LandPlot

class LandPlotSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LandPlot
        fields = ('owner_name', 'recorded_area', 'parcel_code', 'crop_type', 'comment', 'geom')
        geo_field = 'geom'
  


from rest_framework import serializers


class LandPlotBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPlot
        fields = ['id', 'owner_name', 'recorded_area', 'parcel_code' , 'crop_type']
