from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include

import users

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
