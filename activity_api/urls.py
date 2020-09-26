from django.conf.urls import url
from .views import UserActivityView

urlpatterns = [
url(r'user/activity_details/$',UserActivityView.as_view(),name='user_activity'),
]
