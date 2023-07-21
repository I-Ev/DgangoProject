from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product, categories, products_categ

app_name = CatalogConfig.name

urlpatterns = [
                  path('', home, name='index'),
                  path('home/', home, name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('categories/', categories, name='categories'),
                  path('product/<int:product_id>/', product, name='product'),
                  path('products_categ/<int:category_id>/', products_categ, name='products_categ'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
