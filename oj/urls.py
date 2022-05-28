from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

from oj.dev_settings import DEBUG

urlpatterns = [
    path("api/", include("account.urls.oj")),
    path("api/admin/", include("account.urls.admin")),
    path("api/", include("announcement.urls.oj")),
    path("api/admin/", include("announcement.urls.admin")),
    path("api/", include("conf.urls.oj")),
    path("api/admin/", include("conf.urls.admin")),
    path("api/", include("problem.urls.oj")),
    path("api/admin/", include("problem.urls.admin")),
    path("api/", include("contest.urls.oj")),
    path("api/admin/", include("contest.urls.admin")),
    path("api/", include("submission.urls.oj")),
    path("api/admin/", include("submission.urls.admin")),
    path("api/admin/", include("utils.urls")),
]


if DEBUG:
    # API DOCUMENT URLS
    show_url_patterns = [url_pattern for url_pattern in urlpatterns]
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(urlconf=show_url_patterns), name="schema"),
        path('docs/', SpectacularSwaggerView.as_view(url_name="schema"), name='swagger'),
        path('redoc/', SpectacularRedocView.as_view(url_name="schema"), name='redoc')
    ]
