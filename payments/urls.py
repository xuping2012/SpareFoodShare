# payments/urls.py

from django.urls import path

from . import views

urlpatterns = [
    #path('', views.HomePageView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/<str:pk>', views.create_checkout_session),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('success/<str:pk>', views.success),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
    path('index/', views.index, name='index'),
    #path('shop/', views.ShopView.as_view(), name='shop'),
    path('shop/', views.shoppage, name='shop'),
    #path('product/', views.ProductView.as_view(), name='product'),
    path('product/<str:pk>/', views.product, name='product'),
    path('collection/<str:pk>/', views.collection, name='collection'),
    #path('search/', views.SearchView.as_view(), name='search'),
    path('search/', views.search, name='search'),
    path('categories/<str:pk>/', views.categories, name='categories'),
    #path('upload/', views.UploadView.as_view(), name='upload'),
    path('upload/', views.upload, name='upload'),
    path('upload/csv/', views.upload_CSV, name='upload_csv'),
    path('payment/<str:pk>', views.payment, name='payment'),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.user_register, name="register"),
    path('contact/<str:pk>', views.contact, name='contact'),
    path("dashboard/", views.dashboard, name="dashboard"),
    ]