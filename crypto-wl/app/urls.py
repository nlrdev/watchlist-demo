from django.urls import path
from .views import (
    app,
)

urlpatterns = [
    path("", app, name="app"),
    path("<slug:page>/", app, name="app"),
    path("<slug:page>/<slug:function>/", app, name="app"),
]
