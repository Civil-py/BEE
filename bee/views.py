from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, EmploymentEquity, Procurement, SkillsDevelopment, Ownership, Board, SocioEconomicDevelopment, FinacialSkillsDevelopment, FinancialInformation, NetProfit_ED_ESD
from .forms import UserForm, EmploymentEquityForm, ProcurementForm,SkillsDevelopmentForm, OwnershipForm, BoardForm, SocioEconomicDevelopmentForm, FinacialInformationForm, FinacialSkillsDevelopmentForm, NetProfit_ED_ESDForm
from django.contrib import messages

# Create your views here.

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


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {user}!')
            return redirect('index')
        else:
            return render(request, 'bee/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'bee/login.html')

def logout_view(request):
    logout(request)
    return redirect('landingpage')


@login_required
def index(request):
    return render(request,"bee/index.html")


def get_form(choice, post_data=None):
    if choice == "Employment Equity":
        return EmploymentEquityForm(post_data)
    if choice == "Ownership":
        return OwnershipForm(post_data)
    if choice == "Skills Development":
        return SkillsDevelopmentForm(post_data)
    if choice == "Procurement":
        return ProcurementForm(post_data)
    if choice == "Board":
        return BoardForm(post_data)
    if choice == "Socio Economic Development":
        return SocioEconomicDevelopmentForm(post_data)
    if choice == "Financial Information":
        return FinacialInformationForm(post_data)
    if choice == "Financial Skills Development":
        return FinacialSkillsDevelopmentForm(post_data)
    if choice == "Net Profit ED ESD":
        return NetProfit_ED_ESDForm(post_data)
    return None

@login_required
def inputs(request, choice):
    if request.method == "POST":
        form = get_form(choice, request.POST)
        if form and form.is_valid():

            form.save()
            messages.success(request, f"added successfully")
            return redirect('inputs', choice=choice)
        else:
            return render(request, "bee/inputs.html", {
                'form': form
            })
    else:
        form = get_form(choice)
        table_name = f'{choice} Input Table'
        return render(request, "bee/inputs.html", {
            'form': form,
            'choice': table_name
        })



@login_required
def financial_inputs(request, choice):
    if request.method == "POST":
        form = get_form(choice, request.POST)
        if form and form.is_valid():

            form.save()
            messages.success(request, f"added successfully")
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