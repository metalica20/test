"""
BIPAD URL Configuration
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import static
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from hazard.views import HazardViewSet
from alert.views import AlertViewSet
from incident.views import IncidentViewSet
from event.views import EventViewSet
from federal.views import (
    ProvinceViewSet,
    DistrictViewSet,
    MunicipalityViewSet,
    WardViewSet,
)
from resources.views import ResourceViewSet
from organization.views import (
    OrganizationViewSet,
    ProjectViewSet,
)
from loss.views import (
    LossViewSet,
    InfrastructureTypeViewSet,
    LivestockTypeViewSet,
)

from realtime.views import (
    EarthquakeViewSet,
    RiverViewSet,
    RainViewSet,
)

from inventory.views import (
    CategoryViewSet,
    ItemViewSet,
    InventoryViewSet,
)

from risk_profile.views import (
    HospitalViewSet,
    SchoolViewSet,


)

admin.site.site_header = 'BIPAD administration'
schema_view = get_schema_view(
    openapi.Info(
        title="BIPAD API",
        default_version='v1',
    ),
)

router = routers.DefaultRouter()
router.register(r'hazard', HazardViewSet,
                base_name='hazard')
router.register(r'alert', AlertViewSet,
                base_name='alert')
router.register(r'incident', IncidentViewSet,
                base_name='incident')
router.register(r'event', EventViewSet,
                base_name='event')
router.register(r'province', ProvinceViewSet,
                base_name='province')
router.register(r'district', DistrictViewSet,
                base_name='district')
router.register(r'municipality', MunicipalityViewSet,
                base_name='municipality')
router.register(r'ward', WardViewSet,
                base_name='ward')
router.register(r'resource', ResourceViewSet,
                base_name='resource')
router.register(r'organization', OrganizationViewSet,
                base_name='organization')
router.register(r'project', ProjectViewSet,
                base_name='project')
router.register(r'loss', LossViewSet,
                base_name='loss')
router.register(r'infrastructure-type', InfrastructureTypeViewSet,
                base_name='infrastructure_type')
router.register(r'livestock-type', LivestockTypeViewSet,
                base_name='livestock_type')
router.register(r'earthquake', EarthquakeViewSet,
                base_name='earthquake')
router.register(r'river', RiverViewSet,
                base_name='river')
router.register(r'rain', RainViewSet,
                base_name='rain')
router.register(r'inventory-category', CategoryViewSet,
                base_name='inventory-category')
router.register(r'inventory-item', ItemViewSet,
                base_name='inventory-item')
router.register(r'inventory', InventoryViewSet,
                base_name='inventory')
router.register(r'school', SchoolViewSet,
                base_name='school')
router.register(r'hospital', HospitalViewSet,
                base_name='hospital')


API_VERSION = 'v1'


def get_api_path(path):
    return r'^api/(?P<version>({}))/{}'.format(API_VERSION, path)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')),
    path('silk/', include('silk.urls', namespace='silk')),
    re_path(get_api_path(r'token/$'), TokenObtainPairView.as_view(),
            name='token_obtain_pair'),
    re_path(get_api_path(r'token/refresh/$'),
            TokenRefreshView.as_view(), name='token_refresh'),
    re_path(get_api_path(r'token/verify/$'),
            TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^api(?P<format>\.json|\.yaml)$', schema_view.with_ui(
        cache_timeout=0), name='schema-json'),
    re_path(r'^api/$', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc'), name='schema-redoc'),
    re_path(get_api_path(''), include(router.urls)),
    path('risk_profile/', include('risk_profile.urls')),
    path('risk_profile/', include('mappage.urls')),
] + static.static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
) +static.static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
