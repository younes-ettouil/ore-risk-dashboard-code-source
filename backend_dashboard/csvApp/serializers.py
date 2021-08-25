from rest_framework import serializers
from .models import *

class npv_totalserializer(serializers.ModelSerializer):

    class Meta:
        model= npv_total
        fields='__all__'

class npv_Counterpartyserializer(serializers.ModelSerializer):

    class Meta:
        model= npv_Counterparty
        fields='__all__'

class datesSeerializer(serializers.ModelSerializer):
    class Meta:
        model= dates
        fields= '__all__'

class npv_netingsetSeerializer(serializers.ModelSerializer):
    class Meta:
        model= npv_nettingset
        fields= '__all__'

class npv_tradeSeerializer(serializers.ModelSerializer):
    class Meta:
        model= npv_trade
        fields= '__all__'

class npv_creditratingSeerializer(serializers.ModelSerializer):
    class Meta:
        model= npv_creditrating
        fields= '__all__'
#========================================
class xpv_totalSeerializer(serializers.ModelSerializer):
    class Meta:
        model= xpv_total
        fields= '__all__'

class exposeurTotalSeerializer(serializers.ModelSerializer):
    class Meta:
        model= exposeur_total
        fields= '__all__'
class xpvNettingsetSeerializer(serializers.ModelSerializer):
    class Meta:
        model= xpv_nettingset
        fields= '__all__'

class xpvcreditratingSeerializer(serializers.ModelSerializer):
    class Meta:
        model= xpv_creditrating
        fields= '__all__'
class xpvCounterpartySeerializer(serializers.ModelSerializer):
    class Meta:
        model= xpv_counterparty
        fields= '__all__'


class LIMITS_TOSeerializer(serializers.ModelSerializer):
    class Meta:
        model= Limits_Total
        fields= '__all__'
class limits_CRSeerializer(serializers.ModelSerializer):
    class Meta:
        model= Limits_CreditRating
        fields= '__all__'
class limits_CPSeerializer(serializers.ModelSerializer):
    class Meta:
        model= Limits_Counterparty
        fields= '__all__'
class limits_NSSeerializer(serializers.ModelSerializer):
    class Meta:
        model= Limits_Nettingset
        fields= '__all__'
class limits_TrSeerializer(serializers.ModelSerializer):
    class Meta:
        model= Limits_Trade
        fields= '__all__'

class alldata_TrSeerializer(serializers.ModelSerializer):
    class Meta:
        model= alldata
        fields= '__all__'

class alldata2_TrSeerializer(serializers.ModelSerializer):
    class Meta:
        model= alldata2
        fields= '__all__'