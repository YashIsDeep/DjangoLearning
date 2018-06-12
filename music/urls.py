
from django.urls import include,path
from . import views
urlpatterns = [
    # /music/
    path('',views.index,name="index"),

    # /music/1234/
    path('<int:album_id>/',views.detail,name ='detail')
]