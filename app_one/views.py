from django.shortcuts import render, HttpResponse, redirect
from .models import listing_of_accommodationthat_seller_offering, accommodationthat_seller_offering_image, User_info_table

from django.contrib.auth.models import User

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        user_info = User_info_table.objects.get(id=session_user_id)
    else:
        user_info = ''




    get_the_all_list = listing_of_accommodationthat_seller_offering.objects.all()

    print('get_the_all_list.model_Property_and_room_images_1.all()')
    for i in get_the_all_list:
        print(i.model_Property_and_room_images_1)
        print(i.model_Property_and_room_images_1)



    contex = {
        'get_the_all_list':get_the_all_list,
        'user_info':user_info,
    }

    return render(request, 'index.html', contex)



def details_page(request, pk):
    get_the_spacific_list = listing_of_accommodationthat_seller_offering.objects.get(id=pk)

    contex = {
        'get_the_spacific_list': get_the_spacific_list,
    }

    return render(request, 'details_page.html', contex)





def flatmate_listing(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        return render(request, 'flatmate_listing.html')

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def flatmate_listing_place_start(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        # this is for the back button

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Room_availability_Date = request.POST.get('Room_availability_Date')


        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')

        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')

        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')

        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')

        print('Property_AddressProperty_AddressProperty_AddressProperty_AddressProperty_Address')
        print(Property_Address)



        if Property_Address:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,


                'offering_accommodation': offering_accommodation,
                'property': property,
                'back':'back',
                'Property_Address':Property_Address,
                'property_bedrooms':property_bedrooms,
                'property_bathrooms':property_bathrooms,
                'changed_Parking':changed_Parking,
                'changed_Internet':changed_Internet,
                'property_Who_currently_lives':property_Who_currently_lives,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
            }
        else:
            contex={}

        return render(request, 'flatmate_listing_place_start.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def flatmate_listing_place_start_go_for_next(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        print('offering_accommodation')
        print(offering_accommodation)
        print(property)



        # this is for the back button

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        print('popopopopopopopopoppop')
        print(Room_availability_Date)
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')



        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')

        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')

        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')



        if Property_Address:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,


                'offering_accommodation': offering_accommodation,
                'property': property,
                'back':'back',
                'Property_Address':Property_Address,
                'property_bedrooms':property_bedrooms,
                'property_bathrooms':property_bathrooms,
                'changed_Parking':changed_Parking,
                'changed_Internet':changed_Internet,
                'property_Who_currently_lives':property_Who_currently_lives,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
            }



        else:
            contex = {
                'offering_accommodation':offering_accommodation,
                'property':property,
            }

        return render(request, 'flatmate_listing_place_start_go_for_next.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')



def flatmate_listing_place_About_the_property(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')

        #hidden part
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        print('Property_Address')
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)

        print('hidden')
        print(offering_accommodation)
        print(property)

        # this is for the back button

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')


        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')



        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')


        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')

        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,
                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'offering_accommodation': offering_accommodation,
                'property': property,
                'back': 'back',
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'property_Who_currently_lives':property_Who_currently_lives,

                'Room_name':Room_name,
                'Room_type':Room_type,
                'Room_furnishings':Room_furnishings,
                'Bathroom_type':Bathroom_type,
            }




        else:
            contex = {
                'Property_Address':Property_Address,
                'property_bedrooms':property_bedrooms,
                'property_bathrooms':property_bathrooms,
                'changed_Parking':changed_Parking,
                'changed_Internet':changed_Internet,
                'offering_accommodation':offering_accommodation,
                'property':property,

            }


        return render(request, 'flatmate_listing_place_About_the_property.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def flatmate_listing_place_Who_currently_lives(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')


        # hidden part
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('property_Who_currently_lives')
        print(property_Who_currently_lives)

        print('hidden')
        print('Property_Address')
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # this is for the back button
        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')

        print('llllllllllllllllllllllllllllllllllll')
        print(Bed_Size)
        print(Bed_Size)


        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,


                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,

                'offering_accommodation': offering_accommodation,

                'property': property,
                'back': 'back',
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'property_Who_currently_lives': property_Who_currently_lives,
            }


        else:
            contex = {
                'property_Who_currently_lives':property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }

        return render(request, 'flatmate_listing_place_Who_currently_lives.html', contex)


    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')



def flatmate_listing_About_the_room(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')


        # hidden part
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('Room_name')
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)

        print('hidden')
        print('Property_Address')
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # this is for the back button

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')
        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')


        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }


        else:

            contex = {
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,

                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }


        return render(request, 'flatmate_listing_About_the_room.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')


