from django.urls import path

from .views import ShortlinkListView,redirector,ShortlinkCreateView,ShortlinkRetrieveView



urlpatterns = [

    path('shortened-urls/list', ShortlinkListView.as_view(), name='url-list'),
    path('shortened-urls/create', ShortlinkCreateView.as_view(), name='url-create'),
    path('<path:long_url>/', ShortlinkRetrieveView.as_view(), name='get-short_url'),
    path('<slug:short_url>', redirector, name='redirector'),


]
