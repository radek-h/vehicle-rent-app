from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> vuejs

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
<<<<<<< HEAD
        if not settings.DEBUG:
            template_name = "index-dev.html"
        else:
            template_name = "index.html"
=======
        template_name = "index.html"
>>>>>>> vuejs
        return template_name