from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Session_year,CustomUser,Student,Staff,Staff_Notification,Staff_leave
from django.contrib import messages




@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    # course_count = Course.objects.all().count()
    # subject_count= Subject.objects.all().count()


    student_gender_male = Student.objects.filter(gender = 'Male' ).count()
    student_gender_female = Student.objects.filter(gender = 'Female' ).count()


    context = {
        'student_count': student_count,
        'staff_count' : staff_count,
        # 'course_count' : course_count,
        # 'subject_count' : subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,


    }
    return render(request,'Hod/home.html',context)




@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')



    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request,'Hod/add_student.html',context)



@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    context = {
        'student':student,
    }
    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_year.objects.all()

    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Hod/edit_student.html',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')


        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username= username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()


        student = Student.objects.get(admin =student_id)
        student.address = address
        student.gender = gender

        coures = Course.objects.get(id =course_id)
        student.course_id = coures

        session_year = Session_year.objects.get(id = session_year_id)
        student.session_year_id = session_year
        student.save()
        messages.success(request,'Record Are Successfully updated !')
        return redirect('view_student')



    return render(request,'Hod/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Succesfully Deleted')
    return redirect('view_student')





# @login_required(login_url='/')
# def Add_COURSE(request):
#     if request.method == 'POST':
#         course_name = request.POST.get('course_name')

#         course = Course(
#             name = course_name,
#         )
#         course.save()
#         messages.success(request,'course Are successfully Created')
#         return redirect('add_coures')

#     return render(request,'Hod/add_course.html')

# @login_required(login_url='/')
# def VIEW_COURSE(request):
#     course = Course.objects.all()
#     context = {
#         'course':course,
#     }
#     return render(request,'Hod/view_course.html',context)

# @login_required(login_url='/')
# def EDIT_COURSE(request,id):
#     course = Course.objects.get(id= id)
#     context = {
#         'course': course,
#     }
#     return render(request,'Hod/edit_course.html',context)

# @login_required(login_url='/')
# def UPDATE_COURSE(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         course_id = request.POST.get('course_id')

#         course = Course.objects.get(id = course_id)
#         course.name = name
#         course.save()
#         messages.success(request,'course Are successfully updated')
#         return redirect('view_course')
#     return render(request, 'Hod/edit_course.html')

# @login_required(login_url='/')
# def DELETE_COURSE(request,id):
#     course = Course.objects.get(id = id)
#     course.delete()
#     messages.success(request,'course are successfully deleted')

#     return redirect('view_course')





















@login_required(login_url='/')
def ADD_STAFF(request):
    if request .method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken')
            return redirect('add_staff')

        else:
            user = CustomUser(first_name= first_name,last_name=last_name,email=email,username=username,profile_pic=profile_pic,user_type= 2)
            user.set_password(password)
            user.save()
            staff = Staff(
                admin = user,
                address = address,
                gender = gender

            )
            staff.save()
            messages.success(request,'Staff Are Successfuly Add')
            return redirect('add_staff')

    return render(request,'Hod/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()
    context ={
        'staff':staff,
    }
    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):

    staff = Staff.objects.get(id= id)
    context = {
        'staff':staff,
    }
    return render(request,'Hod/edit_staff.html',context)


@login_required(login_url='/')
def UPDATE_STAFF (request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email =  email
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic


        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,'Staff Is Successfuly updated')
        return redirect('view_staff')


    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF (request ,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,'Recoder Are Successfuly Deleted')
    return redirect('view_staff')

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_start')

        session = Session_year(
            session_start =session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,'Successfuly Created')
        return redirect('add_session')
    return render(request,'Hod/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_year.objects.all()

    context = {
        'session': session,
    }
    return render(request,'Hod/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_year.objects.filter(id= id)

    context ={
        'session': session,
    }
    return render(request,'Hod/edit_session.html',context)

@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_year(
            id = session_id,
            session_start =session_year_start,
            session_end = session_year_end

        )
        session.save()
        messages.success(request,'Session Are successfuly update')
        return redirect('view_session')

@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session = Session_year.objects.get(id= id)
    session.delete()
    messages.success(request,'Session Are Sueccessfully Delete')
    return redirect('view_session')


def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_nofification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context ={
        'staff':staff,
        'see_nofification' : see_nofification,
    }
    return render(request,'Hod/staff_notification.html',context)


def SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id =request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,

        )
        notification.save()
        messages.success(request,'notification Are Successfuly send')
        return redirect('staff_send_notification')


def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_leave.objects.all()

    context ={
        "staff_leave" : staff_leave,

    }
    return render(request,'Hod/staff_leave.html',context)


def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id =id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id = id)
    leave.status =2
    leave.save()
    return redirect('staff_leave_view')