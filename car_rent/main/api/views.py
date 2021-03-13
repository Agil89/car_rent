from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import CarModel,Car
from main.api.serializers import CarModelSerializer,CarSerializer
import math
from main.api.my_paginations import PagePagination
import json

class CarListView(APIView):
    def get(self,request):
        data = request.GET
        car_model=data.get('model_id')
        car_class = data.get('checked_class')
        car_status = data.get('checked_status')
        minPrice = data.get('minPrice')
        maxPrice = data.get('maxPrice')
        filtered_cars = Car.objects.all()
        if minPrice:
            filtered_cars=filtered_cars.filter(price__gte=minPrice).distinct()
        if maxPrice:
            filtered_cars=filtered_cars.filter(price__lte=maxPrice).distinct()
        if car_model:
                filtered_cars = filtered_cars.filter(model__id=car_model)
        if car_class:
                filtered_cars = filtered_cars.filter(car_class__name=car_class)
        if car_status and car_status=='Да':
            filtered_cars=filtered_cars.filter(taxi=True)
        if car_status and car_status=='Нет':
            filtered_cars=filtered_cars.filter(taxi=False)


        car_count = filtered_cars.count()
        car_count_for_each_page = 6
        page_count = math.ceil(car_count/car_count_for_each_page)
        page_range = range(1,page_count+1)

        page = data.get('page',1)
        if isinstance(page, str) and page.isdigit():
            page = int(page)
        cars_for_each_page = filtered_cars[(page-1)*6:page*6]
        serializered_cars = CarSerializer(cars_for_each_page,many=True)
        return Response({
            'filtered_cars': serializered_cars.data,
            'page_range': page_count,
        })

class ModelListView(APIView):
    def get(self,request):
        data = request.GET
        id = data.get('marka_id')
        models = CarModel.objects.filter(marka__id=id)
        print(models)
        serialized_models = CarModelSerializer(models,many=True)
        return Response({
                    'models': serialized_models.data,
                })

class AllCarsListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = PagePagination


class OrderCreateView(APIView):

    def post(self,request):
        # data = request.POST
        form_data = json.loads(request.body.decode())
        print(form_data)
        print(form_data('userName'))
        print(form_data('userSurname'))
        # data2 = request.body
        # print(data2)
        # request.body["orderData"]
        # print(request.body["userName"])
        # print(request.body["userSurname"])
        # print(request.body["phoneNumber"])
        # print(request.body["orderData"])
        print('its ok')