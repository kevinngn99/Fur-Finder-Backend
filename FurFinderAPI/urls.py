from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'api/register/', views.RegisterViewSet)
router.register(r'api/pets/', views.PetViewSet)
#router.register(r'api/reportedpets/', views.ReportedPetsViewSet)
router.register(r'api/fidofinder/', views.FidoFinderSet)
router.register(r'api/helpinglostpets/', views.HelpingLostPetsSet)
router.register(r'api/lostmydoggie/', views.LostMyDoggieSet)
router.register(r'api/pawboost/', views.PawBoostSet)
router.register(r'api/petkey/', views.PetKeySet)
router.register(r'api/tabbytracker/', views.TabbyTrackerSet)
router.register(r'api/UserMessages/', views.UserMessagesViewSet)


router.register(r'^api/register/(?P<zip>[0-9]+)', views.RegisterViewSet)
router.register(r'^api/pets/(?P<zip>[0-9]+)', views.PetViewSet)
router.register(r'^api/fidofinder/(?P<zip>[0-9]+)', views.FidoFinderSet)
router.register(r'^api/helpinglostpets/(?P<zip>[0-9]+)', views.HelpingLostPetsSet)
router.register(r'^api/lostmydoggie/(?P<zip>[0-9]+)', views.LostMyDoggieSet)
router.register(r'^api/pawboost/(?P<zip>[0-9]+)', views.PawBoostSet)
router.register(r'^api/petkey/(?P<zip>[0-9]+)', views.PetKeySet)
router.register(r'^api/tabbytracker/(?P<zip>[0-9]+)', views.TabbyTrackerSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('api/login/', obtain_auth_token, name='login'),
]
