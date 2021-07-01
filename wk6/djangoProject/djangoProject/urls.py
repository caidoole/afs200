from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('useraccounts/', include('django.contrib.auth.urls')),
    path('', include('mainsite.urls'))
]
