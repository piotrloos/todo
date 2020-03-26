from django.urls import include, path
from entries.routers import router


urlpatterns = [
    path('', include(router.urls)),
]
