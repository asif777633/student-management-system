from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification

def HOME(request):
    return render(request,'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staf_id = i.id
        notification = Staff_Notification.objects.filter(staff_id = staf_id)

        context = {
            'notification' : notification,
        }
    return render(request,'Staff/notification.html',context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification =Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')