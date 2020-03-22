from django.conf.urls import url,include
from rest_framework import routers
from hrm import views
from hrm.apiviews import EmployeeDetail

router = routers.DefaultRouter()
router.register(r'designation', views.DesignationViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^index', views.index),
    url(r'^emp/$', EmployeeDetail.as_view()),
    url(r'^emp/(?P<pk>\d+)/$', EmployeeDetail.as_view()),
]