
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('user_registration', views.user_registration),
    path('stylist_registration', views.stylist_registration),
    path('tailor_registration', views.tailor_registration),

    ############## Admin #################

    path('admin_home', views.admin_home),
    path('admin_view_tailor_requests',views.admin_view_tailor_requests),
    path('admin_view_tailor_request_single',views.admin_view_tailor_request_single),
    path('admin_accept_tailor_request',views.admin_accept_tailor_request),
    path('admin_reject_tailor_request',views.admin_reject_tailor_request),
    path('admin_view_stylist_requests',views.admin_view_stylist_requests),
    path('admin_view_stylist_request_single',views.admin_view_stylist_request_single),
    path('admin_accept_stylist_request',views.admin_accept_stylist_request),
    path('admin_reject_stylist_request',views.admin_reject_stylist_request),
    path('admin_view_tailors',views.admin_view_tailors),
    path('admin_view_tailor_single',views.admin_view_tailor_single),
    path('admin_delete_tailor',views.admin_delete_tailor),
    path('admin_view_stylists',views.admin_view_stylists),
    path('admin_view_stylist_single',views.admin_view_stylist_single),
    path('admin_delete_stylist',views.admin_delete_stylist),
    path('admin_view_users',views.admin_view_users),
    path('admin_view_user_single',views.admin_view_user_single),
    path('admin_delete_user',views.admin_delete_user),
    path('admin_view_bookings',views.admin_view_bookings),
    path('admin_view_feedbacks',views.admin_view_feedbacks),


    ############## Tailor #################

    path('tailor_home', views.tailor_home),
    path('tailor_view_work_requests', views.tailor_view_work_requests),
    path('tailor_accept_work', views.tailor_accept_work),
    path('tailor_view_user_messages', views.tailor_view_user_messages),
    path('tailor_reply_user', views.tailor_reply_user),
    path('tailor_sent_work_update_user', views.tailor_sent_work_update_user),
    path('payment_user_for_work_tailor', views.payment_user_for_work_tailor),


    ############## Stylist ################

    path('stylist_home', views.stylist_home),
    path('stylist_add_outfit_designs', views.stylist_add_outfit_designs),
    path('stylist_view_outfit_designs', views.stylist_view_outfit_designs),
    path('stylist_view_outfit_design_single', views.stylist_view_outfit_design_single),
    path('stylist_update_outfit_design', views.stylist_update_outfit_design),
    path('stylist_remove_outfit_design', views.stylist_remove_outfit_design),
    path('stylist_view_user_messages', views.stylist_view_user_messages),
    path('stylist_reply_user', views.stylist_reply_user),



    ############## User #################

    path('user_home', views.user_home),
    path('user_view_outfit_designs', views.user_view_outfit_designs),
    path('user_view_stylists', views.user_view_stylists),
    path('user_view_tailors', views.user_view_tailors),
    path('user_message_to_tailor', views.user_message_to_tailor),
    path('user_view_messages_to_tailor', views.user_view_messages_to_tailor),
    path('user_request_work_to_tailor', views.user_request_work_to_tailor),
    path('user_view_work_requests', views.user_view_work_requests),
    path('user_message_to_stylist', views.user_message_to_stylist),
    path('user_view_messages_to_stylist', views.user_view_messages_to_stylist),
    path('user_add_feedback', views.user_add_feedback),
    path('user_view_feedbacks', views.user_view_feedbacks),
  

]
