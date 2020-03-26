from rest_framework import viewsets
from entries.models import Entry
from entries.serializers import EntrySerializer


class EntryListView(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
