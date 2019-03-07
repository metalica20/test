from rest_framework import viewsets,views
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
import json
from risk_profile.models import Hospital,School
from hazard.models import Hazard 
from .serializers import HospitalSerializer
from django.contrib.gis.db.models.functions import Distance
from django.apps import apps
import io
from rest_framework.parsers import JSONParser
from django.contrib.gis.measure import D
from django.views.generic import TemplateView

# Create your views here.

class HazardResourceViewSet(views.APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request,*args,**kwargs):
        longitude = self.kwargs['long']
        latitude =self.kwargs['lat']
        hazard_title = self.kwargs['hazard']
        try:
            distance_parm= self.kwargs['distance']
        except:
            distance_parm=3000
        try: 
            count= int(self.kwargs['count'])
        except:
            count=100
        
        user_location =GEOSGeometry('POINT({} {})'.format(longitude,latitude), srid=4326)

        #Hazard_object = Hazard.objects.get(title=hazard_title)
        #Hresources = Hazard_object.hazardresources_set.all()
        api_json = {}
        
        if(hazard_title=='flood'):
            resource_array=['Hospital','School']
        elif (hazard_title=='landslide'):
            resource_array=['MarketCenter']


        resource_object=[]
        print(distance_parm)
        for resource in resource_array:
            model_x= apps.get_model('risk_profile', resource)            
            resource_queryset=model_x.objects \
            .filter(location__distance_lte=(user_location,D(km=distance_parm))) \
            .annotate(distance=Distance('location',user_location)) \
            .order_by('distance')[0:count]
            print(resource_queryset)
            resource_json= HospitalSerializer(resource_queryset,many=True)
            json = JSONRenderer().render(resource_json.data)
            stream = io.BytesIO(json)
            data = JSONParser().parse(stream)
            api_json[resource] =data
        
        return Response(api_json)



# HTML View

class MapPage(TemplateView):
    template_name= 'mapPage.html'