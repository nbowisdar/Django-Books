# black: skip-file

from django.urls import path

from . import views

app_name = "books"

# fmt: off
urlpatterns = [
    path("", views.BookAPIList.as_view(), name="book-list"),
    path("<int:pk>/", views.BookAPIUpdate.as_view(), name="book-update"),
    path('<int:pk>/delete/', views.BookAPIDestroy.as_view(), name='book-destroy'),
]
# fmt: on
