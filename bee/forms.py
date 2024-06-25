from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User, BeeUsers, EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinacialSkillsDevelopment, FinancialInformation, NetProfit_ED_ESD

class UserForm(forms.ModelForm):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = BeeUsers
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),}
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

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
        widgets = {'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
                   'id_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'job_title': forms.TextInput(attrs={'class': 'form-control'}),
                   'race': forms.Select(attrs={'class': 'form-control'}),
                    'gender': forms.Select(attrs={'class': 'form-control'}),
                    'disabled': forms.Select(attrs={'class': 'form-control'}),
                    'description_of_disability': forms.TextInput(attrs={'class': 'form-control'}),
                    'occupational_level': forms.Select(attrs={'class': 'form-control'}),
                    'foreign':forms.Select(attrs={'class': 'form-control'}),
                    'pilot': forms.Select(attrs={'class': 'form-control'}),
                    'technician': forms.Select(attrs={'class': 'form-control'}),
                   'black_youth_as_defined_by_the_national_youth_commission_act_of_1996' : forms.Select(attrs={'class': 'form-control'})}


    def __init__(self, *args, **kwargs):
        super(EmploymentEquityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))




class ProcurementForm(forms.ModelForm):

    class Meta:
        model = Procurement
        fields = '__all__'
        widgets = {'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'reg_no':forms.TextInput(attrs={'class': 'form-control'}),
                   'expenditure_per_supplier_ledger_for_the_period_including_vat': forms.TextInput(attrs={'class': 'form-control'}),
                   'expenditure_excluding_vat': forms.TextInput(attrs={'class': 'form-control'}),
                   'non_vat_item': forms.Select(attrs={'class': 'form-control'}),
                   'supplier_classification': forms.Select(attrs={'class': 'form-control'}),
                   'bee_level': forms.Select(attrs={'class': 'form-control'}),
                   'fifty_one_percent_or_more_black_owned': forms.Select(attrs={'class': 'form-control'}),
                   'black_ownership_percent': forms.TextInput(attrs={'class': 'form-control'}),
                   'thirty_percent_or_more_black_woman_owned' : forms.Select(attrs={'class' : 'form-control'}),
                    'black_woman_ownership' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'empowering_supplier': forms.Select(attrs={'class' : 'form-control'}),
                  'esd_recipient_and_black_owned_qse_or_eme_min_three_year_contract' : forms.Select(attrs={'class' : 'form-control'}),
                 'designated_group_supplier' : forms.Select(attrs={'class' : 'form-control'})}







        def __init__(self, *args, **kwargs):
          super(ProcurementForm, self).__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_method = 'post'
          self.helper.add_input(Submit('submit', 'Submit'))

