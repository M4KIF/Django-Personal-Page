from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name="homepage/home.html"


class LinkView(TemplateView):
    template_name="homepage/links.html"
