from . import views
from django.urls import path

urlpatterns = [
    path('add',views.Orderview.as_view(),name="add"),
    path('', views.demo,name='demo'),
    path('home',views.home,name='home'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
    # path('home/<int:pk>', views.order_update_view, name='order_change')
    # path('order',views.add_order,name='order'),
    # path('ajax/load_courses/', views.load_courses, name='ajax_load_courses'),
    # path('orders',views.update,name="don")

    ]