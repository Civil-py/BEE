from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import User, EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinacialSkillsDevelopment, FinancialInformation, NetProfit_ED_ESD
from .forms import UserForm, EmploymentEquityForm, ProcurementForm,SkillsDevelopmentForm, OwnershipForm, BoardForm, SocioEconomicDevelopmentForm, FinacialInformationForm, FinacialSkillsDevelopmentForm, NetProfit_ED_ESDForm, ValuationForm
from django.contrib import messages
import boto3
from django.conf import settings
import requests
from jose import jwt
import json

from uuid import uuid4
import datetime

# Create your views here.





def cognito_login(request):
    cognito_login_url = (
        f"https://dominateconsulting.auth.{settings.AWS_COGNITO_REGION}.amazoncognito.com/login?"
        f"client_id={settings.AWS_COGNITO_APP_CLIENT_ID}&"
        f"response_type=code&"
        f"scope=email+openid+phone&"
        f"redirect_uri={settings.AWS_COGNITO_REDIRECT_URL}"
    )
    return redirect(cognito_login_url)



#
# def cognito_authenticate(username, password):
#     client = boto3.client('cognito-idp', region_name=settings.AWS_COGNITO_REGION)
#
#     try:
#         response = client.initiate_auth(
#             AuthFlow='USER_PASSWORD_AUTH',
#             AuthParameters={
#                 'USERNAME': username,
#                 'PASSWORD': password
#             },
#             ClientId=settings.AWS_COGNITO_APP_CLIENT_ID
#         )
#         return response
#     except client.exceptions.NotAuthorizedException:
#         return None
#     except client.exceptions.UserNotFoundException:
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None

def get_cognito_user_info(request, username):
    # Initialize the Cognito client using the settings from your settings.py
    client = boto3.client(
        'cognito-idp',
        region_name=settings.AWS_COGNITO_REGION
    )

    try:
        # Get user information from Cognito
        response = client.admin_get_user(
            UserPoolId=settings.AWS_COGNITO_USER_POOL_ID,
            Username=username
        )

        # Extract and format the user attributes
        user_attributes = {
            attribute['Name']: attribute['Value']
            for attribute in response['UserAttributes']
        }

        return JsonResponse({
            'status': 'success',
            'data': user_attributes
        })

    except client.exceptions.UserNotFoundException:
        return JsonResponse({
            'status': 'error',
            'message': f'User {username} not found.'
        }, status=404)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

# def login_view(request):
#     # Ensure this view is triggered by adding a success message
#     messages.success(request, 'login_view triggered!')
#
#     # Get username from session, which should have been set in the cognito_callback
#     username = request.session.get('username')
#
#     # Check if username is present in the session
#     if username:
#         # You should also have access to the tokens in the session if needed
#         id_token = request.session.get('id_token')
#         access_token = request.session.get('access_token')
#
#         # Retrieve user info from Cognito
#         user_info = get_cognito_user_info(request, username)
#
#         if user_info['status'] == 'success':
#             email = user_info['data'].get('email', username)
#             user, created = User.objects.get_or_create(username=email, defaults={'email': email})
#
#             if created:
#                 user.set_unusable_password()  # Set unusable password if no actual password is needed
#                 user.save()
#
#             # Log the user in for the session
#             login_user(request, user)
#
#             messages.success(request, f'Welcome back, {username}!')
#             return redirect('index')
#         else:
#             return render(request, 'bee/landingpage.html',
#                           {'error': 'Unable to retrieve user information from Cognito.'})
#     else:
#         return render(request, 'bee/landingpage.html', {'error': 'User session not found.'})
#

def login_view(request):
    # Trigger the login_view with a success message
    messages.success(request, 'login_view triggered!')

    # Generate a unique username using a portion of a UUID
    username = f"{str(uuid4()).split('-')[2]}"

    # Create the user or get an existing one
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'email': "Thisseason@email.com"}
    )

    if created:
        # Set an unusable password since it's not needed for this use case
        user.set_unusable_password()
        user.save()

        # Log the user in for the session
        login(request, user)

        # Send a welcome message and redirect to the index page
        messages.success(request, f'Welcome, {username}!')
        return redirect('index')
    else:
        # Handle cases where the user already exists or other issues arise
        return render(request, 'bee/landingpage.html', {'error': 'User session not found.'})






