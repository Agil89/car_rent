
from django.urls import path
from main.views import MainPageView,CarDetailView,CreateOrderView,OrderSuccessView,AboutUsView,ContactPageView


app_name = 'main'


urlpatterns = [
    path('',MainPageView.as_view(),name='home'),
    path('car-detail/<int:pk>/',CarDetailView.as_view(),name='car-detail'),
    path('create-order/',CreateOrderView.as_view(),name='create-order'),
    path('success/',OrderSuccessView.as_view(),name='success'),
    path('about/',AboutUsView.as_view(),name='about-us'),
    path('contacts/',ContactPageView.as_view(),name='contacts')

]