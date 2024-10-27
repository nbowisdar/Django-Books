from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from books.api.views import BooksViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()


router.register(r"books", BooksViewSet, basename="book")


app_name = "api"
urlpatterns = router.urls
