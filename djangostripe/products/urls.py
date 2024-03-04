from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    ItemListView,
)

app_name = "items"

urlpatterns = [
    path("", ItemListView.as_view(), name="item-list"),
    path("item/<int:pk>/", views.item_detail, name="item-detail"),
    path("buy/<int:pk>/", views.create_checkout_session, name="api")
]

