from rest_framework import generics, decorators, response, status, mixins, viewsets
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .serializers import UserSerializer, CaffeineItemSerializer
from .models import CaffeineItem

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@decorators.api_view(["GET", "POST"])
def caffeine_item_list(request):
    """View function based

    Args:
        request (str): request type

    Returns:
        _type_: _description_
    """
    if request.method == "GET":
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return response.Response(serializer.data)

    elif request.method == "POST":
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaffeineItemListViewClassBased(APIView):
    def get(self, request, format=None):
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CaffeineItemListMixins(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CaffeineItemListGenerics(generics.ListCreateAPIView):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

class CaffeineItemViewSet(viewsets.ModelViewSet):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

# TODO-6-3 Créer une nouvelle viewset pour le ConsumedItem et lui ajouter une
# action POST permettant d'incrémenter le consumed number d'un consumed item
# TODO-6-6 Remplacer les generic views du User par un viewset
# TODO-6-10 Mettre à jour le viewset du User pour utiliser le nouveau serializer
# TODO-6-12 Mettre à jour le viewset de ConsumedItem pour utiliser le nouveau serializer
# et vérifier que les nouvelles données sont bien accessibles via la browsable API de DRF
