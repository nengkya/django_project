from django.views.generic import TemplateView

#create your views here
class HomePageView(TemplateView):
    template_name = 'home.html'