def login_user(request, user):
    if request.method == "POST":
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {user}!')
            return redirect('index')
        else:
            return render(request, 'bee/landingpage.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'bee/landingpage.html')


# def cognito_callback(request):
#     code = request.GET.get('code')
#     token_url = f"https://dominateconsulting.auth.{settings.AWS_COGNITO_REGION}.amazoncognito.com/oauth2/token"
#     response = requests.post(token_url, data={
#         'grant_type': 'authorization_code',
#         'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
#         'client_secret': settings.AWS_COGNITO_APP_CLIENT_SECRET,
#         'code': code,
#         'redirect_uri': 'https://bee-xj6g.onrender.com/bee/bee/cognito/callback/'
#     }, headers={'Content-Type': 'application/x-www-form-urlencoded'})
#
#     token_data = response.json()
#     id_token = token_data.get('id_token')
#     access_token = token_data.get('access_token')
#
#     claims = validate_cognito_token(id_token)
#     if claims:
#         # Store tokens and claims in session
#         request.session['id_token'] = id_token
#         request.session['access_token'] = access_token
#         request.session['username'] = claims['cognito:username']
#         request.session['email'] = claims['email']
#
#         # Redirect to login_view to handle session creation and user login
#         return redirect('login')
#
#     # Handle error cases
#     messages.error(request, f" {token_data} Authentication failed. Please try again.")
#     return redirect('landingpage')

def cognito_callback(request):
    code = request.GET.get('code')
    token_url = f"https://dominateconsulting.auth.{settings.AWS_COGNITO_REGION}.amazoncognito.com/oauth2/token"
    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'client_id': settings.AWS_COGNITO_APP_CLIENT_ID,
        'client_secret': settings.AWS_COGNITO_APP_CLIENT_SECRET,
        'code': code,
        'redirect_uri': 'https://bee-xj6g.onrender.com/bee/bee/cognito/callback/'
    }, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    token_data = response.json()
    id_token = token_data.get('id_token')
    access_token = token_data.get('access_token')

    # claims = validate_cognito_token(id_token)
    # if claims:
    #     # Store tokens and claims in session
    #     request.session['id_token'] = id_token
    #     request.session['access_token'] = access_token
    #     request.session['username'] = claims['cognito:username']
    #     request.session['email'] = claims['email']
    #
    #     # Redirect to login_view to handle session creation and user login
    #     return redirect('login')

    if check_token(token_data):
        login_view(request)



    messages.error(request, f" {token_data} Authentication failed. Please try again.")
    return redirect('landingpage')

def check_token(token_data):
    if 'id_token' in token_data and len(token_data['id_token']) > 50:
        return True
    else:
        return False



def sync_cognito_user(user_info):

    email = user_info['email']
    user, created = User.objects.get_or_create(username=email, defaults={'email': email})

    if created:
        user.set_unusable_password()
        user.save()

    return user


# def validate_cognito_token(token):
#     try:
#         # Get the public keys from AWS
#         response = requests.get(settings.AWS_COGNITO_JWK_URL)
#         keys = response.json().get('keys')
#
#         # Get the key ID from the token headers
#         headers = jwt.get_unverified_headers(token)
#         kid = headers['kid']
#
#         # Find the key
#         key = next(k for k in keys if k['kid'] == kid)
#
#         # Verify the token
#         claims = jwt.decode(
#             token,
#             key,
#             algorithms=['RS256'],
#             audience=settings.AWS_COGNITO_APP_CLIENT_ID,
#             issuer=f"https://cognito-idp.{settings.AWS_COGNITO_REGION}.amazonaws.com/{settings.AWS_COGNITO_USER_POOL_ID}"
#         )
#         return claims
#     except Exception as e:
#         print(f"Token validation error: {e}")
#         return None

def validate_cognito_token(token):
    try:
        # Get the public keys from AWS
        response = requests.get(settings.AWS_COGNITO_JWK_URL)
        keys = response.json().get('keys')
        print(f"Public keys: {keys}")

        # Get the key ID from the token headers
        headers = jwt.get_unverified_headers(token)
        kid = headers['kid']
        print(f"Token headers: {headers}")

        # Find the key
        key = next(k for k in keys if k['kid'] == kid)
        print(f"Matched key: {key}")

        # Verify the token
        claims = jwt.decode(
            token,
            key,
            algorithms=['RS256'],
            audience=settings.AWS_COGNITO_APP_CLIENT_ID,
            issuer=f"https://cognito-idp.{settings.AWS_COGNITO_REGION}.amazonaws.com/{settings.AWS_COGNITO_USER_POOL_ID}"
        )
        print(f"Token claims: {claims}")
        return claims
    except Exception as e:
        print(f"Token validation error: {e}")
        return None







