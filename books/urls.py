from django.urls import path
import books
from books.views import PublisherList

urlpatterns = [
    path('publishers/',PublisherList.as_view())
]