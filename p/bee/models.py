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
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    ID = models.CharField(max_length=64, primary_key=True)
    Name = models.CharField(max_length=64, null=True)
    Surname = models.CharField(max_length=64, null=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Id_Number = models.CharField(null=True, max_length=64, blank=True)
    Job_title = models.CharField(max_length=64,null=True)
    Race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    Gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    Disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    Gross_Monthly_Salary = models.CharField(null=True, max_length=64, blank=True)
    Description_of_disability = models.CharField(max_length=150, null=True)
    Occupational_Level =  models.CharField(max_length=64, null=True, choices=OCCUPATIONAL_LEVEL)
    Foreign = models.CharField(max_length=64, null=True, choices=YES_NO)
    Pilot = models.CharField(max_length=64, null=True, choices=YES_NO)
    Technician = models.CharField(max_length=64, null=True, choices=YES_NO)
    Black_Youth = models.CharField(max_length=64, null=True, choices=YES_NO)
    Createdby_user = models.CharField(null=True, max_length=64, blank=True)




class Board(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)

    ID = models.CharField(max_length=64, primary_key=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Name = models.CharField(max_length=64, null=True)
    Surname = models.CharField(max_length=64, null=True)
    ID_Number = models.CharField(null=True, max_length=64, blank=True)
    Position_Occupational_Level = models.CharField(max_length=64, null=True)
    Race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    Gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    Disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    Job_Title = models.CharField(max_length=64, null=True)
    Voting_Rights = models.CharField(max_length=64, null=True, choices=YES_NO)
    Executive_Director = models.CharField(max_length=64, null=True, choices=YES_NO)
    Independent_Non_Executive = models.CharField(max_length=64, null=True, choices=YES_NO)

    Createdby_user = models.CharField(null=True, max_length=64, blank=True)
    Modifiedby_user = models.CharField(null=True, max_length=64, blank=True)



class SkillsDevelopment(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    ID = models.CharField(max_length=64, primary_key=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Learner_Name = models.CharField(max_length=64, null=True)
    Learner_Surname = models.CharField(max_length=64, null=True)

    ID_Number = models.CharField(null=True, max_length=64, blank=True)
    Race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    Gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    Disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    Training_Course = models.CharField(max_length=64, null=True)
    Trainer_or_Service_Provider = models.CharField(max_length=64, null=True)
    Category = models.CharField(max_length=64, null=True, choices=CATEGORIES)
    Internal_Training =  models.CharField(max_length=64, null=True, choices=YES_NO)
    ABET = models.CharField(max_length=64, null=True, choices=YES_NO)
    ABET_Level = models.CharField(max_length=64, null=True, choices=ABET_LEVELS)
    Core_and_Critical_Skills = models.CharField(max_length=64, null=True, choices=YES_NO)
    Direct_Expenditure_for_Period_excl_Vat = models.CharField(null=True, max_length=64, blank=True)
    Additional_Expenditure_for_the_period = models.CharField(null=True, max_length=64, blank=True)
    Total_Expenditure = models.CharField(null=True, max_length=64, blank=True)
    Cost_to_company_annual_salary_internal_trainers_CategoryG = models.CharField(null=True, max_length=64, blank=True)
    Duration_of_training_for_Internal_Training = models.CharField(null=True, max_length=64, blank=True)
    Cost_to_company= models.CharField(null=True, max_length=64, blank=True)
    Number_of_Participants_on_Training_Course_CategoryG = models.CharField(null=True, max_length=64, blank=True)
    Designated_Groups = models.CharField(max_length=64, null=True, choices=YES_NO)
    Passed_Qualifying_Examinations = models.CharField(max_length=64, null=True, choices=YES_NO)
    Spare = models.CharField(max_length=64, null=True, choices=YES_NO)
    Unemployed_Learner = models.CharField(max_length=64, null=True, choices=YES_NO)
    Absorbed_Learner = models.CharField(max_length=64, null=True, choices=YES_NO)

    Createdby_user = models.CharField(null=True, max_length=64, blank=True)
    Modifiedby_user = models.CharField(null=True, max_length=64, blank=True)



class Ownership(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    ID = models.CharField(max_length=64, primary_key=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Name = models.CharField(max_length=64, null=True)
    Surname = models.CharField(max_length=64, null=True)
    ID_Number = models.CharField(null=True, max_length=64, blank=True)
    Race = models.CharField(max_length=64, null=True, choices=RACE_TYPES)
    Gender = models.CharField(max_length=64, null=True, choices=GENDER_TYPES)
    Disabled = models.CharField(max_length=64, null=True, choices=YES_NO)
    Foreign = models.CharField(max_length=64, null=True, choices=YES_NO)
    New_Entrant = models.CharField(max_length=64, null=True, choices=YES_NO)
    Designated_Groups = models.CharField(max_length=64, null=True, choices=YES_NO)
    Youth = models.CharField(max_length=64, null=True, choices=YES_NO)
    Unemployed = models.CharField(max_length=64, null=True, choices=YES_NO)
    Living_in_Rural_Areas = models.CharField(max_length=64, null=True, choices=YES_NO)
    Military_Veteran = models.CharField(max_length=64, null=True, choices=YES_NO)
    Economic_Interest = models.CharField(max_length=64, null=True, choices=YES_NO)
    Voting_Rights = models.CharField(max_length=64, null=True, choices=YES_NO)
    Chartered_Accountant = models.CharField(max_length=64, null=True, choices=YES_NO)
    Outstanding_Debt_by_Black_Participants = models.CharField(null=True, max_length=64, blank=True)
    Ownership_Type = models.CharField(max_length=64, null=True)

    Createdby_user = models.CharField(null=True, max_length=64, blank=True)
    Modifiedby_user = models.CharField(null=True, max_length=64,blank=True)


class Procurement(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    ID = models.CharField(max_length=64, primary_key=True)
    Supplier_Name = models.CharField(max_length=64, null=True)
    Reg_No =models.CharField(null=True, max_length=64, blank=True)
    Expenditure_incl_VAT = models.CharField(null=True, max_length=64, blank=True)
    Expenditure_excl_VAT = models.CharField(null=True, max_length=64, blank=True)
    Non_Vat_Item = models.CharField(max_length=64, null=True, choices=YES_NO)
    Supplier_Classification = models.CharField(max_length=64, null=True, choices=SUPPLIER_CLASSIFICATION)
    BEE_Level = models.CharField(max_length=64, null=True, choices=BEE_LEVELS)
    fifty_one_or_more_black_owned = models.CharField(max_length=64, null=True, choices=YES_NO)
    Black_Ownership =  models.CharField(null=True, max_length=64, blank=True)
    thirty_or_more_black_woman_owned = models.CharField(max_length=64, null=True, choices=YES_NO)
    Black_Woman_Ownership = models.CharField(null=True, max_length=64, blank=True)
    Empowering_Supplier = models.CharField(max_length=64, null=True, choices=YES_NO)
    ESD_Recipient_Black_Owned_QSE_EME = models.CharField(max_length=64, null=True, choices=YES_NO)
    Designated_Group_Supplier = models.CharField(max_length=64, null=True, choices=YES_NO)
    Ingest_date = models.CharField(null=True, max_length=64)
    Createdby_user = models.CharField(null=True, max_length=64, blank=True)
    Modifiedby_user = models.CharField(null=True, max_length=64, blank=True)


class SocioEconomicDevelopment(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    ID = models.CharField(max_length=64, primary_key=True)
    Ingest_date = models.CharField(null=True, max_length=64)
    Beneficiary = models.CharField(max_length=64, null=True)
    ICT_Sector_Initiative = models.CharField(max_length=64, null=True, choices=YES_NO)
    Percentage_of_Black_participation = models.FloatField(null=True, blank=True)
    Contribution_Type = models.CharField(max_length=64, null=True, choices=CONTRIBUTION_TYPES)
    Description_of_Contribution = models.CharField(max_length=64, null=True)
    Structured_SED_Project = models.CharField(max_length=64, null=True, choices=YES_NO)
    Date_of_Contribution = models.CharField(null=True, max_length=64)
    Amount_of_Contribution = models.CharField(null=True, max_length=64, blank=True)
    #utilites filed
    Createdby_user = models.CharField(null=True, max_length=64, blank=True)
    Modifiedby_user = models.CharField(null=True, max_length=64, blank=True)




class FinancialInformation(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
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
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    valuation_method = models.CharField(max_length=64, null=True)
    formal_valuation_if_available = models.FloatField(null=True, blank=True)
    total_assets = models.FloatField(null=True, blank=True)
    total_liabilities = models.FloatField(null=True, blank=True)
    nett_asset_value_per_afs = models.FloatField(null=True, blank=True)
    finacial_period = models.CharField(max_length=64, null=True)
    month = models.IntegerField(null=True, blank=True)


class FinacialSkillsDevelopment(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    finacial_period = models.CharField(max_length=64, null=True)
    month = models.IntegerField(null=True, blank=True)
    sdl_payments_made_per_emp201 = models.FloatField(null=True, blank=True)


class NetProfit_ED_ESD(models.Model):
    Table_Name = models.CharField(null=True, max_length=64, blank=True)
    Company_Name = models.CharField(null=True, max_length=64, blank=True)
    finacial_period = models.CharField(max_length=64, null=True)
    npat = models.FloatField(null=True, blank=True)
    projected = models.FloatField(null=True, blank=True)
    ed = models.FloatField(null=True, blank=True)
    sd = models.FloatField(null=True, blank=True)
    sed = models.FloatField(null=True, blank=True)

