from django.conf.urls import url, include
from django.contrib import admin

import users

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls'))
]
