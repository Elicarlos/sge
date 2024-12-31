from django.urls import path
from .views import BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name="brand_list"),
    path('brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brand/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete')
]