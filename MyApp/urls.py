from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sd_series/', views.sd_series, name='sd_series'),
    path('mr_series/', views.mr_series, name='mr_series'),
    path('arm_series/', views.arm_series, name='arm_series'),
    path('elec_series/', views.elec_series, name='elec_series'),
    path('fluids_l/', views.fluids_l, name='fluids_l'),
    path('paste/', views.paste, name='paste'),
    path('fluids_p/', views.fluids_p, name='fluids_p'),
    path('dev/', views.dev, name='dev'),
    path('test/', views.test, name='test'),
    path('prod/', views.prod, name='prod'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_login/stats/', views.stats, name='admin_login/stats'),
]