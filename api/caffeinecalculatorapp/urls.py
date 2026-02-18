from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

drfRouter = DefaultRouter()

# Register all the routes
drfRouter.register(r"caffeine-items", views.CaffeineItemViewSet, basename="caffeineitem")
drfRouter.register(r"consumed-items", views.ConsumedItemViewSet, basename="consumeditem")
drfRouter.register(r"users", views.UserViewSet, basename="user") # Replace UserList and UserDetail views with UserViewSet

urlpatterns = [
    # Routes for the UserList or UserDetail views (replaced by UserViewSet)
    # path("users/", views.UserList.as_view() , name="user-list"),
    # path(
    #     "users/<int:pk>/",
    #     views.UserDetail.as_view(),
    #     name="user-detail",
    # ),

    # Include all router urls
    path("", include(drfRouter.urls)),
]
