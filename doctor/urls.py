from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() 
router.register('list', views.SpecializationViewset)
router.register('designation', views.DesignationViewset)
router.register('available', views.AvailableTimeViewset)
router.register('doctor', views.DoctorViewset)
router.register('review', views.ReviewViewset)


urlpatterns = [
    path('', include(router.urls)),
]