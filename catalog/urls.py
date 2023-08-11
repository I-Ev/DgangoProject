from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, CategoriesListView, ProductsCategListView, HomeView, \
    ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
                  path('', HomeView.as_view(), name='index'),
                  path('home/', HomeView.as_view(), name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('categories/', CategoriesListView.as_view(), name='categories'),
                  path('product/<int:pk>/', cache_page(60 * 15)(ProductDetailView.as_view()), name='product'),
                  path('product/create/', ProductCreateView.as_view(), name='create_product'),
                  path('product/create/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
                  path('products_categ/<int:category_id>/', ProductsCategListView.as_view(), name='products_categ'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
