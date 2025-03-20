from django.urls import path,re_path
# from shop.views import first_view,second_view,first_html,index
from shop.views import home, info
urlpatterns = [
    # path("hello/<path:year>/", first_view),
    # path("", index),
    # path("hello/first_html",first_html),
    # re_path(r"^reg/(?P<year>2[0-9]{3})/$", second_view),
    path("", home, name="home"),
    path("info", info, name="info"),
]