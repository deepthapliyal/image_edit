from django.contrib import admin
from django.urls import path, include
from . import urls_media

urlpatterns  = [
    path('admin/', admin.site.urls),
    path('images/', include("images.urls"), name="images"),
]

urlpatterns += urls_media.urlpatterns
# add at the last
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
