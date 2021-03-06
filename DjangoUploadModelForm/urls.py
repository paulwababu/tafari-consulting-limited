from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tutorials import views

urlpatterns = [
    path('tutorials/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('tutorials/', views.tutorialList, name='tutorial_list'),
    path('sms/', views.sms, name="sms"),
    path('', views.home, name='home'),
    path('traffic_monitor/', views.traffic_monitor, name="traffic_monitor"),
    path('about-us/', views.about, name='about-us'),
    path('developing-team-creativity-initiative/', views.developingteamcreativityinitiative, name='developingteamcreativityinitiative'),
    path('leadership_development_skills/', views.leadership_development_skills, name='leadership_development_skills'),
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
    path('internal_brand_engagement/', views.internal_brand_engagement, name="internal_brand_engagement"),
    path('brand_innovation_and_management/', views.brand_innovation_and_management, name="brand_innovation_and_management"),
    path('effective_sales_management_techniques/', views.effective_sales_management_techniques, name="effective_sales_management_techniques"),
    path('team_building/', views.team_building, name="team_building"),
    path('gender_streamlining/', views.gender_streamlining, name="gender_streamlining"),
    path('customer_service_programs/', views.customer_service_programs, name="customer_service_programs"),
    path('leadership_programs/', views.leadership_programs, name="leadership_programs"),
    path('special_category/', views.special_category, name="special_category"),
    path('business_programs/', views.business_programs, name="business_programs"),
    path('communication_programs/', views.communication_programs, name="communication_programs"),
    path('training_programs/', views.training_programs, name="training_programs"),
    path('consultancy_services/', views.consultancy_services, name="consultancy_services"),
    path('gallery/', views.gallery, name="gallery"),
    path('clients_partners/', views.clients_partners, name="clients_partners"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('sales_and_marketing/', views.sales_and_marketing, name="sales_and_marketing"),
    path('human_resource_programs/', views.human_resource_programs, name="human_resource_programs"),
    ####################
    path('about_us/', views.about, name='about-us'),
    path('developing_team_creativity_initiative/', views.developingteamcreativityinitiative, name='developingteamcreativityinitiative'),
    path('leadership-development-skills/', views.leadership_development_skills, name='leadership_development_skills'),
    path('project-team-leadership/', views.project_team_leadership, name="project_team_leadership"),
    path('coaching-a-service-team/', views.coaching_a_service_team, name="coaching_a_service_team"),
    path('the-voice-of-leadership/', views.the_voice_of_leadership, name="the_voice_of_leadership"),
    path('creating-leaders-through-mentorship/', views.creating_leaders_through_mentorship, name="creating_leaders_through_mentorship"),
    path('leading-change-organizational-renewal/', views.leading_change_organizational_renewal, name="leading_change_organizational_renewal"),
    path('high-impact-executive-program/', views.high_impact_executive_program, name="high_impact_executive_program"),
    path('achieving-leadership-success-through-people/', views.achieving_leadership_success_through_people, name="achieving_leadership_success_through_people"),
    path('leading-with-emotional-intelligence/', views.leading_with_emotional_intelligence, name="leading_with_emotional_intelligence"),
    path('attitudes-for-customer-service/', views.attitudes_for_customer_service, name="attitudes_for_customer_service"),
    path('building-customer-loyalty/', views.building_customer_loyalty, name="building_customer_loyalty"),
    path('call-centre-and-customer-care-skills/', views.call_centre_and_customer_care_skills, name="call_centre_and_customer_care_skills"),
    path('customer-service-excellence-for-managers/', views.customer_service_excellence_for_managers, name="customer_service_excellence_for_managers"),
    path('how-to-exceed-customers-expectations/', views.how_to_exceed_customers_expectations, name=""),
    path('mastering-the-telephone/', views.mastering_the_telephone, name="mastering_the_telephone"),
    path('ultimate-loyalty-build-teams-that-wow-the-customer/', views.ultimate_loyalty_build_teams_that_wow_the_customer, name="ultimate_loyalty_build_teams_that_wow_the_customer"),
    path('strategies-of-dealing-with-dissatisfied-customers/', views.strategies_of_dealing_with_dissatisfied_customers, name=""),
    path('managing-conflict-at-work-place/', views.managing_conflict_at_work_place, name="managing_conflict_at_work_place"),
    path('retirement-planning/', views.retirement_planning, name="retirement_planning"),
    path('labour-laws-and-regulations/', views.labour_laws_and_regulations, name="labour_laws_and_regulations"),
    path('coaching-yourself-and-others-for-peak-performance/', views.coaching_yourself_and_others_for_peak_performance, name="coaching_yourself_and_others_for_peak_performance"),
    path('stress-management-at-the-workplace/', views.stress_management_at_the_workplace, name=""),
    path('data-and-record-management/', views.data_and_record_management, name=""),
    path('finance-for-non-finance-managers/', views.finance_for_non_finance_managers, name="finance_for_non_finance_managers"),
    path('effective-personal-assistant/', views.effective_personal_assistant, name="effective_personal_assistant"),
    path('business-values-and-ethics/', views.business_values_and_ethics, name="business_values_and_ethics"),
    path('business-etiquette/', views.business_etiquette, name="business_etiquette"),
    path('report-writing/', views.report_writing, name="report_writing"),
    path('knowledge-management/', views.knowledge_management, name="knowledge_management"),
    path('beyond-time-management/', views.beyond_time_management, name="beyond_time_management"),
    path('meetings-and-minute-management/', views.meetings_and_minute_management, name="meetings_and_minute_management"),
    path('public-speaking/', views.public_speaking, name="public_speaking"),
    path('media-training/', views.media_training, name="media_training"),
    path('advanced-leadership-communication-strategies/', views.advanced_leadership_communication_strategies, name=""),
    path('developing-your-negotiation-skills/', views.developing_your_negotiation_skills, name="developing_your_negotiation_skills"),
    path('establishing-positive-relationships-managing-conflict/', views.establishing_positive_relationships_managing_conflict, name="establishing_positive_relationships_managing_conflict"),
    path('expanding-your-influence-understanding-the-psychology-of-persuasion/', views.expanding_your_influence_understanding_the_psychology_of_persuasion, name="expanding_your_influence_understanding_the_psychology_of_persuasion"),
    path('conflict-management-and-negotiation-skills/', views.conflict_management_and_negotiation_skills, name="conflict_management_and_negotiation_skills"),
    path('high-impact-communication-skills/', views.high_impact_communication_skills, name="high_impact_communication_skills"),
    path('mastering-the-art-of-business-communication/', views.mastering_the_art_of_business_communication, name="mastering_the_art_of_business_communication"),
    path('digital-branding/', views.digital_branding, name="digital_branding"),
    path('i-m-possible-sales/', views.i_m_possible_sales, name="i_m_possible_sales"),
    path('sponsorship_marketing/', views.sponsorship_marketing, name="sponsorship_marketing"),
    path('brand-and-crisis-communication/', views.brand_and_crisis_communication, name="brand_and_crisis_communication"),
    path('internal-brand-engagement/', views.internal_brand_engagement, name="internal_brand_engagement"),
    path('brand-innovation-and-management/', views.brand_innovation_and_management, name="brand_innovation_and_management"),
    path('effective-sales-management-techniques/', views.effective_sales_management_techniques, name="effective_sales_management_techniques"),
    path('team-building/', views.team_building, name="team_building"),
    path('gender-streamlining/', views.gender_streamlining, name="gender_streamlining"),
    path('customer-service-programs/', views.customer_service_programs, name="customer_service_programs"),
    path('leadership-programs/', views.leadership_programs, name="leadership_programs"),
    path('special-category/', views.special_category, name="special_category"),
    path('business-programs/', views.business_programs, name="business_programs"),
    path('communication-programs/', views.communication_programs, name="communication_programs"),
    path('training-programs/', views.training_programs, name="training_programs"),
    path('consultancy-services/', views.consultancy_services, name="consultancy_services"),
    path('gallery/', views.gallery, name="gallery"),
    path('clients-partners/', views.clients_partners, name="clients_partners"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('sales-and-marketing/', views.sales_and_marketing, name="sales_and_marketing"),
    path('human-resource-programs/', views.human_resource_programs, name="human_resource_programs"),
    
    ####################
    path('accounts/login/', views.signin, name="login"),
    path('accounts/logout/', views.signout, name="logout"),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
