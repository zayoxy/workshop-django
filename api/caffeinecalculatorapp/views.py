from rest_framework import generics, decorators, response, status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User

from .serializers import UserSerializer, ComplexeUserSerializer, CaffeineItemSerializer, ComplexeConsumedItemSerializer
from .models import CaffeineItem, ConsumedItem

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): # Same as UserList
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet): # Replace UserList and UserDetail views with UserViewSet
    queryset = User.objects.all()
    serializer_class = ComplexeUserSerializer


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

class ConsumedItemViewSet(viewsets.ModelViewSet):
    queryset = ConsumedItem.objects.all()
    serializer_class = ComplexeConsumedItemSerializer

    @action(detail=True, methods=["POST"], url_path="increase-by-one")
    def increase_by_one(self, request, pk):
        consumed_item = get_object_or_404(ConsumedItem, pk=pk)

        data = {"consumed_number": consumed_item.consumed_number + 1}
        serializer = self.get_serializer(
            consumed_item,
            data=data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
