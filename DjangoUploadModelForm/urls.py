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
    path('finance_for_non_finance_managers/', views.finance_for_non_finance_managers, name="finance_for_non_finance_managers"),
    path('effective_personal_assistant/', views.effective_personal_assistant, name="effective_personal_assistant"),
    path('business_values_and_ethics/', views.business_values_and_ethics, name="business_values_and_ethics"),
    path('business_etiquette/', views.business_etiquette, name="business_etiquette"),
    path('report_writing/', views.report_writing, name="report_writing"),
    path('knowledge_management/', views.knowledge_management, name="knowledge_management"),
    path('beyond_time_management/', views.beyond_time_management, name="beyond_time_management"),
    path('meetings_and_minute_management/', views.meetings_and_minute_management, name="meetings_and_minute_management"),
    path('public_speaking/', views.public_speaking, name="public_speaking"),
    path('media_training/', views.media_training, name="media_training"),
    path('advanced_leadership_communication_strategies/', views.advanced_leadership_communication_strategies, name=""),
    path('developing_your_negotiation_skills/', views.developing_your_negotiation_skills, name="developing_your_negotiation_skills"),
    path('establishing_positive_relationships_managing_conflict/', views.establishing_positive_relationships_managing_conflict, name="establishing_positive_relationships_managing_conflict"),
    path('expanding_your_influence_understanding_the_psychology_of_persuasion/', views.expanding_your_influence_understanding_the_psychology_of_persuasion, name="expanding_your_influence_understanding_the_psychology_of_persuasion"),
    path('conflict_management_and_negotiation_skills/', views.conflict_management_and_negotiation_skills, name="conflict_management_and_negotiation_skills"),
    path('high_impact_communication_skills/', views.high_impact_communication_skills, name="high_impact_communication_skills"),
    path('mastering_the_art_of_business_communication/', views.mastering_the_art_of_business_communication, name="mastering_the_art_of_business_communication"),
    path('digital_branding/', views.digital_branding, name="digital_branding"),
    path('i_m_possible_sales/', views.i_m_possible_sales, name="i_m_possible_sales"),
    path('sponsorship_marketing/', views.sponsorship_marketing, name="sponsorship_marketing"),
    path('brand_and_crisis_communication/', views.brand_and_crisis_communication, name="brand_and_crisis_communication"),
    path('accounts/login/', views.signin, name="login"),
    path('accounts/logout/', views.signout, name="logout"),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
