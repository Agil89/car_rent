from django.urls import path
from main.api.views import ModelListView,CarListView,AllCarsListView,OrderCreateView, \
CarClassesView,CarMarkaView

app_name = 'api_cars'

urlpatterns = [
    path('cars/',CarListView.as_view(),name='cars'),
    path('models/',ModelListView.as_view(),name= 'models'),
    path('all/',AllCarsListView.as_view(),name='all'),
    path('orders/',OrderCreateView.as_view(),name='orders'),
    path('classes/',CarClassesView.as_view(),name='classes'),
    path('markas/',CarMarkaView.as_view(),name='markas')

]