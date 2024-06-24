from django.forms import ModelForm
from django import forms
from .models import User, BeeUsers, EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinacialSkillsDevelopment, FinancialInformation, NetProfit_ED_ESD
class UserForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = BeeUsers
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        bee_user = super().save(commit=False)
        bee_user.user = user
        if commit:
            bee_user.save()
            self.save_m2m()
        return bee_user


class EmploymentEquityForm(forms.ModelForm):

    class Meta:
        model = EmploymentEquity
        fields = '__all__'

class ProcurementForm(forms.ModelForm):

    class Meta:
        model = Procurement
        fields = '__all__'


class SkillsDevelopmentForm(forms.ModelForm):

    class Meta:
        model = SkillsDevelopment
        fields = '__all__'



class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = '__all__'


class OwnershipForm(forms.ModelForm):

    class Meta:
        model = Ownership
        fields = '__all__'


class SocioEconomicDevelopmentForm(forms.ModelForm):

    class Meta:
        model = SocioEconomicDevelopment
        fields = '__all__'


class FinacialSkillsDevelopmentForm(forms.ModelForm):

    class Meta:
        model = FinacialSkillsDevelopment
        fields = '__all__'

class FinacialInformationForm(forms.ModelForm):

    class Meta:
        model = FinancialInformation
        fields = '__all__'

class NetProfit_ED_ESDForm(forms.ModelForm):

    class Meta:
        model = NetProfit_ED_ESD
        fields = '__all__'



