from django.conf import settings
from django.conf.urls import include, url
# from django.contrib import admin
from django.conf.urls.static import static


from . import views


urlpatterns = [
    ### API ###
    url(r'^$', views.root),
    url(r'^nodes/', include('api.nodes.urls', namespace='nodes')),
] + static('/static/', document_root=settings.STATIC_ROOT)
