from django.conf.urls import url
from .views import UserActivityView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
url(r'user/activity_details/$',UserActivityView.as_view(),name='user_activity'),

]