from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RACE_TYPES = [
    ('African', 'African'),
    ('Indian', 'Indian'),
('Coloured', 'Coloured'),
('Non-Black', 'Non-Black')
]

ABET_LEVELS = [
    ('1', '1'),
    ('2', '2'),
('3', '3'),
('4', '4')
]


BEE_LEVELS = [
    ('1', '1'),
    ('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
    ('6', '6'),
('7', '7'),
('8', '8'),
('Non Compliant', 'Non Compliant'),
]


CATEGORIES = [
    ('A', 'A'),
    ('A2', 'A2'),
('B', 'B'),
('C', 'C'),
('D', 'D'),
('E', 'E'),
('F', 'F'),
('G', 'G'),
('MST', 'MST'),


]

OCCUPATIONAL_LEVEL = [
    ('Junior Management', 'Junior Management'),
    ('Middle Management', 'Middle Management'),
('Senior Management', 'Senior Management'),
('Executive Management', 'Executive Management'),
('Other Executive Management', ' Other Executive Management'),
('Semi-Skilled', 'Semi-Skilled'),
]

GENDER_TYPES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

CONTRIBUTION_TYPES = [
    ('Direct Cost', 'Direct Cost'),
    ('Non-Monetary', 'Non-Monetary'),
]

SUPPLIER_CLASSIFICATION = [
    ('Generic', 'Generic'),
('QSE', 'QSE'),
    ('EME', 'EME'),
]



YES_NO = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

class BeeUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'No User'}"