def flatmate_listing_Room_Features(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')



        # hidden part
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)


        print('hidden')
        print('Room_name')
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # this is for the back button

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')
        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')

        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,


                'Flatmate_Preference_name':Flatmate_Preference_name,

                'image_id':image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }
        else:




            contex = {
                'Bed_Size':Bed_Size,
                'Room_furnishings_features_Bed_side_table':Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe':Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers':Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner':Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater':Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk':Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp':Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair':Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch':Room_furnishings_features_Couch,
                'Room_furnishings_features_TV':Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony':Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock':Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette':Room_furnishings_features_Kitchenette,


                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }



        return render(request, 'flatmate_listing_Room_Features.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')


def flatmate_listing_place_Rent_bond_bills(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')


        # hidden part


        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)


        print('hidden')
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # this is for the back button
        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')
        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')


        image_id = request.POST.get('image_id')
        print('image_idimage_idimage_idimage_idimage_idimage_id')
        print(image_id)
        print(image_id)

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')

        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name':Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }

        else:
            contex = {
                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,


                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }


        return render(request, 'flatmate_listing_place_Rent_bond_bills.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')


def flatmate_listing_place_Date_available(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        image_id = request.POST.get('image_id')
        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')
        print('ppppppppppppppppppp')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        print(Flatmate_Preference_name)
        print(Accepting_Backpackers)

        print("soheloooooooo")
        print(image_id)

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')


        # hidden part
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')




        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)


        print('hidden')
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # this is for the back button
        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        print('ppppppppppppppppppp')
        print(Accepting_Backpackers)
        print(Flatmate_Preference_name)
        print(Accepting_Backpackers)

        image_id = request.POST.get('image_id')

        print("soheloooooooo")
        print(image_id)
        upload_image=[]
        if image_id:
            k = image_id[1:len(image_id) - 1]
            print(k)
            lit_img = []
            p = k.split(", ")
            print('ppppppppppp')
            print(p)
            if p != [''] and p != ['on']:
                for i in p:
                    print('iiiiiiiiiii')
                    print(i)
                    lit_img.append(int(i))
                print('lit_imglit_imglit_imglit_imglit_img')
                print(lit_img)
                if lit_img:
                    upload_image = accommodationthat_seller_offering_image.objects.filter(id__in=lit_img)
                    lenth_of_image =0
                    for i in upload_image:
                        lenth_of_image=lenth_of_image+1
                print('ddddddddddddddddddddddddddssssssssssssssssss')
                print(lenth_of_image)


        print('dakhe koybar')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')

        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')

        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')

        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')





        if changed_Internet:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name':Flatmate_Preference_name,

                'upload_image': upload_image,
                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }
        if upload_image and changed_Internet:

            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name':Flatmate_Preference_name,

                'upload_image': upload_image,
                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,

                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,

                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,

                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }


        else:
            contex = {
                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'upload_image': upload_image,
                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,


                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,
                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }


        return render(request, 'flatmate_listing_place_Date_available.html', contex)


    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')



def flatmate_listing_place_Property_room_images(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:
        Property_and_room_images_1 = request.FILES.get('Property_and_room_images_1')
        Property_and_room_images_2 = request.FILES.get('Property_and_room_images_2')
        Property_and_room_images_3 = request.FILES.get('Property_and_room_images_3')
        Property_and_room_images_4 = request.FILES.get('Property_and_room_images_4')
        Property_and_room_images_5 = request.FILES.get('Property_and_room_images_5')

        image_id = request.POST.get('image_id')
        if image_id:

            k = image_id[1:len(image_id) - 1]

            lit_img = []
            p = k.split(", ")

            if p != [''] and p != ['on']:
                for i in p:

                    lit_img.append(int(i))

            # checking, is the image in the model
            lit_img_2=[]
            for i in lit_img:

                is_it_there_or_not = accommodationthat_seller_offering_image.objects.filter(id=i)
                if is_it_there_or_not:
                    lit_img_2.append(i)

            if lit_img_2:
                image_id=lit_img_2
            else:
                image_id = lit_img


        else:
            image_id=[]
        if Property_and_room_images_1:
            images_1_save_images = accommodationthat_seller_offering_image(model_Property_and_room_images_1=Property_and_room_images_1)
            images_1_save_images.save()
            print("images_1_save_images.id")
            print(images_1_save_images.id)
            image_id.append(images_1_save_images.id)
        if Property_and_room_images_2:
            images_2_save_images = accommodationthat_seller_offering_image(model_Property_and_room_images_1=Property_and_room_images_2)
            images_2_save_images.save()
            print("images_2_save_images.id")
            print(images_2_save_images.id)
            image_id.append(images_2_save_images.id)
        if Property_and_room_images_3:
            images_3_save_images = accommodationthat_seller_offering_image(model_Property_and_room_images_1=Property_and_room_images_3)
            images_3_save_images.save()
            print("images_3_save_images.id")
            print(images_3_save_images.id)
            image_id.append(images_3_save_images.id)
        if Property_and_room_images_4:
            images_4_save_images = accommodationthat_seller_offering_image(model_Property_and_room_images_1=Property_and_room_images_4)
            images_4_save_images.save()
            print("images_4_save_images.id")
            print(images_4_save_images.id)
            image_id.append(images_4_save_images.id)
        if Property_and_room_images_5:
            images_5_save_images = accommodationthat_seller_offering_image(model_Property_and_room_images_1=Property_and_room_images_5)
            images_5_save_images.save()
            print("images_5_save_images.id")
            print(images_5_save_images.id)
            image_id.append(images_5_save_images.id)

        print('image_id')
        print(image_id)
        for i in image_id:
            print('first place')
            print(i)


        print(type(image_id))
        image_id = str(image_id)
        print(type(image_id))




        # hidden part
        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')




        print('Property_and_room_images_1')
        print(Property_and_room_images_1)
        print(Property_and_room_images_2)
        print(Property_and_room_images_3)
        print(Property_and_room_images_4)
        print(Property_and_room_images_5)


        print('hidden')
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        # back part


        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        print('wwwwwwwwwwwwwwwwwwwwwwwwwwww')
        print(Accepting_Backpackers)
        print(Flatmate_Preference_name)
        print(Accepting_Backpackers)


        if Flatmate_Preference_name:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,
                'introduce_about_your_flatmates': introduce_about_your_flatmates,

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,
                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }

        else:

            contex = {

                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,

                'image_id': image_id,

                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,
                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }




        return render(request, 'flatmate_listing_place_Property_room_images.html', contex)


    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')




