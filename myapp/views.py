from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="user":
                    user = User_registration.objects.get(email=email)
                    request.session["email"] = email
                    request.session["id"] = user.id
                    return redirect('/user_home')
                
                elif user.usertype=="tailor":
                    user = Tailor_registration.objects.get(email=email)
                    if user.admin_approval:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/tailor_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
                elif user.usertype=="stylist":
                    user = Stylist_registration.objects.get(email=email)
                    if user.admin_approval:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/stylist_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')


    return render(request,"login.html")

def user_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="user")
        log.save()

        regi=User_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            email=email,
            login_id=log,
            profile_picture=profile_picture
        )
        regi.save()
        messages.info(request,"Registration successful,You can login now")

    return render(request,"user_registration.html")

def tailor_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="tailor")
        log.save()

        regi=Tailor_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            email=email,
            id_proof=id_proof,
            login_id=log,
            profile_picture=profile_picture
        )
        regi.save()
        messages.info(request,"Registration successful,Wait admin admin_approval")

    return render(request,"tailor_registration.html")

def stylist_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="stylist")
        log.save()

        regi=Stylist_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            email=email,
            id_proof=id_proof,
            login_id=log,
            profile_picture=profile_picture
        )
        regi.save()
        messages.info(request,"Registration successful,Wait admin admin_approval")

    return render(request,"stylist_registration.html")



###################### ADMIN ###################

def admin_home(request):

    return render(request,"admin/admin_home.html")

def admin_view_tailor_requests(request):

    tailors=Tailor_registration.objects.filter(admin_approval=False)

    return render(request,"admin/view_tailor_requests.html",{"tailors":tailors})

def admin_view_tailor_request_single(request):

    did=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=did)

    return render(request,"admin/view_tailor_request_single.html",{"tailor":tailor})


def admin_accept_tailor_request(request):

    did=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=did)
    tailor.admin_approval=True
    tailor.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/admin_view_tailor_requests')

def admin_reject_tailor_request(request):

    did=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=did)
    tailor.delete()
    log=Login_table.objects.get(id=tailor.login_id)
    log.delete()
    messages.info(request,"Rejected Sucessfully")

    return redirect('/admin_view_tailor_requests')

def admin_view_stylist_requests(request):

    stylists=Stylist_registration.objects.filter(admin_approval=False)

    return render(request,"admin/view_stylist_requests.html",{"stylists":stylists})

def admin_view_stylist_request_single(request):

    tid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=tid)

    return render(request,"admin/view_stylist_request_single.html",{"stylist":stylist})

def admin_accept_stylist_request(request):

    tid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=tid)
    stylist.admin_approval=True
    stylist.save()
    messages.info(request,"Accepted Sucessfully")

    return redirect('/admin_view_stylist_requests')

def admin_reject_stylist_request(request):

    tid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=tid)
    stylist.delete()
    log=Login_table.objects.get(id=stylist.login_id)
    log.delete()
    messages.info(request,"Rejected Sucessfully")

    return redirect('/admin_view_stylist_requests')

def admin_view_tailors(request):

    tailors=Tailor_registration.objects.filter(admin_approval=True)

    return render(request,"admin/admin_view_tailors.html",{"tailors":tailors})

def admin_view_tailor_single(request):

    did=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=did)

    return render(request,"admin/admin_view_tailor_single.html",{"tailor":tailor})

def admin_delete_tailor(request):

    did=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=did)
    tailor.delete()
    log=Login_table.objects.get(id=tailor.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_tailors')

def admin_view_stylists(request):

    stylists=Stylist_registration.objects.filter(admin_approval=True)

    return render(request,"admin/admin_view_stylists.html",{"stylists":stylists})

def admin_view_stylist_single(request):

    tid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=tid)

    return render(request,"admin/admin_view_stylist_single.html",{"stylist":stylist})

def admin_delete_stylist(request):

    tid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=tid)
    stylist.delete()
    log=Login_table.objects.get(id=stylist.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_stylists')

def admin_view_users(request):

    users=User_registration.objects.all()

    return render(request,"admin/admin_view_users.html",{"users":users})

def admin_view_user_single(request):

    uid=request.GET.get('id')
    user_obj=User_registration.objects.get(id=uid)

    return render(request,"admin/admin_view_user_single.html",{"user_obj":user_obj})

def admin_delete_user(request):

    uid=request.GET.get('id')
    user_obj=User_registration.objects.get(id=uid)
    user_obj.delete()
    log=Login_table.objects.get(username=user_obj.login_id)
    log.delete()
    messages.info(request,"Removed successfully")

    return redirect('/admin_view_users')

def admin_view_bookings(request):

    bookings=Work_request.objects.all()

    return render(request,"admin/admin_view_bookings.html",{"bookings":bookings})

def admin_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"admin/admin_view_feedbacks.html",{"feedbacks":feedbacks})

