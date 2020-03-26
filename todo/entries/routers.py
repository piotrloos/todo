from rest_framework import routers
from entries.views import EntryListView


router = routers.DefaultRouter()
router.register(r'entries', EntryListView)
