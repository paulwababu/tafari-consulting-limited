from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tutorials import views

urlpatterns = [
    path('tutorials/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('tutorials/', views.tutorialList, name='tutorial_list'),
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about-us'),
    path('developing-team-creativity-initiative/', views.developingteamcreativityinitiative, name='developingteamcreativityinitiative'),
    path('leadership_development_skills/', views.leadership_development_skills, name='leadership_development_skills'),
    #project_team_leadership#coaching_a_service_team#the_voice_of_leadership
    path('project_team_leadership/', views.project_team_leadership, name="project_team_leadership"),
    path('coaching_a_service_team/', views.coaching_a_service_team, name="coaching_a_service_team"),
    path('the_voice_of_leadership/', views.the_voice_of_leadership, name="the_voice_of_leadership"),
    path('creating_leaders_through_mentorship/', views.creating_leaders_through_mentorship, name="creating_leaders_through_mentorship"),
    path('leading_change_organizational_renewal/', views.leading_change_organizational_renewal, name="leading_change_organizational_renewal"),
    path('high_impact_executive_program/', views.high_impact_executive_program, name="high_impact_executive_program"),
    path('achieving_leadership_success_through_people/', views.achieving_leadership_success_through_people, name="achieving_leadership_success_through_people"),
    path('leading_with_emotional_intelligence/', views.leading_with_emotional_intelligence, name="leading_with_emotional_intelligence"),
    path('attitudes_for_customer_service/', views.attitudes_for_customer_service, name="attitudes_for_customer_service"),
    path('building_customer_loyalty/', views.building_customer_loyalty, name="building_customer_loyalty"),
    path('call_centre_and_customer_care_skills/', views.call_centre_and_customer_care_skills, name="call_centre_and_customer_care_skills"),
    path('customer_service_excellence_for_managers/', views.customer_service_excellence_for_managers, name="customer_service_excellence_for_managers"),
    path('how_to_exceed_customers_expectations/', views.how_to_exceed_customers_expectations, name=""),
    path('mastering_the_telephone/', views.mastering_the_telephone, name="mastering_the_telephone"),
    path('ultimate_loyalty_build_teams_that_wow_the_customer/', views.ultimate_loyalty_build_teams_that_wow_the_customer, name="ultimate_loyalty_build_teams_that_wow_the_customer"),
    path('strategies_of_dealing_with_dissatisfied_customers/', views.strategies_of_dealing_with_dissatisfied_customers, name=""),
    path('managing_conflict_at_work_place/', views.managing_conflict_at_work_place, name="managing_conflict_at_work_place"),
    path('retirement_planning/', views.retirement_planning, name="retirement_planning"),
    path('labour_laws_and_regulations/', views.labour_laws_and_regulations, name="labour_laws_and_regulations"),
    path('coaching_yourself_and_others_for_peak_performance/', views.coaching_yourself_and_others_for_peak_performance, name="coaching_yourself_and_others_for_peak_performance"),
    path('stress_management_at_the_workplace/', views.stress_management_at_the_workplace, name=""),
    path('data_and_record_management/', views.data_and_record_management, name=""),
    path('accounts/login/', views.signin, name="login"),
    path('accounts/logout/', views.signout, name="logout"),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
