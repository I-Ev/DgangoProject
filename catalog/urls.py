from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)