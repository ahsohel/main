from . import  views, views_2
from django.urls import path

urlpatterns = [

    path('', views.index, name='index'),
    path('flatmate_listing/', views.flatmate_listing, name='flatmate_listing'),
    path('flatmate_listing_place_start/', views.flatmate_listing_place_start, name='flatmate_listing_place_start'),
    path('flatmate_listing_place_start_go_for_next/', views.flatmate_listing_place_start_go_for_next, name='flatmate_listing_place_start_go_for_next'),
    path('flatmate_listing_place_About_the_property/', views.flatmate_listing_place_About_the_property, name='flatmate_listing_place_About_the_property'),
    path('flatmate_listing_place_Who_currently_lives/', views.flatmate_listing_place_Who_currently_lives, name='flatmate_listing_place_Who_currently_lives'),
    path('flatmate_listing_About_the_room/', views.flatmate_listing_About_the_room, name='flatmate_listing_About_the_room'),
    path('flatmate_listing_Room_Features/', views.flatmate_listing_Room_Features, name='flatmate_listing_Room_Features'),
    path('flatmate_listing_place_Rent_bond_bills/', views.flatmate_listing_place_Rent_bond_bills, name='flatmate_listing_place_Rent_bond_bills'),
    path('flatmate_listing_place_Date_available/', views.flatmate_listing_place_Date_available, name='flatmate_listing_place_Date_available'),
    path('flatmate_listing_place_Property_room_images/', views.flatmate_listing_place_Property_room_images, name='flatmate_listing_place_Property_room_images'),
    path('ideal_flatmate/', views.ideal_flatmate, name='ideal_flatmate'),
    path('Flatmate_Preference/', views.Flatmate_Preference, name='Flatmate_Preference'),
    path('Flatmate_Preference_Accepting/', views.Flatmate_Preference_Accepting, name='Flatmate_Preference_Accepting'),
    path('introduce_yourself/', views.introduce_yourself, name='introduce_yourself'),
    path('introduce_yourself_about_your_flatmates/', views.introduce_yourself_about_your_flatmates, name='introduce_yourself_about_your_flatmates'),
    path('introduce_great_about_living_here/', views.introduce_great_about_living_here, name='introduce_great_about_living_here'),
    path('Preview_Listing_for_House/', views.Preview_Listing_for_House, name='Preview_Listing_for_House'),

    path('details_page/<int:pk>', views.details_page, name='details_page'),

    path('going_for_login/', views_2.going_for_login, name='going_for_login'),
    path('going_for_signup/', views_2.going_for_signup, name='going_for_signup'),

    path('func_signup/', views_2.func_signup, name='func_signup'),
    path('func_login/', views_2.func_login, name='func_login'),

    path('func_logout/', views_2.func_logout, name='func_logout'),

    path('user_profile/', views_2.user_profile, name='user_profile'),
    path('show_list/', views_2.show_list, name='show_list'),

    path('go_to_edit_list/<int:pk>', views_2.go_to_edit_list, name='go_to_edit_list'),
    path('go_to_delete_list/<int:pk>', views_2.go_to_delete_list, name='go_to_delete_list'),

    path('Change_Password_Or_Information/', views_2.Change_Password_Or_Information, name='Change_Password_Or_Information'),
    path('save_the_edited_part/', views_2.save_the_edited_part, name='save_the_edited_part'),
    path('Show_List_Edit_Image/', views_2.Show_List_Edit_Image, name='Show_List_Edit_Image'),
    path('Show_List_Edit_Total/', views_2.Show_List_Edit_Total, name='Show_List_Edit_Total'),
    path('lets_delete_the_image_from_edit_option/', views_2.lets_delete_the_image_from_edit_option, name='lets_delete_the_image_from_edit_option'),
    path('let_save_edited_image_and_get_back/', views_2.let_save_edited_image_and_get_back, name='let_save_edited_image_and_get_back'),


    path('Room_Find_a_place/', views_2.Room_Find_a_place, name='Room_Find_a_place'),
    path('What_type_of_place_are_you_looking/', views_2.What_type_of_place_are_you_looking, name='What_type_of_place_are_you_looking'),
    path('let_go_Where_would_you_like_to_live/', views_2.let_go_Where_would_you_like_to_live, name='let_go_Where_would_you_like_to_live'),
    path('let_go_Rent_and_timing/', views_2.let_go_Rent_and_timing, name='let_go_Rent_and_timing'),
    path('let_go_Property_preferences/', views_2.let_go_Property_preferences, name='let_go_Property_preferences'),
    path('lets_go_for_step_2/', views_2.lets_go_for_step_2, name='lets_go_for_step_2'),
    path('finder_about_you/', views_2.finder_about_you, name='finder_about_you'),
    path('lets_go_for_Employment_status/', views_2.lets_go_for_Employment_status, name='lets_go_for_Employment_status'),
    path('let_go_Lifestyle/', views_2.let_go_Lifestyle, name='let_go_Lifestyle'),
    path('let_go_What_makes_you_great_to_live/', views_2.let_go_What_makes_you_great_to_live, name='let_go_What_makes_you_great_to_live'),
    path('let_go_do_you_want_to_preview/', views_2.let_go_do_you_want_to_preview, name='let_go_do_you_want_to_preview'),
    path('let_finder_info_Preview/', views_2.let_finder_info_Preview, name='let_finder_info_Preview'),


    path('lets_delete_the_image/', views.lets_delete_the_image, name='lets_delete_the_image'),




]