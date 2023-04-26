from rest_framework.decorators import api_view
# api_view = This will assign certain permissions to this function
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer

@api_view(["GET", "POST"])
def super_type_list(request):
    if request.method == "GET":
        supertypes = SuperType.objects.all()
        serializer = SuperTypeSerializer(supertypes, many =True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SuperTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
@api_view(["GET"])
def super_types_detail(request,pk):

    print(pk)
    return Response(pk)
        




# Create your views here.
