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
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'ID': forms.HiddenInput(),
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Ingest_date': forms.HiddenInput(),
            'Table_Name': forms.HiddenInput(),
            'Createdby_user': forms.HiddenInput(),
            'Surname': forms.TextInput(attrs={'class': 'form-control'}),
            'Id_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'Gross_Monthly_Salary': forms.TextInput(attrs={'class': 'form-control'}),
            'Race': forms.Select(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Disabled': forms.Select(attrs={'class': 'form-control'}),
            'Description_of_disability': forms.TextInput(attrs={'class': 'form-control'}),
            'Occupational_Level': forms.Select(attrs={'class': 'form-control'}),
            'Foreign': forms.Select(attrs={'class': 'form-control'}),
            'Pilot': forms.Select(attrs={'class': 'form-control'}),
            'Technician': forms.Select(attrs={'class': 'form-control'}),
            'Black_Youth': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmploymentEquityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.fields['Id_Number'].label = 'ID Number'
        self.fields['Gross_Monthly_Salary'].label = 'Gross Monthly Salary (R)'
        self.fields['Black_Youth'].label = 'Black Youth (as defined by the National Youth Commission Act of 1996)'



class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'
        widgets = {
            'ID': forms.HiddenInput(),
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Company_Name': forms.HiddenInput(),
            'Ingest_date': forms.HiddenInput(),
            'Table_Name': forms.HiddenInput(),
            'Createdby_user': forms.HiddenInput(),
            'Modifiedby_user': forms.HiddenInput(),
            'Supplier_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Reg_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Expenditure_incl_VAT': forms.TextInput(attrs={'class': 'form-control'}),
            'Expenditure_excl_VAT': forms.TextInput(attrs={'class': 'form-control'}),
            'Non_Vat_Item': forms.Select(attrs={'class': 'form-control'}),
            'Supplier_Classification': forms.Select(attrs={'class': 'form-control'}),
            'BEE_Level': forms.Select(attrs={'class': 'form-control'}),
            'fifty_one_or_more_black_owned': forms.Select(attrs={'class': 'form-control'}),
            'Black_Ownership': forms.TextInput(attrs={'class': 'form-control'}),
            'thirty_or_more_black_woman_owned': forms.Select(attrs={'class': 'form-control'}),
            'Black_Woman_Ownership': forms.TextInput(attrs={'class': 'form-control'}),
            'Empowering_Supplier': forms.Select(attrs={'class': 'form-control'}),
            'ESD_Recipient_Black_Owned_QSE_EME': forms.Select(attrs={'class': 'form-control'}),
            'Designated_Group_Supplier': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcurementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['Supplier_Name'].label = 'Supplier Name'
        self.fields['Reg_No'].label = 'Registration Number'
        self.fields['Expenditure_incl_VAT'].label = 'Expenditure per Supplier Ledger (including VAT)'
        self.fields['Expenditure_excl_VAT'].label = 'Expenditure (excluding VAT)'
        self.fields['Non_Vat_Item'].label = 'Non-VAT Item'
        self.fields['Supplier_Classification'].label = 'Supplier Classification'
        self.fields['BEE_Level'].label = 'BEE Level'
        self.fields['Fifty_one_or_more_black_owned'].label = '51% or More Black Owned'
        self.fields['Black_Ownership'].label = 'Black Ownership %'
        self.fields['Thirty_or_more_black_woman_owned'].label = '30% or More Black Woman Owned'
        self.fields['Black_Woman_Ownership'].label = 'Black Woman Ownership'
        self.fields['Empowering_Supplier'].label = 'Empowering Supplier'
        self.fields['ESD_Recipient_Black_Owned_QSE_EME'].label = 'ESD Recipient and Black Owned QSE/EME (Minimum Three Year Contract)'
        self.fields['Designated_Group_Supplier'].label = 'Designated Group Supplier'


class SkillsDevelopmentForm(forms.ModelForm):
    class Meta:
        model = SkillsDevelopment
        fields = '__all__'
        widgets = {
            'ID': forms.HiddenInput(),
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Company_Name': forms.HiddenInput(),
            'Ingest_date': forms.HiddenInput(),
            'Table_Name': forms.HiddenInput(),
            'Createdby_user': forms.HiddenInput(),
            'Modifiedby_user': forms.HiddenInput(),
            'Learner_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Learner_Surname': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'End_Date': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_of_Training_Program': forms.TextInput(attrs={'class': 'form-control'}),

            'Race': forms.Select(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Disabled': forms.Select(attrs={'class': 'form-control'}),
            'Training_Course': forms.TextInput(attrs={'class': 'form-control'}),
            'Trainer_or_Service_Provider': forms.TextInput(attrs={'class': 'form-control'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'Internal_Training': forms.Select(attrs={'class': 'form-control'}),
            'ABET': forms.Select(attrs={'class': 'form-control'}),
            'ABET_Level': forms.Select(attrs={'class': 'form-control'}),
            'Core_and_Critical_Skills': forms.Select(attrs={'class': 'form-control'}),
            'Direct_Expenditure_for_Period_excl_VAT': forms.TextInput(attrs={'class': 'form-control'}),
            'Additional_Expenditure_for_the_period': forms.TextInput(attrs={'class': 'form-control'}),
            'Total_Expenditure': forms.TextInput(attrs={'class': 'form-control'}),
            'Cost_to_company_annual_salary_internal_trainers_CategoryG': forms.TextInput(attrs={'class': 'form-control'}),
            'Duration_of_training_for_Internal_Training': forms.TextInput(attrs={'class': 'form-control'}),
            'Cost_to_company': forms.TextInput(attrs={'class': 'form-control'}),
            'Number_of_Participants_on_Training_Course_CategoryG': forms.TextInput(attrs={'class': 'form-control'}),
            'Designated_Groups': forms.Select(attrs={'class': 'form-control'}),
            'Passed_Qualifying_Examinations': forms.Select(attrs={'class': 'form-control'}),
            'Spare': forms.Select(attrs={'class': 'form-control'}),
            'Unemployed_Learner': forms.Select(attrs={'class': 'form-control'}),
            'Absorbed_Learner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SkillsDevelopmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['Learner_Name'].label = 'Learner Name'
        self.fields['Learner_Surname'].label = 'Learner Surname'
        self.fields['ID_Number'].label = 'ID Number'
        self.fields['End_Date'].label = 'End Date (yyyy-mm-dd)'
        self.fields['Date_of_Training_Program'].label = 'Date of Training Program (yyyy-mm-dd)'
        self.fields['Race'].label = 'Race'
        self.fields['Gender'].label = 'Gender'
        self.fields['Disabled'].label = 'Disabled'
        self.fields['Training_Course'].label = 'Training Course'
        self.fields['Trainer_or_Service_Provider'].label = 'Trainer or Service Provider'
        self.fields['Category'].label = 'Category'
        self.fields['Internal_Training'].label = 'Internal Training'
        self.fields['ABET'].label = 'ABET'
        self.fields['ABET_Level'].label = 'ABET Level'
        self.fields['Core_and_Critical_Skills'].label = 'Core and/or Critical Skills'
        self.fields['Direct_Expenditure_for_Period_excl_VAT'].label = 'Direct Expenditure for Period (Excl. VAT)'
        self.fields['Additional_Expenditure_for_the_period'].label = 'Additional Expenditure for the Period'
        self.fields['Total_Expenditure'].label = 'Total Expenditure'
        self.fields['Cost_to_company'].label = 'Cost to Company Annual Salary for B/C/D Students'
        self.fields['Duration_of_training_for_Internal_Training'].label = 'Duration of Training (in hours) for Internal Training'
        self.fields['Cost_to_company_annual_salary_internal_trainers_CategoryG'].label = 'Cost to Company Annual Salary for Internal Trainers (Category G)'
        self.fields['Number_of_Participants_on_Training_Course_CategoryG'].label = 'Number of Participants on Training Course (Category G)'
        self.fields['Designated_Groups'].label = 'Designated Groups'
        self.fields['Passed_Qualifying_Examinations'].label = 'Passed Qualifying Examinations'
        self.fields['Spare'].label = 'Spare'
        self.fields['Unemployed_Learner'].label = 'Unemployed Learner'
        self.fields['Absorbed_Learner'].label = 'Absorbed Learner'


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = '__all__'
        widgets = {'Name': forms.TextInput(attrs={'class': 'form-control'}),
                   'ID': forms.HiddenInput(),
                   'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
                   # 'Company_Name': forms.HiddenInput(),
                   'Ingest_date': forms.HiddenInput(),
                   'Table_Name': forms.HiddenInput(),
                   'Createdby_user': forms.HiddenInput(),
                   'Modifiedby_user': forms.HiddenInput(),
                   'Surname': forms.TextInput(attrs={'class': 'form-control'}),
                  'ID_Number': forms.TextInput(attrs={'class': 'form-control'}),
                  'Race': forms.Select(attrs={'class': 'form-control'}),
                  'Gender': forms.Select(attrs={'class': 'form-control'}),
                  'Disabled': forms.Select(attrs={'class': 'form-control'}),
                  'Job_Title': forms.TextInput(attrs={'class': 'form-control'}),
                   'Position_Occupational_Level': forms.TextInput(attrs={'class': 'form-control'}),
                  'Voting_Rights': forms.Select(attrs={'class': 'form-control'}),
                  'Executive_Director': forms.Select(attrs={'class': 'form-control'}),
                  'Independent_Non_Executive': forms.Select(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        self.fields['Name'].label = 'Name'
        self.fields['Surname'].label = 'Surname'
        self.fields['Gender'].label = 'Gender'
        self.fields['Disabled'].label = 'Disabled'
        self.fields['ID_Number'].label = 'ID Number'
        self.fields['Job_Title'].label = 'Job Title'
        self.fields['Position_Occupational_Level'].label = 'Position Occupational Level'
        self.fields['Voting_Rights'].label = 'Voting Rights'
        self.fields['Executive_Director'].label = 'Executive Director'
        self.fields['Race'].label = 'Race'
        self.fields['Independent_Non_Executive'].label = 'Independent Non-Executive'

class OwnershipForm(forms.ModelForm):
    class Meta:
        model = Ownership
        fields = '__all__'
        widgets = {
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'ID': forms.HiddenInput(),
            # 'Company_Name': forms.HiddenInput(),
            'Ingest_date': forms.HiddenInput(),
            'Table_Name': forms.HiddenInput(),
            'Createdby_user': forms.HiddenInput(),
            'Modifiedby_user': forms.HiddenInput(),
            'Surname': forms.TextInput(attrs={'class': 'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'Race': forms.Select(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Disabled': forms.Select(attrs={'class': 'form-control'}),
            'New_Entrant': forms.Select(attrs={'class': 'form-control'}),
            'Foreign': forms.Select(attrs={'class': 'form-control'}),
            'Designated_Groups': forms.Select(attrs={'class': 'form-control'}),
            'Youth': forms.Select(attrs={'class': 'form-control'}),
            'Unemployed': forms.Select(attrs={'class': 'form-control'}),
            'Living_in_Rural_Areas': forms.Select(attrs={'class': 'form-control'}),
            'Military_Veteran': forms.Select(attrs={'class': 'form-control'}),
            'Economic_Interest': forms.Select(attrs={'class': 'form-control'}),
            'Voting_Rights': forms.Select(attrs={'class': 'form-control'}),
            'Chartered_Accountant': forms.Select(attrs={'class': 'form-control'}),
            'Outstanding_Debt_by_Black_Participants': forms.TextInput(attrs={'class': 'form-control'}),
            'Ownership_Type': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(OwnershipForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

        # Customize field labels
        self.fields['Surname'].label = 'Surname'
        self.fields['Name'].label = 'Name'
        self.fields['ID_Number'].label = 'ID Number'
        self.fields['Race'].label = 'Race'
        self.fields['Gender'].label = 'Gender'
        self.fields['Disabled'].label = 'Disabled'
        self.fields['Foreign'].label = 'Foreign'
        self.fields['Designated_Groups'].label = 'Designated Groups'
        self.fields['Youth'].label = 'Youth'
        self.fields['Unemployed'].label = 'Unemployed'
        self.fields['Living_in_Rural_Areas'].label = 'Living in Rural Areas'
        self.fields['Military_Veteran'].label = 'Military Veteran'
        self.fields['Economic_Interest'].label = 'Economic Interest'
        self.fields['Voting_Rights'].label = 'Voting Rights'
        self.fields['Chartered_Accountant'].label = 'Chartered Accountant'
        self.fields['Outstanding_Debt_by_Black_Participants'].label = 'Outstanding Debt by Black Participants'
        self.fields['Ownership_Type'].label = 'Ownership Model'


class SocioEconomicDevelopmentForm(forms.ModelForm):
    class Meta:
        model = SocioEconomicDevelopment
        fields = '__all__'
        widgets = {
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),

            'Createdby_user': forms.HiddenInput(),
            'Modifiedby_user': forms.HiddenInput(),
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
        self.fields['Date_of_Contribution'].label = 'Date of Contribution (yyyy-mm-dd)'
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
