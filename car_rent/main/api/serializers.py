from rest_framework import serializers
from main.models import CarMarka,CarModel,CarYear,Transmission,Fuel,Type,\
    CarClass,Car,Images


class CarMarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMarka
        fields = ('id','marka',)

class CarModelSerializer(serializers.ModelSerializer):
    marka = CarMarkaSerializer()
    class Meta:
        model = CarModel
        fields = ('id','marka','model',)

class CarYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarYear
        fields = ('id','year',)

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ('id','name',)

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('id','name',)

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id','name',)

class CarClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarClass
        fields = ('id','name',)

#
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Images
#         fields = ('carr','image')

class CarSerializer(serializers.ModelSerializer):
    marka = CarMarkaSerializer()
    model = CarModelSerializer()
    car_year = CarYearSerializer()
    transmission = TransmissionSerializer()
    fuel = FuelSerializer()
    type= TypeSerializer()
    car_class = CarClassSerializer()
    images = serializers.StringRelatedField(many=True)

    # image = ImageSerializer(many=True)
    # images = serializers.PrimaryKeyRelatedField(many=True,)
    class Meta:
        model = Car
        fields = ('id','marka','model','car_year','transmission','main_image',
                  'price','fuel','type','car_class','seats','comment',
                  'is_published','taxi','images')
        #
        # def get_images(self,obj):
        #     return ImageSerializer(obj.images,read_only=True).data
