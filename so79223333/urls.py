from django.contrib import admin
from django.urls import path

from investors.views import investor_relations

urlpatterns = [
    path("admin/", admin.site.urls),
    path("investors/", investor_relations),
]
