from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,TemplateView,CreateView

from car_rent import settings
from main.models import Car,CarClass,Images,AboutUs,Contacts,CarMarka,SendList
from main.forms import OrderDataForm
from django.urls import reverse_lazy
from threading import Thread
from django.template.loader import render_to_string
import json
from django.core.mail import EmailMessage
from django.core.paginator import Paginator



# Create your views here.
class MainPageView(ListView):
    model = Car
    template_name = 'main.html'
    paginate_by = 3
    context_object_name = 'cars'

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['classes'] = CarClass.objects.all()
        context['markas'] = CarMarka.objects.all()
        page = self.request.GET.get('page', 1) if self.request.GET.get('page', 1) != '' else 1
        data = self.get_queryset()
        if data:
            paginator = Paginator(data, self.paginate_by)
            results = paginator.page(page)
            index = results.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 5 if index >= 5 else 0
            end_index = index + 5 if index <= max_index - 5 else max_index
            context['page_range'] = list(paginator.page_range)[start_index:end_index]
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


# def send_email():
#     template_name = 'send-email.html'
#     context = {
#         'data': 'data'
#     }
#     msg = render_to_string(template_name, context)
#     subject = 'Новое заявление'
#     user_emails = SendList.objects.all().values_list('email', flat=True)
#     message = EmailMessage(subject=subject, body=msg, from_email=settings.EMAIL_HOST_USER, to=user_emails)
#     message.content_subtype = 'html'
#     message.send()


class OrderSuccessView(TemplateView):
    # Thread(target=send_email).start()
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



