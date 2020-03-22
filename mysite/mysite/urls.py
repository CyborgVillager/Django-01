from django.contrib import admin
from django.urls import include,path

# Include Img Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # index
    path('', include('ursitey.urls')),
    #
    path('ursitey/', include('ursitey.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
