
from . import views
from django.urls import path, include

product_patterns = [
    path("", views.products1),
    path("comments", views.comments),
    path("likes", views.likes),
]

posts_patterns = [
    path('products', views.products),
    path('new', views.new),
    path('top', views.top),
]

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/', include(posts_patterns)),
    path('products/', include(product_patterns)),
    path('about/', views.about, name='about'),
    path('redirect_about', views.redirect_about, name='reidrect'),
    path('redirect_contacts/', views.permanent_redirect_about, name='contacts'),
    path('not_found', views.not_found),
    path('access/<str:login>/<str:password>', views.access, name="access"),
    path('login/<str:login>/<str:password>', views.login, name="login"),
    path('json', views.json),
    path('get', views.get, name="get"),
    path('set', views.set, name="set"),
]