##################### TAILOR ###################

def tailor_home(request):

    return render(request,"tailor/tailor_home.html")

def tailor_view_work_requests(request):

    id=request.session['id']
    tailor_id=Tailor_registration.objects.get(id=id)
    works=Work_request.objects.filter(tailor_id=tailor_id)

    return render(request,"tailor/tailor_view_work_requests.html",{"works":works})

def tailor_accept_work(request):

    wid=request.GET.get('id')
    work=Work_request.objects.get(id=wid)

    work.accept_status=True
    work.accepted_on=timezone.now()
    work.save()

    messages.info(request,"Work accepted successfully")

    return redirect('/tailor_view_work_requests')

def tailor_sent_work_update_user(request):

    wid=request.GET.get('id')
    work=Work_request.objects.get(id=wid)

    if request.POST:
        price=request.POST['price']
        work.price=price
        delivery_date=request.POST['delivery_date']
        work.delivery_date=delivery_date

        work.save()
        messages.info(request,"Send successfully")
        return redirect('/tailor_view_work_requests')

    return render(request,"tailor/tailor_sent_work_update_user.html")

def tailor_view_user_messages(request):

    id=request.session['id']
    tailor_id=Tailor_registration.objects.get(id=id)
    chats=User_message_to_tailor.objects.filter(tailor_id=tailor_id)

    return render(request,"tailor/tailor_view_user_messages.html",{"chats":chats})

def tailor_reply_user(request):

    cid=request.GET.get('id')
    chat=User_message_to_tailor.objects.get(id=cid)

    if request.POST:
        reply=request.POST['reply']
        chat.reply=reply,
        chat.reply_on=timezone.now()
        chat.save()
        messages.info(request,"Reply sent successfully")
        return redirect('/tailor_view_user_messages')


#################### STYLIST ###################

def stylist_home(request):

    return render(request,"stylist/stylist_home.html")

def stylist_add_outfit_designs(request):

    id=request.session['id']
    stylist_id=Stylist_registration.objects.get(id=id)

    if request.POST:
        name=request.POST['name']
        description=request.POST['description']
        image=request.FILES['image']

        outfit=Add_outfit_designs.objects.create(
            name=name,
            description=description,
            image=image,
            stylist_id=stylist_id
        )
        outfit.save()
        messages.info(request,"Outfit added successfully")
        return redirect('/stylist_view_outfit_designs')

    return render(request,"stylist/stylist_add_outfit_designs.html")

def stylist_view_outfit_designs(request):

    id=request.session['id']
    stylist_id=Stylist_registration.objects.get(id=id)
    outfits=Add_outfit_designs.objects.filter(stylist_id=stylist_id)

    return render(request,"stylist/stylist_view_outfit_designs.html",{"outfits":outfits})

def stylist_view_outfit_design_single(request):

    oid=request.GET.get('id')
    outfit=Add_outfit_designs.objects.get(id=oid)

    return render(request,"stylist/stylist_view_outfit_design_single.html",{"outfit":outfit})

def stylist_update_outfit_design(request):

    oid=request.GET.get('id')
    outfit=Add_outfit_designs.objects.get(id=oid)

    if request.POST:
        name=request.POST['name']
        outfit.name=name
        description=request.POST['description']
        outfit.description=description
        image=request.FILES['image']
        outfit.image=image
        outfit.save()
        messages.info(request,"Updated Successfully")
        return redirect('/stylist_view_outfit_designs')

    return render(request,"stylist/stylist_update_outfit_design.html",{"outfit":outfit})

def stylist_remove_outfit_design(request):

    oid=request.GET.get('id')
    outfit=Add_outfit_designs.objects.get(id=oid)
    outfit.delete()
    messages.info(request,"Deleted successfully")

    return redirect('/stylist_view_outfit_designs')

def stylist_view_user_messages(request):

    id=request.session['id']
    stylist_id=Stylist_registration.objects.get(id=id)

    chats=User_message_to_stylist.objects.filter(stylist_id=stylist_id)

    return render(request,"stylist/stylist_view_user_messages.html",{"chats":chats})

def stylist_reply_user(request):

    cid=request.GET.get('id')
    chat=User_message_to_stylist.objects.get(id=cid)

    if request.POST:
        reply=request.POST['reply']
        chat.reply=reply,
        chat.reply_on=timezone.now()
        chat.save()
        messages.info(request,"Reply sent successfully")
        return redirect('/stylist_view_user_messages')



#################### USER ######################

def user_home(request):

    return render(request,"user/user_home.html")