class EmploymentEquity(models.Model):
    Table_Name = models.CharField(null=True, max_length=64)
    ID = models.CharField(max_length=64, primary_key=True)
    Name = models.CharField(max_length=64, null=True)
    Surname = models.CharField(max_length=64, null=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Id_Number = models.IntegerField(null=True, blank=True, unique=True)
    Job_title = models.CharField(max_length=64,null=True)
    Race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    Gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    Disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    Gross_Monthly_Salary = models.FloatField(null=True, blank=True, unique=True)
    Description_of_disability = models.CharField(max_length=150, null=True)
    Occupational_Level =  models.CharField(max_length=64, null=True, choices=OCCUPATIONAL_LEVEL)
    Foreign = models.CharField(max_length=64, null=True, choices=YES_NO)
    Pilot = models.CharField(max_length=64, null=True, choices=YES_NO)
    Technician = models.CharField(max_length=64, null=True, choices=YES_NO)
    Black_Youth = models.CharField(max_length=64, null=True, choices=YES_NO)



class Board(models.Model):
    name_and_surname = models.CharField(max_length=64, null=True)
    id_number = models.IntegerField(null=True, blank=True, unique=True)
    race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    job_title = models.CharField(max_length=64, null=True)
    voting_rights = models.CharField(max_length=64, null=True, choices=YES_NO)
    executive_director = models.CharField(max_length=64, null=True, choices=YES_NO)
    independent_non_Executive = models.CharField(max_length=64, null=True, choices=YES_NO)




class SkillsDevelopment(models.Model):
    name_and_surname = models.CharField(max_length=64, null=True)
    id_number = models.IntegerField(null=True, blank=True, unique=True)
    race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    training_course = models.CharField(max_length=64, null=True)
    trainer_or_service_provider = models.CharField(max_length=64, null=True)
    category = models.CharField(max_length=64, null=True, choices=CATEGORIES)
    internal_training =  models.CharField(max_length=64, null=True, choices=YES_NO)
    abet = models.CharField(max_length=64, null=True, choices=YES_NO)
    abet_level = models.CharField(max_length=64, null=True, choices=ABET_LEVELS)
    core_and_or_critical_skills = models.CharField(max_length=64, null=True, choices=YES_NO)
    direct_expenditure_for_period_excl_vat = models.FloatField(null=True, blank=True)
    additional_expenditure_for_the_period = models.FloatField(null=True, blank=True)
    total_expenditure = models.FloatField(null=True, blank=True)
    cost_to_company_annual_salary_for_b_c_d_students = models.FloatField(null=True, blank=True)
    duration_of_training_in_hours_for_internal_training = models.FloatField(null=True, blank=True)
    cost_to_company_annual_salary_for_internal_trainers_category_g = models.FloatField(null=True, blank=True)
    number_of_participants_on_training_course_category_g = models.IntegerField(null=True, blank=True)
    designated_groups = models.CharField(max_length=64, null=True, choices=YES_NO)
    passed_qualifying_examinations = models.CharField(max_length=64, null=True, choices=YES_NO)
    spare = models.CharField(max_length=64, null=True, choices=YES_NO)
    unemployed_learner = models.CharField(max_length=64, null=True, choices=YES_NO)
    absorbed_learner = models.CharField(max_length=64, null=True, choices=YES_NO)



class Ownership(models.Model):
    name_and_surname = models.CharField(max_length=64, null=True)
    id_number = models.IntegerField(null=True, blank=True, unique=True)
    race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    foreign = models.CharField(max_length=64, null=True, choices=YES_NO)
    designated_groups = models.CharField(max_length=64, null=True, choices=YES_NO)
    youth = models.CharField(max_length=64, null=True, choices=YES_NO)
    unemployed = models.CharField(max_length=64, null=True, choices=YES_NO)
    living_in_rural_areas = models.CharField(max_length=64, null=True, choices=YES_NO)
    military_veteran = models.CharField(max_length=64, null=True, choices=YES_NO)
    economic_interest = models.CharField(max_length=64, null=True, choices=YES_NO)
    voting_rights = models.CharField(max_length=64, null=True, choices=YES_NO)
    chartered_accountant = models.CharField(max_length=64, null=True, choices=YES_NO)
    outstanding_debt_by_black_participants = models.FloatField(null=True, blank=True)
    ownership_model = models.CharField(max_length=64, null=True)


class Procurement(models.Model):
    supplier_name = models.CharField(max_length=64, null=True)
    reg_no = models.IntegerField(null=True, blank=True, unique=True)
    expenditure_per_supplier_ledger_for_the_period_including_vat = models.FloatField(null=True, blank=True)
    expenditure_excluding_vat = models.FloatField(null=True, blank=True)
    non_vat_item = models.CharField(max_length=64, null=True, choices=YES_NO)
    supplier_classification = models.CharField(max_length=64, null=True, choices=SUPPLIER_CLASSIFICATION)
    bee_level = models.CharField(max_length=64, null=True, choices=BEE_LEVELS)
    fifty_one_percent_or_more_black_owned = models.CharField(max_length=64, null=True, choices=YES_NO)
    black_ownership_percent =  models.FloatField(null=True, blank=True)
    thirty_percent_or_more_black_woman_owned = models.CharField(max_length=64, null=True, choices=YES_NO)
    black_woman_ownership = models.FloatField(null=True, blank=True)
    empowering_supplier = models.CharField(max_length=64, null=True, choices=YES_NO)
    esd_recipient_and_black_owned_qse_or_eme_min_three_year_contract = models.CharField(max_length=64, null=True, choices=YES_NO)
    designated_group_supplier = models.CharField(max_length=64, null=True, choices=YES_NO)


class SocioEconomicDevelopment(models.Model):
    Table_Name = models.CharField(null=True, max_length=64)
    ID = models.CharField(max_length=64, primary_key=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Beneficiary = models.CharField(max_length=64, null=True)
    ICT_Sector_Initiative = models.CharField(max_length=64, null=True, choices=YES_NO)
    Percentage_of_Black_participation = models.FloatField(null=True, blank=True)
    Contribution_Type = models.CharField(max_length=64, null=True, choices=CONTRIBUTION_TYPES)
    Description_of_Contribution = models.CharField(max_length=64, null=True)
    Structured_SED_Project = models.CharField(max_length=64, null=True, choices=YES_NO)
    Date_of_Contribution = models.DateField(null=True)
    Amount_of_Contribution = models.FloatField(null=True, blank=True)




class FinancialInformation(models.Model):
    financial_period = models.CharField(max_length=64, null=True)
    turnover_revenue = models.FloatField(null=True, blank=True)
    nett_profit_before_tax = models.FloatField(null=True, blank=True)
    nett_profit_after_tax = models.FloatField(null=True, blank=True)
    salaries = models.FloatField(null=True, blank=True)
    directors_members_emoluments = models.FloatField(null=True, blank=True)
    annual_payroll = models.FloatField(null=True, blank=True)
    expenses = models.FloatField(null=True, blank=True)
    cost_of_sales_purchases_only = models.FloatField(null=True, blank=True)
    additions_capex_for_the_year =  models.FloatField(null=True, blank=True)
    depreciation_for_the_year = models.FloatField(null=True, blank=True)




class Valuation(models.Model):
    valuation_method = models.CharField(max_length=64, null=True)
    formal_valuation_if_available = models.FloatField(null=True, blank=True)
    total_assets = models.FloatField(null=True, blank=True)
    total_liabilities = models.FloatField(null=True, blank=True)
    nett_asset_value_per_afs = models.FloatField(null=True, blank=True)
    finacial_period = models.CharField(max_length=64, null=True)
    month = models.IntegerField(null=True, blank=True)


class FinacialSkillsDevelopment(models.Model):
    finacial_period = models.CharField(max_length=64, null=True)
    month = models.IntegerField(null=True, blank=True)
    sdl_payments_made_per_emp201 = models.FloatField(null=True, blank=True)


class NetProfit_ED_ESD(models.Model):
    finacial_period = models.CharField(max_length=64, null=True)
    npat = models.FloatField(null=True, blank=True)
    projected = models.FloatField(null=True, blank=True)
    ed = models.FloatField(null=True, blank=True)
    sd = models.FloatField(null=True, blank=True)
    sed = models.FloatField(null=True, blank=True)













































