from django.urls import path, include


app_name = 'sport'

urlpatterns = [
    path('api/v1/', include('sport.api.v1.urls')),
]