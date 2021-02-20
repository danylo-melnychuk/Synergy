from django.urls import path
from  rest_framework import routers
from .views import UserView, GroupView

router = routers.SimpleRouter()
router.register('users', UserView, basename='users')
router.register('groups', GroupView, basename='groups')

urlpatterns = []
urlpatterns += router.urls