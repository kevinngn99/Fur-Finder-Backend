from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/pets', views.PetViewSet)
router.register(r'api/fidofinder', views.FidoFinderSet)
router.register(r'api/helpinglostpets', views.HelpingLostPetsSet)
router.register(r'api/lostmydoggie', views.LostMyDoggieSet)
router.register(r'api/pawboost', views.PawBoostSet)
router.register(r'api/petkey', views.PetKeySet)
router.register(r'api/tabbytracker', views.TabbyTrackerSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]