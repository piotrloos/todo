from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from entries.models import Entry
from entries.serializers import EntrySerializer


class EntryListView(ListView):
    model = Entry
    template_name = ''
    serializer_class = EntrySerializer
    ordering = 'id'
    queryset = Entry.objects.all()


class EntryCreateView(CreateView):
    pass


class EntryRetrieveView(DetailView):
    model = Entry
    template_name = ''
    serializer_class = EntrySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        id = self.request.GET.get('id')
        qs = qs.filter(pk=id)


class EntryUpdateView(UpdateView):
    pass


class EntryDeleteView(DeleteView):
    pass
