from django.urls import path
from main.api.views import ModelListView,CarListView

app_name = 'api_cars'

urlpatterns = [
    path('cars/',CarListView.as_view(),name='cars'),
    path('models/',ModelListView.as_view(),name= 'models'),

]