def ideal_flatmate(request):

    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')


        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        image_id = request.POST.get('image_id')

        print('image_id secondplllllllllllllllll')
        print(type(image_id))
        print(image_id)

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')


        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('hidden')
        print('hidden')
        print('hidden')
        print('hidden')
        print('hidden')
        print('hidden')
        print(image_id)
        print(image_id)
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        if Flatmate_Preference_name:
            contex = {

                'introduce_great_about_living': introduce_great_about_living,

                'introduce_about_your_flatmates': introduce_about_your_flatmates,


                'Accepting_Backpackers': Accepting_Backpackers,
                'Accepting_Students': Accepting_Students,
                'Accepting_Smokers': Accepting_Smokers,
                'Accepting_LGBTI': Accepting_LGBTI,
                'Accepting_years_olds': Accepting_years_olds,
                'Accepting_Children': Accepting_Children,
                'Accepting_Pets': Accepting_Pets,
                'Accepting_Retirees': Accepting_Retirees,
                'Accepting_On_welfare': Accepting_On_welfare,

                'Flatmate_Preference_name': Flatmate_Preference_name,
                'image_id': image_id,
                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,
                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }

        else:
            contex = {



                'image_id': image_id,
                'Room_availability_Date': Room_availability_Date,
                'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
                'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
                'room_Weekly_rent': room_Weekly_rent,
                'room_changed_Bond': room_changed_Bond,
                'room_changed_Bills': room_changed_Bills,
                'Bed_Size': Bed_Size,
                'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
                'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
                'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
                'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
                'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
                'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
                'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
                'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
                'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
                'Room_furnishings_features_TV': Room_furnishings_features_TV,
                'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
                'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
                'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
                'Room_name': Room_name,
                'Room_type': Room_type,
                'Room_furnishings': Room_furnishings,
                'Bathroom_type': Bathroom_type,
                'property_Who_currently_lives': property_Who_currently_lives,
                'Property_Address': Property_Address,
                'property_bedrooms': property_bedrooms,
                'property_bathrooms': property_bathrooms,
                'changed_Parking': changed_Parking,
                'changed_Internet': changed_Internet,
                'offering_accommodation': offering_accommodation,
                'property': property,

            }






        return render(request, 'ideal_flatmate.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def Flatmate_Preference(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        image_id = request.POST.get('image_id')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')









        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)




        contex = {

            'introduce_great_about_living': introduce_great_about_living,

            'introduce_about_your_flatmates': introduce_about_your_flatmates,

            'Accepting_Backpackers': Accepting_Backpackers,
            'Accepting_Students': Accepting_Students,
            'Accepting_Smokers': Accepting_Smokers,
            'Accepting_LGBTI': Accepting_LGBTI,
            'Accepting_years_olds': Accepting_years_olds,
            'Accepting_Children': Accepting_Children,
            'Accepting_Pets': Accepting_Pets,
            'Accepting_Retirees': Accepting_Retirees,
            'Accepting_On_welfare': Accepting_On_welfare,


            'Flatmate_Preference_name': Flatmate_Preference_name,
            'image_id': image_id,




            'Room_availability_Date': Room_availability_Date,
            'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
            'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
            'room_Weekly_rent': room_Weekly_rent,
            'room_changed_Bond': room_changed_Bond,
            'room_changed_Bills': room_changed_Bills,
            'Bed_Size': Bed_Size,
            'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
            'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
            'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
            'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
            'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
            'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
            'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
            'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
            'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
            'Room_furnishings_features_TV': Room_furnishings_features_TV,
            'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
            'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
            'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
            'Room_name': Room_name,
            'Room_type': Room_type,
            'Room_furnishings': Room_furnishings,
            'Bathroom_type': Bathroom_type,
            'property_Who_currently_lives': property_Who_currently_lives,
            'Property_Address': Property_Address,
            'property_bedrooms': property_bedrooms,
            'property_bathrooms': property_bathrooms,
            'changed_Parking': changed_Parking,
            'changed_Internet': changed_Internet,
            'offering_accommodation': offering_accommodation,
            'property': property,

        }


        return render(request, 'Flatmate_Preference.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def Flatmate_Preference_Accepting(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:



        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')





        # hidden part



        image_id = request.POST.get('image_id')

        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')


        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')




        print('nonononoonnnoononono')
        print('Accepting_Backpackers')
        print(Accepting_Backpackers)
        print(Accepting_Students)
        print(Accepting_Smokers)
        print(Accepting_LGBTI)
        print(Accepting_years_olds)
        print(Accepting_Children)
        print(Accepting_Pets)
        print(Accepting_Retirees)
        print(Accepting_On_welfare)

        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)





        contex = {



            'introduce_great_about_living': introduce_great_about_living,

            'introduce_about_your_flatmates': introduce_about_your_flatmates,

            'Accepting_Backpackers': Accepting_Backpackers,
            'Accepting_Students': Accepting_Students,
            'Accepting_Smokers': Accepting_Smokers,
            'Accepting_LGBTI': Accepting_LGBTI,
            'Accepting_years_olds': Accepting_years_olds,
            'Accepting_Children': Accepting_Children,
            'Accepting_Pets': Accepting_Pets,
            'Accepting_Retirees': Accepting_Retirees,
            'Accepting_On_welfare': Accepting_On_welfare,


            'Flatmate_Preference_name': Flatmate_Preference_name,
            # 'Property_and_room_images_1': Property_and_room_images_1,
            # 'Property_and_room_images_2': Property_and_room_images_2,
            # 'Property_and_room_images_3': Property_and_room_images_3,
            # 'Property_and_room_images_4': Property_and_room_images_4,
            # 'Property_and_room_images_5': Property_and_room_images_5,

            'image_id': image_id,

            'Room_availability_Date': Room_availability_Date,
            'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
            'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
            'room_Weekly_rent': room_Weekly_rent,
            'room_changed_Bond': room_changed_Bond,
            'room_changed_Bills': room_changed_Bills,
            'Bed_Size': Bed_Size,
            'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
            'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
            'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
            'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
            'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
            'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
            'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
            'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
            'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
            'Room_furnishings_features_TV': Room_furnishings_features_TV,
            'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
            'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
            'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
            'Room_name': Room_name,
            'Room_type': Room_type,
            'Room_furnishings': Room_furnishings,
            'Bathroom_type': Bathroom_type,
            'property_Who_currently_lives': property_Who_currently_lives,
            'Property_Address': Property_Address,
            'property_bedrooms': property_bedrooms,
            'property_bathrooms': property_bathrooms,
            'changed_Parking': changed_Parking,
            'changed_Internet': changed_Internet,
            'offering_accommodation': offering_accommodation,
            'property': property,

        }




        return render(request, 'Flatmate_Preference_Accepting.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')






