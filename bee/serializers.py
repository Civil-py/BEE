# serializers.py
from rest_framework import serializers
from .models import EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinancialInformation, NetProfit_ED_ESD, FinacialSkillsDevelopment, Valuation

class EmploymentEquitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentEquity
        fields = '__all__'

class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'


class SkillsDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsDevelopment
        fields = '__all__'

class OwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownership
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class SocioEconomicDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocioEconomicDevelopment
        fields = '__all__'


class FinancialInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInformation
        fields = '__all__'


class FinacialSkillsDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinacialSkillsDevelopment
        fields = '__all__'


class NetProfit_ED_ESDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetProfit_ED_ESD
        fields = '__all__'


class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = '__all__'

# Repeat similarly for other models
