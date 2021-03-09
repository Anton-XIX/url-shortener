from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import ShortLinkListSerializer, ShotlinkCreateSerializer, ShortLinkRetrieveSerializer
from .models import ShortLink
from django.shortcuts import redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from requests import head, RequestException


def validate_long_urls(model):
    if model.last_validation < timezone.now() - timezone.timedelta(minutes=180):

        try:
            # response = PoolManager().urlopen('GET', self.long_url, retries=1, timeout=1.0)
            response = head(model.long_url)

            if response.status_code == 200:
                model.is_broken = False
        except RequestException:
            model.is_broken = True
    model.last_validation = timezone.now()
    model.save()


class ShortlinkListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkListSerializer

    def get(self, request, *args, **kwargs):
        for link in ShortLink.objects.all():
            validate_long_urls(link)
        return self.list(request, *args, **kwargs)


class ShortlinkCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ShortLink.objects.all()
    serializer_class = ShotlinkCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShortlinkRetrieveView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkRetrieveSerializer
    lookup_field = 'long_url'



def redirector(request, short_url):
    instance = get_object_or_404(ShortLink, short_url=short_url)
    return redirect(instance.long_url)
