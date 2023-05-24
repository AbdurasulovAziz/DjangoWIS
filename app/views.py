from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'app/home.html'
    
    # def get(self, request, *args, **kwargs):
    #     return super().get(self, request, *args, **kwargs)




