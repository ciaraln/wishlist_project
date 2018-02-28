from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^lr_app/', include('apps.lr_app.urls')),
	url(r'^first_app/', include('apps.first_app.urls')),
    url(r'^admin/', admin.site.urls),
]
