from django.urls import path

from . import views

urlpatterns = [
    path(
        "initialize_payment/",
        view=views.initialize_payment_api_view,  # Complete URL (Адрес результата) ga qo'yasiz.
        name="initialize_payment",
    ),
    path(
        "integration_with_click/",
        view=views.accept_click_request_view,  # Prepare URL (Адрес проверки) ga qo'yasiz.
        name="accept_click_requests",
    ),
]
