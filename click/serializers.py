from rest_framework import serializers

from .models import TRANSACTIONTYPECHOICES


class InitializePaymentSerializer(serializers.Serializer):
    transaction_type = serializers.ChoiceField(
        choices=TRANSACTIONTYPECHOICES.choices,
    )
    price = serializers.DecimalField(max_digits=20, decimal_places=2)

