# from rest_framework import viewsets
# from rest_framework.permissions import AllowAny  # later you can restrict
# from .models import Restaurant, MenuItem
# from .serializers import RestaurantSerializer, MenuItemSerializer


# class RestaurantViewSet(viewsets.ModelViewSet):
#     queryset = Restaurant.objects.all().order_by("-created_at")
#     serializer_class = RestaurantSerializer
#     permission_classes = [AllowAny]  # dev only; change later


# class MenuItemViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.objects.all().order_by("-created_at")
#     serializer_class = MenuItemSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         restaurant_id = self.request.query_params.get("restaurant")
#         if restaurant_id:
#             queryset = queryset.filter(restaurant_id=restaurant_id)
#         return queryset


# GET /api/restaurants/ – list

# POST /api/restaurants/ – create

# GET /api/restaurants/<id>/ – retrieve

# PUT /api/restaurants/<id>/ – full update

# PATCH /api/restaurants/<id>/ – partial update

# DELETE /api/restaurants/<id>/ – delete


from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from . import services


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by("-created_at")
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="create-with-default-menu")
    def create_with_default_menu(self, request):
        name = request.data.get("name")
        address = request.data.get("address", "")
        phone = request.data.get("phone", "")

        if not name:
            return Response(
                {"detail": "Name is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        restaurant = services.create_restaurant_with_default_menu(
            name=name, address=address, phone=phone
        )
        serializer = self.get_serializer(restaurant)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("-created_at")
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        restaurant_id = self.request.query_params.get("restaurant")

        if restaurant_id and str(restaurant_id).isdigit():
            queryset = queryset.filter(restaurant_id=int(restaurant_id))
        # else: ignore bad values like "NaN" instead of crashing

        return queryset
