from django.urls import path,include
from apps.news import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('news/', include("apps.news.urls")),
    path('cms/',include('apps.cms.urls')),
    path('account/', include("apps.xauth.urls")),
    path('course/',include('apps.course.urls')),
    path('payinfo/',include('apps.payinfo.urls')),
    path('ueditor/',include('apps.ueditor.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path("__debug__/",include(debug_toolbar.urls)))