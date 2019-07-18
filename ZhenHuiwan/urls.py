from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from ZhenHuiwan import settings
from index import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 旅游网站路由
    url(r'^about/',views.about),
    url(r'^contact/',views.contact),
    url(r'^codes/',views.codes),
    url(r'^gallery/',views.gallery),
    url(r'^icons/',views.icons),
    url(r'^index/',views.index),
    url(r'^services/',views.services),
    url(r'^single/',views.single),
    url(r'^$',views.index),

]
