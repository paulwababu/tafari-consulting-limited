from django.shortcuts import render, redirect
from .forms import TutorialForm
from .models import Tutorial, Monitor
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import africastalking
from django.contrib import messages
import os
import psutil
import urllib3
import json
import requests
import datetime
from django.core.paginator import Paginator
# Create your views here.
#ssh -i "tci_please_save.pem" ubuntu@ec2-18-223-88-101.us-east-2.compute.amazonaws.com
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
    paginatedSearch = Paginator(tutorials, 6)
    pageSearch = request.GET.get('page', 1)
    pgSearch = paginatedSearch.page(pageSearch)
    #search
    if request.method == 'POST':
        inputGiven = (request.POST['search2'])
        tosearch = Tutorial.objects.filter(category__contains=inputGiven)
        paginatedSearch2 = Paginator(tosearch, 6)
        pageSearch2 = request.GET.get('page', 1)
        pgSearch2 = paginatedSearch2.page(pageSearch2)
        return render(request, 'tutorial/list.html', { 'tutorials' : pgSearch2})
    return render(request, 'tutorial/list.html', { 'tutorials' : pgSearch})


def home(request):
    tutorials = Tutorial.objects.all()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    response = requests.get('http://api.ipstack.com/'+ip+'?access_key=ee7d4335635d89a71b95dcc33eb2a044')
    rawData = response.json()
    continent = rawData['continent_name']
    country = rawData['country_name']
    capital = rawData['city']
    city = rawData['location']['capital']
    now = datetime.datetime.now()
    datetimenow = now.strftime("%Y-%m-%d %H:%M:%S")
    saveNow = Monitor(
        continent=continent,
        country=country,
        capital=capital,
        city=city,
        datetime=datetimenow,
        ip=ip
    )
    saveNow.save()
    return render(request, 'tutorial/home.html', { 'tutorials' : tutorials})

@login_required
def traffic_monitor(request):
    dataSaved = Monitor.objects.all()
    # Getting loadover15 minutes 
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage = int((load15/os.cpu_count()) * 100)
    ram_usage = int(psutil.virtual_memory()[2])
    p = Paginator(dataSaved, 10)
    #shows number of items in page
    totalSiteVisits = (p.count)
    #find unique page viewers & Duration
    pageNum = request.GET.get('page', 1)
    page1 = p.page(pageNum)
    #unique page viewers
    a = Monitor.objects.order_by().values('ip').distinct()
    pp = Paginator(a, 10)
    #shows number of items in page
    unique = (pp.count)
    #update time
    now = datetime.datetime.now()
    data = {
        "now":now,
        "unique":unique,
        "totalSiteVisits":totalSiteVisits,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "dataSaved": page1,
    }
    return render(request, 'tutorial/traffic_monitor.html', data)

@login_required
def uploadTutorial(request):
    if request.method == 'POST':  
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(), messages.success(request, 'Successfully Uploaded Photo')
            return redirect('tutorial_list')
    else:
        form = TutorialForm()
    return render(request, 'tutorial/upload.html', {'form' : form})

@login_required
def deleteTutorial(request, pk):
    if request.method == 'POST':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete(), messages.success(request, 'Successfully Deleted Photo')
    return redirect('tutorial_list')

@login_required
def sms(request):
    tutorials = Tutorial.objects.all()
    if request.method == 'POST':
        inputGiven = (request.POST['message'])
        #initialize the sdk
        username = "PaulSaul"
        api_key = "630bf5f260ab805515344b1da455b0b74120afd270bba43701b4552f14080136"
        africastalking.initialize(username,api_key)
        recipients = ['+254797584194']
        #message
        message = inputGiven
        #initialize the service, in our case, SMS
        sms = africastalking.SMS
        sms.send(message, recipients), messages.success(request, 'Successfully Sent Photo')
    return render(request, 'tutorial/sms.html')

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

def brand_and_crisis_communication(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/brand_and_crisis_communication.html', { 'tutorials' : tutorials})

def internal_brand_engagement(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/internal_brand_engagement.html', { 'tutorials' : tutorials})

def brand_innovation_and_management(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/brand_innovation_and_management.html', { 'tutorials' : tutorials})

def effective_sales_management_techniques(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/effective_sales_management_techniques.html', { 'tutorials' : tutorials})

def team_building(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/team_building.html', { 'tutorials' : tutorials})

def gender_streamlining(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/gender_streamlining.html', { 'tutorials' : tutorials})

def customer_service_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/customer_service_programs.html', { 'tutorials' : tutorials})

def leadership_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/leadership_programs.html', { 'tutorials' : tutorials})

def special_category(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/special_category.html', { 'tutorials' : tutorials})

def business_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/business_programs.html', { 'tutorials' : tutorials})

def communication_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/communication_programs.html', { 'tutorials' : tutorials})

def training_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/training_programs.html', { 'tutorials' : tutorials})

def consultancy_services(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/consultancy_services.html', { 'tutorials' : tutorials})

def gallery(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/gallery.html', { 'tutorials' : tutorials})

def clients_partners(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/clients_partners.html', { 'tutorials' : tutorials})

def human_resource_programs(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/human_resource_programs.html', { 'tutorials' : tutorials})

def sales_and_marketing(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial/sales_and_marketing.html', { 'tutorials' : tutorials})

def contact_us(request):
    tutorials = Tutorial.objects.all()
    if request.method == 'POST':
        theyname = (request.POST['your-name'])
        thymail = (request.POST['your-email'])
        thytel = (request.POST['your-tel'])
        thymenu = (request.POST['menu-354'])
        thymessage = (request.POST['your-message'])
        inputGiven = ("Name: " +theyname+ "\nEmail: " +thymail+ "\nTel: " +thytel+ "\nSubject: " +thymenu+ "\nMessage-Body: " +thymessage)
        username = "PaulSaul"
        api_key = "bac664d33d4f6f5a556aec0b8c88898112215d38056695b7f79e09035c2c6e46"
        africastalking.initialize(username,api_key)
        #recipients
        recipients = ['+254797584194']
        #message
        message = inputGiven
        #initialize the service, in our case, SMS
        sms = africastalking.SMS
        sms2 = africastalking.SMS
        sms.send(message, recipients)
        #send sms to the sender to tell them you have received
        message2sender = ("We will get back to you shortly, " +theyname)
        sms2.send(message2sender, [thytel]), messages.success(request, 'Message Sent, Awaiting response')
        return redirect('/')
    return render(request, 'tutorial/contact_us.html', { 'tutorials' : tutorials})
