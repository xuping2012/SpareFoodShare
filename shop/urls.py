# shop/urls.py

from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('collection/', views.CollectionView.as_view(), name='collection'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('upload/', views.UploadView.as_view(), name='upload'),
     path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
]