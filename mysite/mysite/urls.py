from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    # index
    path('', include('ursitey.urls')),
    #
    path('ursitey/', include('ursitey.urls')),
]
