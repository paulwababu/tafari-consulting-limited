from django.shortcuts import render, redirect
from .forms import TutorialForm
from .models import Tutorial
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'tutorial/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'tutorial/signin.html', {'form': form})

@login_required
def tutorialList(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/list.html', { 'tutorials' : tutorials})


def home(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/home.html', { 'tutorials' : tutorials})    

@login_required
def uploadTutorial(request):
    if request.method == 'POST':  
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})

@login_required
def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete()
    return redirect('tutorial_list')

def signout(request):
    logout(request)
    return redirect('/')

def about(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/about-us.html', { 'tutorials' : tutorials})    

def developingteamcreativityinitiative(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/developing-team-creativity-initiative.html', { 'tutorials' : tutorials})

def leadership_development_skills(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/leadership_development_skills.html', { 'tutorials' : tutorials})

def project_team_leadership(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/project_team_leadership.html', { 'tutorials' : tutorials})

def coaching_a_service_team(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/coaching_a_service_team.html', { 'tutorials' : tutorials})

def the_voice_of_leadership(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/the_voice_of_leadership.html', { 'tutorials' : tutorials})

def creating_leaders_through_mentorship(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/creating_leaders_through_mentorship.html', { 'tutorials' : tutorials})

def leading_change_organizational_renewal(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/leading_change_organizational_renewal.html', { 'tutorials' : tutorials})

def high_impact_executive_program(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/high_impact_executive_program.html', { 'tutorials' : tutorials})

def achieving_leadership_success_through_people(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/achieving_leadership_success_through_people.html', { 'tutorials' : tutorials})

def leading_with_emotional_intelligence(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/leading_with_emotional_intelligence.html', { 'tutorials' : tutorials})

def attitudes_for_customer_service(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/attitudes_for_customer_service.html', { 'tutorials' : tutorials})

def building_customer_loyalty(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/building_customer_loyalty.html', { 'tutorials' : tutorials})

def call_centre_and_customer_care_skills(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/call_centre_and_customer_care_skills.html', { 'tutorials' : tutorials})

def customer_service_excellence_for_managers(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/customer_service_excellence_for_managers.html', { 'tutorials' : tutorials})

def how_to_exceed_customers_expectations(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/how_to_exceed_customers_expectations.html', { 'tutorials' : tutorials})

def mastering_the_telephone(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/mastering_the_telephone.html', { 'tutorials' : tutorials})

def ultimate_loyalty_build_teams_that_wow_the_customer(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/ultimate_loyalty_build_teams_that_wow_the_customer.html', { 'tutorials' : tutorials})

def strategies_of_dealing_with_dissatisfied_customers(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/strategies_of_dealing_with_dissatisfied_customers.html', { 'tutorials' : tutorials})

def managing_conflict_at_work_place(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/managing_conflict_at_work_place.html', { 'tutorials' : tutorials})

def retirement_planning(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/retirement_planning.html', { 'tutorials' : tutorials})

def labour_laws_and_regulations(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/labour_laws_and_regulations.html', { 'tutorials' : tutorials})

def coaching_yourself_and_others_for_peak_performance(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/coaching_yourself_and_others_for_peak_performance.html', { 'tutorials' : tutorials})

def stress_management_at_the_workplace(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/stress_management_at_the_workplace.html', { 'tutorials' : tutorials})

def data_and_record_management(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/data_and_record_management.html', { 'tutorials' : tutorials})

def finance_for_non_finance_managers(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/finance_for_non_finance_managers.html', { 'tutorials' : tutorials})

def effective_personal_assistant(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/effective_personal_assistant.html', { 'tutorials' : tutorials})

def business_values_and_ethics(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/business_values_and_ethics.html', { 'tutorials' : tutorials})

def business_etiquette(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/business_etiquette.html', { 'tutorials' : tutorials})

def report_writing(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/report_writing.html', { 'tutorials' : tutorials})

def knowledge_management(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/knowledge_management.html', { 'tutorials' : tutorials})

def beyond_time_management(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/beyond_time_management.html', { 'tutorials' : tutorials})

def meetings_and_minute_management(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/meetings_and_minute_management.html', { 'tutorials' : tutorials})

def public_speaking(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/public_speaking.html', { 'tutorials' : tutorials})

def media_training(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/media_training.html', { 'tutorials' : tutorials})

def advanced_leadership_communication_strategies(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/advanced_leadership_communication_strategies.html', { 'tutorials' : tutorials})

def developing_your_negotiation_skills(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/developing_your_negotiation_skills.html', { 'tutorials' : tutorials})

def establishing_positive_relationships_managing_conflict(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/establishing_positive_relationships_managing_conflict.html', { 'tutorials' : tutorials})

def expanding_your_influence_understanding_the_psychology_of_persuasion(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/expanding_your_influence_understanding_the_psychology_of_persuasion.html', { 'tutorials' : tutorials})

def conflict_management_and_negotiation_skills(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/conflict_management_and_negotiation_skills.html', { 'tutorials' : tutorials})

def high_impact_communication_skills(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/high_impact_communication_skills.html', { 'tutorials' : tutorials})

def mastering_the_art_of_business_communication(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/mastering_the_art_of_business_communication.html', { 'tutorials' : tutorials})

def digital_branding(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/digital_branding.html', { 'tutorials' : tutorials})

def i_m_possible_sales(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/i_m_possible_sales.html', { 'tutorials' : tutorials})

def sponsorship_marketing(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/sponsorship_marketing.html', { 'tutorials' : tutorials})