def register(request):
    form = UserForm
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Welcome {username}')
            return redirect('index')

        else:
            return render(request, "bee/register.html", {
                'form': form
            })

    # context = {'form': form}
    return render(request, "bee/register.html", {
        'form': form
    })



def logout_view(request):
    logout(request)
    return redirect('landingpage')

def landingpage(request):
    return render(request, "bee/landingpage.html")

#
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Welcome back {user}!')
#             return redirect('index')
#         else:
#             return render(request, 'bee/login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'bee/login.html')
#
#
# @login_required(login_url='https://dominateconsulting.auth.af-south-1.amazoncognito.com/login?client_id=1qa3ngvpha1hcge9arintssh30&response_type=code&scope=email+openid&redirect_uri=https%3A%2F%2Fec2-13-247-145-14.af-south-1.compute.amazonaws.com%3A8000%2Fbee%2Fhome')
# def index(request):
#     return render(request,"bee/index.html")




def index(request):
    return render(request,"bee/index.html")

LAMBDA_URL = 'https://o4pv5kklxvuaxpzxjtmtjjyeie0wriko.lambda-url.af-south-1.on.aws/'

def send_to_lambda(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LAMBDA_URL, json=data, headers=headers)
    return response



def get_form(choice, post_data=None):
    if choice == "Employment Equity":
        return EmploymentEquityForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_EmploymentEquity" })
    if choice == "Ownership":
        return OwnershipForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_Ownership" })
    if choice == "Skills Development":
        return SkillsDevelopmentForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_SkillsDevelopment" })
    if choice == "Procurement":
        return ProcurementForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_Procurement" })
    if choice == "Board":
        return BoardForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_Board" })
    if choice == "Socio Economic Development":
        return SocioEconomicDevelopmentForm(post_data, initial={'ID':  str(uuid4()).split('-')[2], 'Ingest_date': datetime.datetime.today().date(), 'Table_Name': "in_SocioEconomicDevelopment" })
    if choice == "Financial Information":
        return FinacialInformationForm(post_data)
    if choice == "Financial Skills Development":
        return FinacialSkillsDevelopmentForm(post_data)
    if choice == "Net Profit ED ESD":
        return NetProfit_ED_ESDForm(post_data)
    if choice == "Valuation":
        return ValuationForm(post_data)
    return None



def inputs(request, choice):
    if request.method == "POST":
        form = get_form(choice, request.POST)
        if form and form.is_valid():
            serialized_data = serialize_form_data(form)
            response = send_to_lambda(serialized_data)
            messages.success(request, f"Added Successfully ")

            return redirect('inputs', choice=choice)
        else:
            return render(request, "bee/inputs.html", {
                'form': form,
                'choice': choice
            })
    else:
        form = get_form(choice)
        table_name = f'{choice} Input Table'
        return render(request, "bee/inputs.html", {
            'form': form,
            'choice': table_name
        })


def serialize_form_data(form):
    """
    Serialize Django form data into JSON format.
    """
    serialized_data = {}
    for field_name, field_value in form.cleaned_data.items():
        serialized_data[field_name] = field_value
    return serialized_data
#
# def serialize_form_data(choice, form):
#     """
#     Serialize Django form data into JSON format and wrap it with the choice key.
#     """
#     serialized_data = {"table name " :choice, form.cleaned_data}
#     return json.dumps(serialized_data)








def financial_inputs(request, choice):
    if request.method == "POST":
        form = get_form(choice, request.POST)
        if form and form.is_valid():
            serialized_data = serialize_form_data(form)
            messages.success(request, f"{serialized_data}")
            return redirect('inputs', choice=choice)
        else:
            return render(request, "bee/financial_inputs.html", {
                'form': form
            })
    else:
        form = get_form(choice)
        table_name = f'{choice} Input Table'
        return render(request, "bee/financial_inputs.html", {
            'form': form,
            'choice': table_name
        })


def landingpage(request):
    return render(request,"bee/landingpage.html")
