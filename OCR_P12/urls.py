"""OCR_P12 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework import routers
from users.views import UserViewSet
from clients.views import ClientViewSet
from events.views import EventViewSet
from contracts.views import ContractViewSet
from django.urls import path

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet, basename='Client')
router.register(r'events', EventViewSet, basename='Event')
router.register(r'contracts', ContractViewSet)


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('sentry-debug/', trigger_error),

              ] + router.urls