class SkillsDevelopmentForm(forms.ModelForm):

    class Meta:
        model = SkillsDevelopment
        fields = '__all__'
        widgets = {'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
                  'id_number': forms.TextInput(attrs={'class': 'form-control'}),
                  'job_title': forms.TextInput(attrs={'class': 'form-control'}),
                  'race': forms.Select(attrs={'class': 'form-control'}),
                  'gender': forms.Select(attrs={'class': 'form-control'}),
                  'disabled': forms.Select(attrs={'class': 'form-control'}),
                  'training_course': forms.TextInput(attrs={'class' : 'form-control'}),
                  'trainer_or_service_provider' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'category' : forms.Select(attrs={'class' : 'form-control'}),
                  'internal_training' : forms.Select(attrs={'class' : 'form-control'}),
                  'abet' : forms.Select(attrs={'class' : 'form-control'}),
                  'abet_level' : forms.Select(attrs={'class' : 'form-control'}),
                  'core_and_or_critical_skills' : forms.Select(attrs={'class' : 'form-control'}),
                  'direct_expenditure_for_period_excl_vat' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'additional_expenditure_for_the_period' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'total_expenditure': forms.TextInput(attrs={'class' : 'form-control'}),
                  'cost_to_company_annual_salary_for_b_c_d_students' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'duration_of_training_in_hours_for_internal_training' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'cost_to_company_annual_salary_for_internal_trainers_category_g' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'number_of_participants_on_training_course_category_g' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'designated_groups' : forms.Select(attrs={'class' : 'form-control'}),
                  'passed_qualifying_examinations' : forms.Select(attrs={'class' : 'form-control'}),
                  'spare' : forms.Select(attrs={'class' : 'form-control'}),
                  'unemployed_learner' : forms.Select(attrs={'class' : 'form-control'}),
                  'absorbed_learner' : forms.Select(attrs={'class' : 'form-control'})}


    def __init__(self, *args, **kwargs):
        super(SkillsDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = '__all__'
        widgets = {'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
                  'id_number': forms.TextInput(attrs={'class': 'form-control'}),
                  'race': forms.Select(attrs={'class': 'form-control'}),
                  'gender': forms.Select(attrs={'class': 'form-control'}),
                  'disabled': forms.Select(attrs={'class': 'form-control'}),
                  'job_title': forms.TextInput(attrs={'class': 'form-control'}),
                  'voting_rights': forms.Select(attrs={'class': 'form-control'}),
                  'executive_director': forms.Select(attrs={'class': 'form-control'}),
                  'independent_non_Executive': forms.Select(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class OwnershipForm(forms.ModelForm):

    class Meta:
        model = Ownership
        fields = '__all__'
        widgets = {'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
                  'id_number': forms.TextInput(attrs={'class': 'form-control'}),
                  'race': forms.Select(attrs={'class': 'form-control'}),
                  'gender': forms.Select(attrs={'class': 'form-control'}),
                  'disabled': forms.Select(attrs={'class' : 'form-control'}),
                  'foreign': forms.Select(attrs={'class': 'form-control'}),
                  'designated_groups': forms.Select(attrs={'class': 'form-control'}),
                  'youth': forms.Select(attrs={'class': 'form-control'}),
                  'unemployed': forms.Select(attrs={'class': 'form-control'}),
                  'living_in_rural_areas': forms.Select(attrs={'class': 'form-control'}),
                  'military_veteran': forms.Select(attrs={'class': 'form-control'}),
                  'economic_interest': forms.Select(attrs={'class': 'form-control'}),
                  'voting_rights': forms.Select(attrs={'class': 'form-control'}),
                  'chartered_accountant': forms.Select(attrs={'class': 'form-control'}),
                  'outstanding_debt_by_black_participants': forms.TextInput(attrs={'class': 'form-control'}),
                  'ownership_model': forms.TextInput(attrs={'class': 'form-control'}),
                  }

    def __init__(self, *args, **kwargs):
        super(OwnershipForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class SocioEconomicDevelopmentForm(forms.ModelForm):

    class Meta:
        model = SocioEconomicDevelopment
        fields = '__all__'
        widget = {'beneficiary' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'ict_sector_initiative' :forms.Select(attrs={'class' : 'form-control'}),
                  'black_participation_percent' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'contribution_type' : forms.Select(attrs={'class' : 'form-control'}),
                  'description_of_contribution' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'structured_sed_project' : forms.Select(attrs={'class' : 'form-control'}),
                  'date_of_contribution' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'amount_of_contribution' : forms.TextInput(attrs={'class' : 'form-control'})}


    def __init__(self, *args, **kwargs):
        super(SocioEconomicDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class FinacialSkillsDevelopmentForm(forms.ModelForm):

    class Meta:
        model = FinacialSkillsDevelopment
        fields = '__all__'
        widgets = {'finacial_period' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'month' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'sdl_payments_made_per_emp201' : forms.TextInput(attrs={'class' : 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(FinacialSkillsDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class FinacialInformationForm(forms.ModelForm):

    class Meta:
        model = FinancialInformation
        fields = '__all__'
        widgets= {'financial_period' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'turnover_revenue' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'nett_profit_before_tax' : forms.TextInput(attrs={'class' : 'form-control'}),
                  'nett_profit_after_tax':  forms.TextInput(attrs={'class' : 'form-control'}),
                  'salaries': forms.TextInput(attrs={'class': 'form-control'}),
                  'directors_members_emoluments': forms.TextInput(attrs={'class': 'form-control'}),
                  'annual_payroll': forms.TextInput(attrs={'class': 'form-control'}),
                  'expenses': forms.TextInput(attrs={'class' : 'form-control'}),
                  'cost_of_sales_purchases_only': forms.TextInput(attrs={'class': 'form-control'}),
                  'additions_capex_for_the_year': forms.TextInput(attrs={'class': 'form-control'}),
                  'depreciation_for_the_year': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(FinacialInformationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
class NetProfit_ED_ESDForm(forms.ModelForm):

    class Meta:
        model = NetProfit_ED_ESD
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NetProfit_ED_ESDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
