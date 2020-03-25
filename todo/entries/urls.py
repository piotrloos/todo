from django.urls import path
from entries.views import EntryListView, EntryCreateView, EntryRetrieveView, EntryUpdateView, EntryDeleteView


urlpatterns = [
    path('', EntryListView.as_view()),
    path('create', EntryCreateView.as_view()),
    path('<int:pk>', EntryRetrieveView.as_view()),
    path('<int:pk>/update', EntryUpdateView.as_view()),
    path('<int:pk>/delete', EntryDeleteView.as_view()),
]
