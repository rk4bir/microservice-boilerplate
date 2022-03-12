from django.urls import reverse
from oauth2_provider.models import AbstractApplication
# from .utils import app_icon_upload_dir


class Application(AbstractApplication):
    run_before = [
        ('oauth2_provider', '0001_initial'),
    ]
    # icon = models.ImageField(default='applications/default.png',
    #                          upload_to=app_icon_upload_dir, blank=True, null=True)

    class Meta:
        verbose_name = 'Client App'
        verbose_name_plural = "Client Apps"

    def get_absolute_url(self):
        return reverse('oauth2:apps-detail', kwargs={'pk': self.pk})
