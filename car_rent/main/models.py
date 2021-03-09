from django.db import models



class CarMarka(models.Model):
    marka = models.CharField(max_length=50, verbose_name='Marka')

    def __str__(self):
        return self.marka

class CarModel(models.Model):
    marka = models.ForeignKey(CarMarka, on_delete=models.CASCADE, verbose_name='Marka',related_name='models')
    model = models.CharField(max_length=50, verbose_name='Model')

    def __str__(self):
        return self.model

class CarYear(models.Model):
    # model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Model',related_name='years')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return str(self.year)

class Transmission(models.Model):
    name = models.CharField(max_length=50, verbose_name='Коробка')

    def __str__(self):
        return str(self.name)

class Fuel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Топливо')

    def __str__(self):
        return str(self.name)

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кузов')

    def __str__(self):
        return str(self.name)

class CarClass(models.Model):
    name = models.CharField(max_length=50, verbose_name='Класс')

    def __str__(self):
        return str(self.name)

# Create your models here.
class Car(models.Model):
    marka = models.ForeignKey(CarMarka, on_delete=models.CASCADE, null=True, verbose_name='Марка',related_name='cars')
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, verbose_name='Модель',related_name='cars')
    car_year = models.ForeignKey(CarYear, on_delete=models.CASCADE, null=True, verbose_name='Год выпуска',related_name='cars')
    transmission = models.ForeignKey(Transmission,on_delete=models.CASCADE, null=True, verbose_name='Коробка передач',related_name='cars')
    main_image = models.ImageField('Main image', upload_to='images/main')
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE, null=True, verbose_name='Топливо', related_name='cars')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, verbose_name='Кузов', related_name='cars')
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE, null=True, verbose_name='Класс авто', related_name='cars')
    seats = models.CharField(max_length=50, verbose_name='Количество сиденье')
    comment = models.TextField('Oписание')

    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    taxi = models.BooleanField(default=False, verbose_name='Такси')

    def get_image(self):
        return self.main_image.url

    def get_car(self):
        return f'{self.marka.marka} {self.model.model} {self.car_year.year}'




class Images(models.Model):
    carr = models.ForeignKey(Car,on_delete=models.CASCADE, verbose_name='Car',related_name='images')
    images = models.ImageField('Допольнительные фотографии', upload_to='images/allImg')

    def __str__(self):
        return f'{self.images}'


class OrderData(models.Model):
    name=models.CharField(max_length=50, verbose_name='Имя')
    surname=models.CharField(max_length=50, verbose_name='Фамилия и Отчество')
    phone_number=models.CharField(max_length=50, verbose_name='Номер телефона')
    order_data=models.CharField(max_length=250, verbose_name='Заказ')
    passport_first = models.ImageField('Пасспорт 1', upload_to='images/users',default='',blank=True,null=True)
    passport_second = models.ImageField('Пасспорт 2', upload_to='images/users',default='',blank=True,null=True)
    driver_lisense_first = models.ImageField('Вод уд. 1', upload_to='images/users',default='',blank=True,null=True)
    driver_lisense_second = models.ImageField('Вод. уд. 2', upload_to='images/users',default='',blank=True,null=True)

    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}   {self.order_data}'


class Contacts(models.Model):
    name=models.CharField(max_length=50, verbose_name='Название организации')
    adress = models.CharField(max_length=200, verbose_name='Адрес организации')
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Электронный адрес')
    corp_number = models.CharField(max_length=50, verbose_name='Номер для корпоративный клиентов',default='',blank=True,null=True)

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    image = models.ImageField('осн фотка', upload_to='images/')
    title = models.CharField(max_length=50, verbose_name='Название')
    text_first =  models.TextField('Текст о нас 1')
    text_second = models.TextField('Текст о нас 2')

    def __str__(self):
        return self.title

class SendList(models.Model):
    #information
    email = models.CharField('Email',max_length=120)

    class Meta:
        verbose_name = 'Почты для заявление'
        verbose_name_plural = 'Почты для заявление'

    def __str__(self):
        return f'{self.email}'