def introduce_yourself(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:


        # hidden part
        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')
        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')


        image_id = request.POST.get('image_id')

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')

        introduce_great_about_living = request.POST.get('introduce_great_about_living')

        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')



        print('nonononoonnnoononono')
        print('Accepting_Backpackers')
        print(Accepting_Backpackers)
        print(Accepting_Students)
        print(Accepting_Smokers)
        print(Accepting_LGBTI)
        print(Accepting_years_olds)
        print(Accepting_Children)
        print(Accepting_Pets)
        print(Accepting_Retirees)
        print(Accepting_On_welfare)

        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        contex = {

            'introduce_great_about_living': introduce_great_about_living,

            'introduce_about_your_flatmates': introduce_about_your_flatmates,

            'Accepting_Backpackers': Accepting_Backpackers,
            'Accepting_Students': Accepting_Students,
            'Accepting_Smokers': Accepting_Smokers,
            'Accepting_LGBTI': Accepting_LGBTI,
            'Accepting_years_olds': Accepting_years_olds,
            'Accepting_Children': Accepting_Children,
            'Accepting_Pets': Accepting_Pets,
            'Accepting_Retirees': Accepting_Retirees,
            'Accepting_On_welfare': Accepting_On_welfare,

            'Flatmate_Preference_name': Flatmate_Preference_name,


            'image_id': image_id,
            'Room_availability_Date': Room_availability_Date,
            'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
            'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
            'room_Weekly_rent': room_Weekly_rent,
            'room_changed_Bond': room_changed_Bond,
            'room_changed_Bills': room_changed_Bills,
            'Bed_Size': Bed_Size,
            'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
            'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
            'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
            'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
            'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
            'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
            'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
            'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
            'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
            'Room_furnishings_features_TV': Room_furnishings_features_TV,
            'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
            'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
            'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
            'Room_name': Room_name,
            'Room_type': Room_type,
            'Room_furnishings': Room_furnishings,
            'Bathroom_type': Bathroom_type,
            'property_Who_currently_lives': property_Who_currently_lives,
            'Property_Address': Property_Address,
            'property_bedrooms': property_bedrooms,
            'property_bathrooms': property_bathrooms,
            'changed_Parking': changed_Parking,
            'changed_Internet': changed_Internet,
            'offering_accommodation': offering_accommodation,
            'property': property,

        }




        return render(request, 'introduce_yourself.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')





def introduce_yourself_about_your_flatmates(request):

    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        introduce_great_about_living = request.POST.get('introduce_great_about_living')
        print('introduce_great_about_livingllllllllllllllll')
        print(introduce_great_about_living)

        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')


        # hidden part
        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')
        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')
        image_id = request.POST.get('image_id')


        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')



        print('nonononoonnnoononono')

        print('introduce_about_your_flatmates')
        print(introduce_about_your_flatmates)


        print('Accepting_Backpackers')
        print(Accepting_Backpackers)
        print(Accepting_Students)
        print(Accepting_Smokers)
        print(Accepting_LGBTI)
        print(Accepting_years_olds)
        print(Accepting_Children)
        print(Accepting_Pets)
        print(Accepting_Retirees)
        print(Accepting_On_welfare)

        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        contex = {

            'introduce_great_about_living': introduce_great_about_living,
            'introduce_about_your_flatmates': introduce_about_your_flatmates,


            'Accepting_Backpackers': Accepting_Backpackers,
            'Accepting_Students': Accepting_Students,
            'Accepting_Smokers': Accepting_Smokers,
            'Accepting_LGBTI': Accepting_LGBTI,
            'Accepting_years_olds': Accepting_years_olds,
            'Accepting_Children': Accepting_Children,
            'Accepting_Pets': Accepting_Pets,
            'Accepting_Retirees': Accepting_Retirees,
            'Accepting_On_welfare': Accepting_On_welfare,
            'Flatmate_Preference_name': Flatmate_Preference_name,
            # 'Property_and_room_images_1': Property_and_room_images_1,
            # 'Property_and_room_images_2': Property_and_room_images_2,
            # 'Property_and_room_images_3': Property_and_room_images_3,
            # 'Property_and_room_images_4': Property_and_room_images_4,
            # 'Property_and_room_images_5': Property_and_room_images_5,

            'image_id': image_id,
            'Room_availability_Date': Room_availability_Date,
            'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
            'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
            'room_Weekly_rent': room_Weekly_rent,
            'room_changed_Bond': room_changed_Bond,
            'room_changed_Bills': room_changed_Bills,
            'Bed_Size': Bed_Size,
            'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
            'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
            'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
            'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
            'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
            'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
            'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
            'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
            'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
            'Room_furnishings_features_TV': Room_furnishings_features_TV,
            'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
            'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
            'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
            'Room_name': Room_name,
            'Room_type': Room_type,
            'Room_furnishings': Room_furnishings,
            'Bathroom_type': Bathroom_type,
            'property_Who_currently_lives': property_Who_currently_lives,
            'Property_Address': Property_Address,
            'property_bedrooms': property_bedrooms,
            'property_bathrooms': property_bathrooms,
            'changed_Parking': changed_Parking,
            'changed_Internet': changed_Internet,
            'offering_accommodation': offering_accommodation,
            'property': property,

        }






        return render(request, 'introduce_yourself_about_your_flatmates.html', contex)


    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')

def introduce_great_about_living_here(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        introduce_great_about_living = request.POST.get('introduce_great_about_living')


        # hidden part
        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')
        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')
        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')
        image_id = request.POST.get('image_id')
        # Property_and_room_images_1 = request.FILES.get('Property_and_room_images_1')
        # Property_and_room_images_2 = request.POST.get('Property_and_room_images_2')
        # Property_and_room_images_3 = request.POST.get('Property_and_room_images_3')
        # Property_and_room_images_4 = request.POST.get('Property_and_room_images_4')
        # Property_and_room_images_5 = request.POST.get('Property_and_room_images_5')
        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')


        print('nonononoonnnoononono')
        print('introduce_great_about_living')
        print(introduce_great_about_living)

        print('introduce_about_your_flatmates')
        print(introduce_about_your_flatmates)

        print('Accepting_Backpackers')
        print(Accepting_Backpackers)
        print(Accepting_Students)
        print(Accepting_Smokers)
        print(Accepting_LGBTI)
        print(Accepting_years_olds)
        print(Accepting_Children)
        print(Accepting_Pets)
        print(Accepting_Retirees)
        print(Accepting_On_welfare)

        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        contex = {

            'introduce_great_about_living': introduce_great_about_living,

            'introduce_about_your_flatmates': introduce_about_your_flatmates,
            'Accepting_Backpackers': Accepting_Backpackers,
            'Accepting_Students': Accepting_Students,
            'Accepting_Smokers': Accepting_Smokers,
            'Accepting_LGBTI': Accepting_LGBTI,
            'Accepting_years_olds': Accepting_years_olds,
            'Accepting_Children': Accepting_Children,
            'Accepting_Pets': Accepting_Pets,
            'Accepting_Retirees': Accepting_Retirees,
            'Accepting_On_welfare': Accepting_On_welfare,
            'Flatmate_Preference_name': Flatmate_Preference_name,
            # 'Property_and_room_images_1': Property_and_room_images_1,
            # 'Property_and_room_images_2': Property_and_room_images_2,
            # 'Property_and_room_images_3': Property_and_room_images_3,
            # 'Property_and_room_images_4': Property_and_room_images_4,
            # 'Property_and_room_images_5': Property_and_room_images_5,
            'image_id': image_id,
            'Room_availability_Date': Room_availability_Date,
            'Room_availability_Minimum_length_stay': Room_availability_Minimum_length_stay,
            'Room_availability_Maximum_length_stay': Room_availability_Maximum_length_stay,
            'room_Weekly_rent': room_Weekly_rent,
            'room_changed_Bond': room_changed_Bond,
            'room_changed_Bills': room_changed_Bills,
            'Bed_Size': Bed_Size,
            'Room_furnishings_features_Bed_side_table': Room_furnishings_features_Bed_side_table,
            'Room_furnishings_features_Wardrobe': Room_furnishings_features_Wardrobe,
            'Room_furnishings_features_Drawers': Room_furnishings_features_Drawers,
            'Room_furnishings_features_Air_conditioner': Room_furnishings_features_Air_conditioner,
            'Room_furnishings_features_Heater': Room_furnishings_features_Heater,
            'Room_furnishings_features_Desk': Room_furnishings_features_Desk,
            'Room_furnishings_features_Lamp': Room_furnishings_features_Lamp,
            'Room_furnishings_features_Chair': Room_furnishings_features_Chair,
            'Room_furnishings_features_Couch': Room_furnishings_features_Couch,
            'Room_furnishings_features_TV': Room_furnishings_features_TV,
            'Room_furnishings_features_Balcony': Room_furnishings_features_Balcony,
            'Room_furnishings_features_Door_lock': Room_furnishings_features_Door_lock,
            'Room_furnishings_features_Kitchenette': Room_furnishings_features_Kitchenette,
            'Room_name': Room_name,
            'Room_type': Room_type,
            'Room_furnishings': Room_furnishings,
            'Bathroom_type': Bathroom_type,
            'property_Who_currently_lives': property_Who_currently_lives,
            'Property_Address': Property_Address,
            'property_bedrooms': property_bedrooms,
            'property_bathrooms': property_bathrooms,
            'changed_Parking': changed_Parking,
            'changed_Internet': changed_Internet,
            'offering_accommodation': offering_accommodation,
            'property': property,

        }






        return render(request, 'introduce_great_about_living_here.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')


def Preview_Listing_for_House(request):
    session_user_id = request.session.get('session_user_id')

    if session_user_id:

        # hidden part
        introduce_great_about_living = request.POST.get('introduce_great_about_living')
        introduce_about_your_flatmates = request.POST.get('introduce_about_your_flatmates')
        Accepting_Backpackers = request.POST.get('Accepting_Backpackers')
        Accepting_Students = request.POST.get('Accepting_Students')
        Accepting_Smokers = request.POST.get('Accepting_Smokers')
        Accepting_LGBTI = request.POST.get('Accepting_LGBTI')
        Accepting_years_olds = request.POST.get('Accepting_years_olds')
        Accepting_Children = request.POST.get('Accepting_Children')
        Accepting_Pets = request.POST.get('Accepting_Pets')
        Accepting_Retirees = request.POST.get('Accepting_Retirees')
        Accepting_On_welfare = request.POST.get('Accepting_On_welfare')
        Flatmate_Preference_name = request.POST.get('Flatmate_Preference_name')
        # Property_and_room_images_1 = request.FILES.get('Property_and_room_images_1')
        # Property_and_room_images_2 = request.POST.get('Property_and_room_images_2')
        # Property_and_room_images_3 = request.POST.get('Property_and_room_images_3')
        # Property_and_room_images_4 = request.POST.get('Property_and_room_images_4')
        # Property_and_room_images_5 = request.POST.get('Property_and_room_images_5')
        image_id = request.POST.get('image_id')
        Room_availability_Date = request.POST.get('Room_availability_Date')
        Room_availability_Minimum_length_stay = request.POST.get('Room_availability_Minimum_length_stay')
        Room_availability_Maximum_length_stay = request.POST.get('Room_availability_Maximum_length_stay')
        room_Weekly_rent = request.POST.get('room_Weekly_rent')
        room_changed_Bond = request.POST.get('room_changed_Bond')
        room_changed_Bills = request.POST.get('room_changed_Bills')
        Bed_Size = request.POST.get('Bed_Size')
        Room_furnishings_features_Bed_side_table = request.POST.get('Room_furnishings_features_Bed_side_table')
        Room_furnishings_features_Wardrobe = request.POST.get('Room_furnishings_features_Wardrobe')
        Room_furnishings_features_Drawers = request.POST.get('Room_furnishings_features_Drawers')
        Room_furnishings_features_Air_conditioner = request.POST.get('Room_furnishings_features_Air_conditioner')
        Room_furnishings_features_Heater = request.POST.get('Room_furnishings_features_Heater')
        Room_furnishings_features_Desk = request.POST.get('Room_furnishings_features_Desk')
        Room_furnishings_features_Lamp = request.POST.get('Room_furnishings_features_Lamp')
        Room_furnishings_features_Chair = request.POST.get('Room_furnishings_features_Chair')
        Room_furnishings_features_Couch = request.POST.get('Room_furnishings_features_Couch')
        Room_furnishings_features_TV = request.POST.get('Room_furnishings_features_TV')
        Room_furnishings_features_Balcony = request.POST.get('Room_furnishings_features_Balcony')
        Room_furnishings_features_Door_lock = request.POST.get('Room_furnishings_features_Door_lock')
        Room_furnishings_features_Kitchenette = request.POST.get('Room_furnishings_features_Kitchenette')
        Room_name = request.POST.get('Room_name')
        Room_type = request.POST.get('Room_type')
        Room_furnishings = request.POST.get('Room_furnishings')
        Bathroom_type = request.POST.get('Bathroom_type')
        property_Who_currently_lives = request.POST.get('property_Who_currently_lives')
        Property_Address = request.POST.get('Property_Address')
        property_bedrooms = request.POST.get('property_bedrooms')
        property_bathrooms = request.POST.get('property_bathrooms')
        changed_Parking = request.POST.get('changed_Parking')
        changed_Internet = request.POST.get('changed_Internet')
        offering_accommodation = request.POST.get('offering_accommodation')
        property = request.POST.get('property')

        print('nonononoonnnoononono')
        print('introduce_great_about_living')
        print(introduce_great_about_living)

        print('introduce_about_your_flatmates')
        print(introduce_about_your_flatmates)

        print('Accepting_Backpackers')
        print(Accepting_Backpackers)
        print(Accepting_Students)
        print(Accepting_Smokers)
        print(Accepting_LGBTI)
        print(Accepting_years_olds)
        print(Accepting_Children)
        print(Accepting_Pets)
        print(Accepting_Retirees)
        print(Accepting_On_welfare)

        print('Flatmate_Preference_name')
        print(Flatmate_Preference_name)

        print('hidden')
        # print('Property_and_room_images_1')
        # print(Property_and_room_images_1)
        # print(Property_and_room_images_2)
        # print(Property_and_room_images_3)
        # print(Property_and_room_images_4)
        # print(Property_and_room_images_5)
        print('Room_availability_Date')
        print(Room_availability_Date)
        print(Room_availability_Minimum_length_stay)
        print(Room_availability_Maximum_length_stay)
        print('room_Weekly_rent')
        print(room_Weekly_rent)
        print(room_changed_Bond)
        print(room_changed_Bills)
        print('Bed_Size')
        print(Bed_Size)
        print(Room_furnishings_features_Bed_side_table)
        print(Room_furnishings_features_Wardrobe)
        print(Room_furnishings_features_Drawers)
        print(Room_furnishings_features_Air_conditioner)
        print(Room_furnishings_features_Heater)
        print(Room_furnishings_features_Desk)
        print(Room_furnishings_features_Lamp)
        print(Room_furnishings_features_Chair)
        print(Room_furnishings_features_Couch)
        print(Room_furnishings_features_TV)
        print(Room_furnishings_features_Balcony)
        print(Room_furnishings_features_Door_lock)
        print(Room_furnishings_features_Kitchenette)
        print(Room_name)
        print(Room_type)
        print(Room_furnishings)
        print(Bathroom_type)
        print(property_Who_currently_lives)
        print(Property_Address)
        print(property_bedrooms)
        print(property_bathrooms)
        print(changed_Parking)
        print(changed_Internet)
        print(offering_accommodation)
        print(property)

        print(image_id)
        print(image_id)
        print(image_id)
        print(image_id)
        print(image_id)
        print(image_id)
        print(image_id)


        user_info = User_info_table.objects.get(id=session_user_id)

        if offering_accommodation and changed_Internet and changed_Parking and property_bathrooms and property_bedrooms and Property_Address and property_Who_currently_lives and Room_name and Room_type and Room_furnishings and Bathroom_type and room_Weekly_rent and room_changed_Bond and room_changed_Bills and Room_availability_Date and Room_availability_Minimum_length_stay and Room_availability_Maximum_length_stay and Flatmate_Preference_name and introduce_great_about_living and introduce_about_your_flatmates:
            print('say hello')
            going_for_save = listing_of_accommodationthat_seller_offering(link_with_user=user_info, Type_of_user_seller_or_finder='Seller', model_offering_accommodation=offering_accommodation, model_property = property, model_Property_Address=Property_Address, model_property_bedrooms=property_bedrooms, model_property_bathrooms=property_bathrooms, model_Parking = changed_Parking, model_Internet=changed_Internet, model_Total_number_of_flatmates=property_Who_currently_lives, model_Room_name=Room_name, model_Room_type=Room_type, model_Room_furnishings=Room_furnishings, model_Bathroom_type=Bathroom_type, model_Bed_Size=Bed_Size, model_Room_furnishings_features_Bed_side_table=Room_furnishings_features_Bed_side_table, model_Room_furnishings_features_Wardrobe=Room_furnishings_features_Wardrobe, model_Room_furnishings_features_Drawers=Room_furnishings_features_Drawers, model_Room_furnishings_features_Air_conditioner=Room_furnishings_features_Air_conditioner, model_Room_furnishings_features_Heater=Room_furnishings_features_Heater, model_Room_furnishings_features_Desk=Room_furnishings_features_Desk, model_Room_furnishings_features_Lamp=Room_furnishings_features_Lamp, model_Room_furnishings_features_Chair=Room_furnishings_features_Chair, model_Room_furnishings_features_Couch=Room_furnishings_features_Couch, model_Room_furnishings_features_TV=Room_furnishings_features_TV, model_Room_furnishings_features_Balcony=Room_furnishings_features_Balcony, model_Room_furnishings_features_Door_lock=Room_furnishings_features_Door_lock, model_Room_furnishings_features_Kitchenette = Room_furnishings_features_Kitchenette, model_room_Weekly_rent=room_Weekly_rent, model_room_changed_Bond=room_changed_Bond, model_room_changed_Bills=room_changed_Bills, model_Room_availability_Date=Room_availability_Date, model_Room_availability_Minimum_length_stay=Room_availability_Minimum_length_stay, model_Room_availability_Maximum_length_stay=Room_availability_Maximum_length_stay, model_Flatmate_Preference_name=Flatmate_Preference_name, model_Accepting_Backpackers=Accepting_Backpackers, model_Accepting_Students=Accepting_Students, model_Accepting_Smokers=Accepting_Smokers, model_Accepting_LGBTI=Accepting_LGBTI, model_Accepting_years_olds=Accepting_years_olds, model_Accepting_Children=Accepting_Children, model_Accepting_Pets=Accepting_Pets, model_Accepting_Retirees=Accepting_Retirees, model_Accepting_On_welfare=Accepting_On_welfare, model_introduce_about_your_flatmates=introduce_about_your_flatmates, model_introduce_great_about_living=introduce_great_about_living)

            going_for_save.save()


            get_the_main = listing_of_accommodationthat_seller_offering.objects.get(id=going_for_save.id)


            #making string to list for image
            k = image_id[1:len(image_id) - 1]
            print(k)
            lit_img = []
            p = k.split(", ")
            if p and p != ['']:
                for i in p:
                    lit_img.append(int(i))


                if lit_img:
                    for i in lit_img:

                        subc1 = accommodationthat_seller_offering_image.objects.get(id=i)
                        get_the_main.model_Property_and_room_images_1.add(subc1)
                        get_the_main.save()
        else:



            print('fast page')

        get_the_main_tabel_value = listing_of_accommodationthat_seller_offering.objects.get(id=going_for_save.id)

        contex = {

            'get_the_main_tabel_value':get_the_main_tabel_value,

        }



        return render(request, 'Preview_Listing_for_House.html', contex)

    messages.warning(request, 'Please login to create a list')
    return redirect('going_for_login')



@csrf_exempt
def lets_delete_the_image(request):
    this_value = request.POST.get('this_value')
    print('this_value')
    print(this_value)
    ko = accommodationthat_seller_offering_image.objects.get(id = this_value)
    ko.delete()

    return HttpResponse('Done')