
from django.urls import include,path
from . import views

app_name='music'
urlpatterns = [
    # /music/
    path('',views.index,name="index"),

    # /music/1234/
    path('<int:album_id>/',views.detail,name ='detail'),

    # /music/1234/favorite/
    path('<int:album_id>/favorite/',views.favorite,name ='favorite'),
]