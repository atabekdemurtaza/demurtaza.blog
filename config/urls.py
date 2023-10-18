from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path(route='jet/', view=include('jet.urls', 'jet')),
    path(route='admin/', view=admin.site.urls),
    path(route='movies/', view=include('movies.api.urls')),
    path(route='rosetta/', view=include('rosetta.urls')),
    path('', RedirectView.as_view(url='/movies/list', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
