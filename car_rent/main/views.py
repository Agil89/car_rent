from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from main.models import Car,CarClass,Images,AboutUs,Contacts,CarMarka
from main.forms import OrderDataForm
from django.urls import reverse_lazy


# Create your views here.
class MainPageView(TemplateView):
    # model = Cake

    template_name = 'main.html'
    # paginate_by = 6
    # context_object_name = 'cakes'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cars'] = Car.objects.all()
        context['classes'] = CarClass.objects.all()
        context['markas'] = CarMarka.objects.all()
        return context

class CarDetailView(DetailView):
    model = Car
    template_name = 'detail.html'
    context_object_name = 'car'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        images = Images.objects.filter(carr__id=self.get_object().pk)
        print(images)
        context['imagess'] = images
        return context


class CreateOrderView(CreateView):
    form_class = OrderDataForm
    template_name = 'form-fill.html'
    success_url='/success'

    # def get_success_url(self):
    #     return render(self.request,'success.html')

    #

    def form_valid(self,form):
        order = form.save(commit=False)
        order.order_data = self.request.POST.get('all-data')
        order.save()
        return super().form_valid(form)


class OrderSuccessView(TemplateView):
    template_name = 'success.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = AboutUs.objects.first()
        context['about'] = about
        return context

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = Contacts.objects.first()
        context['contacts'] = contacts
        return context