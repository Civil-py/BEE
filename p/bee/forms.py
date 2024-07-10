from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User, BeeUsers, EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinacialSkillsDevelopment, FinancialInformation, NetProfit_ED_ESD, Valuation

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
        widgets = {'Name': forms.TextInput(attrs={'class': 'form-control'}),
                   'ID': forms.HiddenInput(),
                   'Ingest_date': forms.HiddenInput(),
                   'Table_Name': forms.HiddenInput(),
                   'Surname': forms.TextInput(attrs={'class': 'form-control'}),
                   'Id_Number': forms.TextInput(attrs={'class': 'form-control'}),
                   'Job_title': forms.TextInput(attrs={'class': 'form-control'}),
                   'Gross_Monthly_Salary': forms.TextInput(attrs={'class': 'form-control'}),
                   'Race': forms.Select(attrs={'class': 'form-control'}),
                    'Gender': forms.Select(attrs={'class': 'form-control'}),
                    'Disabled': forms.Select(attrs={'class': 'form-control'}),
                    'Description_of_disability': forms.TextInput(attrs={'class': 'form-control'}),
                    'Occupational_Level': forms.Select(attrs={'class': 'form-control'}),
                    'Foreign':forms.Select(attrs={'class': 'form-control'}),
                    'Pilot': forms.Select(attrs={'class': 'form-control'}),
                    'Technician': forms.Select(attrs={'class': 'form-control'}),
                   'Black_Youth' : forms.Select(attrs={'class': 'form-control'})}


    def __init__(self, *args, **kwargs):
        super(EmploymentEquityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # # Customize field labels
        # self.fields['Name'].label = 'Name'
        # self.fields['surname'].label = 'Surname'
        self.fields['Id_Number'].label = 'ID Number'
        self.fields['Gross_Monthly_Salary'].label = 'Gross Monthly Salary (R)'
        # self.fields['race'].label = 'Race'
        # self.fields['gender'].label = 'Gender'
        # self.fields['disabled'].label = 'Disabled'
        # self.fields['description_of_disability'].label = 'Description Of Disability'
        # self.fields['occupational_level'].label = 'Occupational Level'
        # self.fields['foreign'].label = 'Foreign'
        # self.fields['pilot'].label = 'Pilot'
        # self.fields['technician'].label = 'Technician'
        self.fields[
            'Black_Youth'].label = 'Black Youth (as defined by the National Youth Commission Act of 1996)'




class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'
        widgets = {
            'supplier_name': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_no': forms.TextInput(attrs={'class': 'form-control'}),
            'expenditure_per_supplier_ledger_for_the_period_including_vat': forms.TextInput(attrs={'class': 'form-control'}),
            'expenditure_excluding_vat': forms.TextInput(attrs={'class': 'form-control'}),
            'non_vat_item': forms.Select(attrs={'class': 'form-control'}),
            'supplier_classification': forms.Select(attrs={'class': 'form-control'}),
            'bee_level': forms.Select(attrs={'class': 'form-control'}),
            'fifty_one_percent_or_more_black_owned': forms.Select(attrs={'class': 'form-control'}),
            'black_ownership_percent': forms.TextInput(attrs={'class': 'form-control'}),
            'thirty_percent_or_more_black_woman_owned': forms.Select(attrs={'class': 'form-control'}),
            'black_woman_ownership': forms.TextInput(attrs={'class': 'form-control'}),
            'empowering_supplier': forms.Select(attrs={'class': 'form-control'}),
            'esd_recipient_and_black_owned_qse_or_eme_min_three_year_contract': forms.Select(attrs={'class': 'form-control'}),
            'designated_group_supplier': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcurementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['supplier_name'].label = 'Supplier Name'
        self.fields['reg_no'].label = 'Registration Number'
        self.fields['expenditure_per_supplier_ledger_for_the_period_including_vat'].label = 'Expenditure per Supplier Ledger (including VAT)'
        self.fields['expenditure_excluding_vat'].label = 'Expenditure (excluding VAT)'
        self.fields['non_vat_item'].label = 'Non-VAT Item'
        self.fields['supplier_classification'].label = 'Supplier Classification'
        self.fields['bee_level'].label = 'BEE Level'
        self.fields['fifty_one_percent_or_more_black_owned'].label = '51% or More Black Owned'
        self.fields['black_ownership_percent'].label = 'Black Ownership Percentage'
        self.fields['thirty_percent_or_more_black_woman_owned'].label = '30% or More Black Woman Owned'
        self.fields['black_woman_ownership'].label = 'Black Woman Ownership'
        self.fields['empowering_supplier'].label = 'Empowering Supplier'
        self.fields['esd_recipient_and_black_owned_qse_or_eme_min_three_year_contract'].label = 'ESD Recipient and Black Owned QSE/EME (Minimum Three Year Contract)'
        self.fields['designated_group_supplier'].label = 'Designated Group Supplier'


class SkillsDevelopmentForm(forms.ModelForm):
    class Meta:
        model = SkillsDevelopment
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),

            'race': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'disabled': forms.Select(attrs={'class': 'form-control'}),
            'training_course': forms.TextInput(attrs={'class': 'form-control'}),
            'trainer_or_service_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'internal_training': forms.Select(attrs={'class': 'form-control'}),
            'abet': forms.Select(attrs={'class': 'form-control'}),
            'abet_level': forms.Select(attrs={'class': 'form-control'}),
            'core_and_or_critical_skills': forms.Select(attrs={'class': 'form-control'}),
            'direct_expenditure_for_period_excl_vat': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_expenditure_for_the_period': forms.TextInput(attrs={'class': 'form-control'}),
            'total_expenditure': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_to_company_annual_salary_for_b_c_d_students': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_of_training_in_hours_for_internal_training': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_to_company_annual_salary_for_internal_trainers_category_g': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_participants_on_training_course_category_g': forms.TextInput(attrs={'class': 'form-control'}),
            'designated_groups': forms.Select(attrs={'class': 'form-control'}),
            'passed_qualifying_examinations': forms.Select(attrs={'class': 'form-control'}),
            'spare': forms.Select(attrs={'class': 'form-control'}),
            'unemployed_learner': forms.Select(attrs={'class': 'form-control'}),
            'absorbed_learner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SkillsDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['name_and_surname'].label = 'Name And Surname'
        self.fields['id_number'].label = 'ID Number'

        self.fields['race'].label = 'Race'
        self.fields['gender'].label = 'Gender'
        self.fields['disabled'].label = 'Disabled'
        self.fields['training_course'].label = 'Training Course'
        self.fields['trainer_or_service_provider'].label = 'Trainer or Service Provider'
        self.fields['category'].label = 'Category'
        self.fields['internal_training'].label = 'Internal Training'
        self.fields['abet'].label = 'ABET'
        self.fields['abet_level'].label = 'ABET Level'
        self.fields['core_and_or_critical_skills'].label = 'Core and/or Critical Skills'
        self.fields['direct_expenditure_for_period_excl_vat'].label = 'Direct Expenditure for Period (Excl. VAT)'
        self.fields['additional_expenditure_for_the_period'].label = 'Additional Expenditure for the Period'
        self.fields['total_expenditure'].label = 'Total Expenditure'
        self.fields['cost_to_company_annual_salary_for_b_c_d_students'].label = 'Cost to Company Annual Salary for B/C/D Students'
        self.fields['duration_of_training_in_hours_for_internal_training'].label = 'Duration of Training (in hours) for Internal Training'
        self.fields['cost_to_company_annual_salary_for_internal_trainers_category_g'].label = 'Cost to Company Annual Salary for Internal Trainers (Category G)'
        self.fields['number_of_participants_on_training_course_category_g'].label = 'Number of Participants on Training Course (Category G)'
        self.fields['designated_groups'].label = 'Designated Groups'
        self.fields['passed_qualifying_examinations'].label = 'Passed Qualifying Examinations'
        self.fields['spare'].label = 'Spare'
        self.fields['unemployed_learner'].label = 'Unemployed Learner'
        self.fields['absorbed_learner'].label = 'Absorbed Learner'


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

        self.fields['name_and_surname'].label = 'Name And Surname'
        self.fields['gender'].label = 'Gender'
        self.fields['disabled'].label = 'Disabled'
        self.fields['id_number'].label = 'ID Number'
        self.fields['job_title'].label = 'Job Title'
        self.fields['voting_rights'].label = 'Voting Rights'
        self.fields['executive_director'].label = 'Executive Director'
        self.fields['race'].label = 'Race'
        self.fields['independent_non_Executive'].label = 'Independent Non-Executive'

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        fields = '__all__'
        widgets = {
            'name_and_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'race': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'disabled': forms.Select(attrs={'class': 'form-control'}),
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

        # Customize field labels
        self.fields['name_and_surname'].label = 'Name And Surname'
        self.fields['id_number'].label = 'ID Number'
        self.fields['race'].label = 'Race'
        self.fields['gender'].label = 'Gender'
        self.fields['disabled'].label = 'Disabled'
        self.fields['foreign'].label = 'Foreign'
        self.fields['designated_groups'].label = 'Designated Groups'
        self.fields['youth'].label = 'Youth'
        self.fields['unemployed'].label = 'Unemployed'
        self.fields['living_in_rural_areas'].label = 'Living in Rural Areas'
        self.fields['military_veteran'].label = 'Military Veteran'
        self.fields['economic_interest'].label = 'Economic Interest'
        self.fields['voting_rights'].label = 'Voting Rights'
        self.fields['chartered_accountant'].label = 'Chartered Accountant'
        self.fields['outstanding_debt_by_black_participants'].label = 'Outstanding Debt by Black Participants'
        self.fields['ownership_model'].label = 'Ownership Model'


class SocioEconomicDevelopmentForm(forms.ModelForm):
    class Meta:
        model = SocioEconomicDevelopment
        fields = '__all__'
        widgets = {
            'ID': forms.HiddenInput(),
            'Ingest_date': forms.HiddenInput(),
            'Table_Name': forms.HiddenInput(),
            'Beneficiary': forms.TextInput(attrs={'class': 'form-control'}),
            'ICT_Sector_Initiative': forms.Select(attrs={'class': 'form-control'}),
            'Percentage_of_Black_participation': forms.TextInput(attrs={'class': 'form-control'}),
            'Contribution_Type': forms.Select(attrs={'class': 'form-control'}),
            'Description_of_Contribution': forms.TextInput(attrs={'class': 'form-control'}),
            'Structured_SED_Project': forms.Select(attrs={'class': 'form-control'}),
            'Date_of_Contribution': forms.TextInput(attrs={'class': 'form-control'}),
            'Amount_of_Contribution': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SocioEconomicDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        # self.fields['beneficiary'].label = 'Beneficiary'
        # self.fields['ict_sector_initiative'].label = 'ICT Sector Initiative'
        self.fields['Percentage_of_Black_participation'].label = 'Black Participation %'
        # self.fields['contribution_type'].label = 'Contribution Type'
        # self.fields['description_of_contribution'].label = 'Description of Contribution'
        # self.fields['structured_sed_project'].label = 'Structured SED Project'
        # self.fields['date_of_contribution'].label = 'Date of Contribution'
        # self.fields['amount_of_contribution'].label = 'Amount of Contribution'


class FinacialSkillsDevelopmentForm(forms.ModelForm):
    class Meta:
        model = FinacialSkillsDevelopment
        fields = '__all__'
        widgets = {
            'finacial_period': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.TextInput(attrs={'class': 'form-control'}),
            'sdl_payments_made_per_emp201': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FinacialSkillsDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['finacial_period'].label = 'Financial Period'
        self.fields['month'].label = 'Month'
        self.fields['sdl_payments_made_per_emp201'].label = 'SDL Payments Made per EMP201'


class FinacialInformationForm(forms.ModelForm):
    class Meta:
        model = FinancialInformation
        fields = '__all__'
        widgets = {
            'financial_period': forms.TextInput(attrs={'class': 'form-control'}),
            'turnover_revenue': forms.TextInput(attrs={'class': 'form-control'}),
            'nett_profit_before_tax': forms.TextInput(attrs={'class': 'form-control'}),
            'nett_profit_after_tax': forms.TextInput(attrs={'class': 'form-control'}),
            'salaries': forms.TextInput(attrs={'class': 'form-control'}),
            'directors_members_emoluments': forms.TextInput(attrs={'class': 'form-control'}),
            'annual_payroll': forms.TextInput(attrs={'class': 'form-control'}),
            'expenses': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_of_sales_purchases_only': forms.TextInput(attrs={'class': 'form-control'}),
            'additions_capex_for_the_year': forms.TextInput(attrs={'class': 'form-control'}),
            'depreciation_for_the_year': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FinacialInformationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['financial_period'].label = 'Financial Period'
        self.fields['turnover_revenue'].label = 'Turnover Revenue'
        self.fields['nett_profit_before_tax'].label = 'Nett Profit Before Tax'
        self.fields['nett_profit_after_tax'].label = 'Nett Profit After Tax'
        self.fields['salaries'].label = 'Salaries'
        self.fields['directors_members_emoluments'].label = 'Directors/Members Emoluments'
        self.fields['annual_payroll'].label = 'Annual Payroll'
        self.fields['expenses'].label = 'Expenses'
        self.fields['cost_of_sales_purchases_only'].label = 'Cost of Sales/Purchases Only'
        self.fields['additions_capex_for_the_year'].label = 'Additions Capex for the Year'
        self.fields['depreciation_for_the_year'].label = 'Depreciation for the Year'

class NetProfit_ED_ESDForm(forms.ModelForm):
    class Meta:
        model = NetProfit_ED_ESD
        fields = '__all__'
        widgets = {'finacial_period': forms.TextInput(attrs={'class': 'form-control'}),
                   'npat': forms.TextInput(attrs={'class': 'form-control'}),
                   'projected': forms.TextInput(attrs={'class': 'form-control'}),
                   'ed': forms.TextInput(attrs={'class': 'form-control'}),
                   'sd': forms.TextInput(attrs={'class': 'form-control'}),
                   'sed': forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super(NetProfit_ED_ESDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['finacial_period'].label = 'Financial Period'
        self.fields['sed'].label = 'SED'
        self.fields['ed'].label = 'ED'
        self.fields['sd'].label = 'SD'



class ValuationForm(forms.ModelForm):
    class Meta:
        model = Valuation
        fields = '__all__'
        widgets = {'valuation_method': forms.TextInput(attrs={'class': 'form-control'}),
                   'formal_valuation_if_available': forms.TextInput(attrs={'class': 'form-control'}),
                   'total_assets': forms.TextInput(attrs={'class': 'form-control'}),
                   'total_liabilities': forms.TextInput(attrs={'class': 'form-control'}),
                   'nett_asset_value_per_afs': forms.TextInput(attrs={'class': 'form-control'}),
                   'finacial_period': forms.TextInput(attrs={'class': 'form-control'}),
                   'month': forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super(ValuationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['finacial_period'].label = 'Financial Period'
        self.fields['valuation_method'].label = 'Valuation Method'
        self.fields['formal_valuation_if_available'].label = 'Formal Valuation If Available'
        self.fields['total_assets'].label = 'Total Assets'
        self.fields['total_liabilities'].label = 'Total Liabilities'
        self.fields['nett_asset_value_per_afs'].label = 'Nett Asset Value per afs'
