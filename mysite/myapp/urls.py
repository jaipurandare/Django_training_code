from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
    url(r'^user_auth/$',views.UserAuthView.as_view(),name='UserAuthView'),
]
