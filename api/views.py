from rest_framework import generics
from .models import Item,Locations

from .serializers import itemSerializer,LocationSerializer


class ItemList(generics.ListCreateAPIView):
    serializer_class = itemSerializer


    def  get_queryset(self):
       queryset = Item.objects.all()
       location = self.request.query_params.get('location')
       if location is not None:
        queryset = queryset.filter(itemLocation=location)
        return queryset
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = itemSerializer
    queryset = Item.objects.all()



class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Locations.objects.all()
    


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Locations.objects.all()
    