def user_view_stylists(request):

    stylists=Stylist_registration.objects.filter(admin_approval=True)

    return render(request,"user/user_view_stylists.html",{"stylists":stylists})

def user_view_outfit_designs(request):

    sid=request.GET.get('id')
    stylist_id=Stylist_registration.objects.get(id=sid)
    outfit_designs=Add_outfit_designs.objects.filter(stylist_id=stylist_id)

    return render(request,"user/user_view_outfit_designs.html",
                  {
                      "outfit_designs":outfit_designs,
                      "stylist":stylist_id
                  })

def user_request_work_to_tailor(request):
    
    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    sid=request.GET.get('id')
    stylist_id=Stylist_registration.objects.get(id=sid)
    outfits=Add_outfit_designs.objects.filter(stylist_id=stylist_id)
    tailors=Tailor_registration.objects.filter(admin_approval=True)


    if request.POST:
        name=request.POST['name']
        details=request.POST['details']
        shipping_address=request.POST['shipping_address']
        contact=request.POST['contact']
        quantity=request.POST['quantity']
        tailor_id=request.POST['tailor_id']
        outfit_id=request.POST['outfit_id']

        tailor_id=Tailor_registration.objects.get(id=tailor_id)
        outfit_id=Add_outfit_designs.objects.get(id=outfit_id)

        request_work=Work_request.objects.create(
            name=name,
            details=details,
            shipping_address=shipping_address,
            contact=contact,
            quantity=quantity,
            request_on=timezone.now(),
            outfit_id=outfit_id,
            tailor_id=tailor_id,
            user_id=user_id
        )
        request_work.save()
        messages.info(request,"Request send successfully ")

    return render(request,"user/user_request_work_to_tailor.html",
                  {
                      "outfits":outfits,
                      "tailors":tailors
                    })

def user_view_work_requests(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    works=Work_request.objects.filter(user_id=user_id)

    return render(request,"user/user_view_work_requests.html",{"works":works})

def payment_user_for_work_tailor(request):

    wid=request.GET.get('id')
    work=Work_request.objects.get(id=wid)

    if request.POST:
        work.payment_status=True
        work.save()
        messages.info(request,"Payment sucessfull")
        return redirect('/user_view_work_requests')

    return render(request,"user/payment_user_for_work_tailor.html")

def user_message_to_stylist(request):

    sid=request.GET.get('id')
    stylist=Stylist_registration.objects.get(id=sid)
    uid=request.session['id']
    user_id=User_registration.objects.get(id=uid)

    if request.POST:
        message=request.POST['message']

        chat=User_message_to_stylist.objects.create(
            message=message,
            stylist_id=stylist,
            user_id=user_id,
            message_on=timezone.now()
        )
        chat.save()
        messages.info(request,"Message send successfully")
        return redirect('/user_view_messages_to_stylist')

    return render(request,"user/user_message_to_stylist.html",{"stylist":stylist})



def user_view_messages_to_stylist(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    chats=User_message_to_stylist.objects.filter(user_id=user_id)

    return render(request,"user/user_view_messages_to_stylist.html",{"chats":chats})

def user_view_tailors(request):

    tailors=Tailor_registration.objects.filter(admin_approval=True)

    return render(request,"user/user_view_tailors.html",{"tailors":tailors})

def user_message_to_tailor(request):

    sid=request.GET.get('id')
    tailor=Tailor_registration.objects.get(id=sid)
    uid=request.session['id']
    user_id=User_registration.objects.get(id=uid)

    if request.POST:
        message=request.POST['message']

        chat=User_message_to_tailor.objects.create(
            message=message,
            tailor_id=tailor,
            user_id=user_id,
            message_on=timezone.now()
        )
        chat.save()
        messages.info(request,"Message send successfully")
        return redirect('/user_view_messages_to_tailor')

    return render(request,"user/user_message_to_tailor.html",{"tailor":tailor})

def user_view_messages_to_tailor(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)
    chats=User_message_to_tailor.objects.filter(user_id=user_id)

    return render(request,"user/user_view_messages_to_tailor.html",{"chats":chats})

def user_add_feedback(request):

    id=request.session['id']
    user_id=User_registration.objects.get(id=id)

    if request.POST:
        feedback=request.POST['feedback']
        rating=request.POST['rating']

        feed=Feedback.objects.create(
            feedback=feedback,
            rating=rating,
            user_id=user_id,
            feedback_on=timezone.now()
        )
        feed.save()
        messages.info(request,"Feedback Sent successfully")
        return redirect('/user_view_feedbacks')


    return render(request,"user/user_add_feedback.html")

def user_view_feedbacks(request):

    feedbacks=Feedback.objects.all()

    return render(request,"user/user_view_feedbacks.html",{"feedbacks":feedbacks})
