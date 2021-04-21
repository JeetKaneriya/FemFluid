from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.mail import get_connection, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import requests
from .models import Admin, user


# Create your views here.

def ip_save(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ""

    # ip = '27.61.178.47'           #Ahmedabad
    # ip = '49.34.237.43'           #Ahmedabad
    # ip = '27.109.30.30'           #Himatnagar
    # ip = '38.28.46.134'           #New York
    # ip = '216.178.47.230'         #Los Angeles

    # ip-api for geolocation
    api = 'http://ip-api.com/json/' + ip

    gip = requests.get(api)
    res = gip.json()

    if ip == "127.0.0.1":
        city = "localhost"
        state = "-"
        country = "-"
    else:
        city = res['city']
        state = res['regionName']
        country = res['country']

    #timezone = res['timezone']

    dt = datetime.now()
    date = dt.strftime('%d-%m-%Y')
    time = dt.strftime('%H : %M : %S')

    login_list = user.objects.all()

    flag = "False"
    o_user = user()

    if len(login_list) > 0:
        for i in range(len(login_list)):
            if city == login_list[i].city:
                count = login_list[i].count
                o_user = user(ip=ip, city=city, state=state, country=country, count=(count + 1), date=date, time=time)
                flag = "True"

        if flag == "False":
            o_user = user(ip=ip, city=city, state=state, country=country, count=1, date=date, time=time)

    else:
        o_user = user(ip=ip, city=city, state=state, country=country, count=1, date=date, time=time)

    o_user.save()
    request.session['ipCheck'] = True


def home(request):
    status = {"run": 2}
    request.session['login'] = False

    if not request.session.get('ipCheck', False):
        ip_save(request)

    if request.method == 'POST':

        # Reading data for the user complaint
        subject = "Response from the client through contact us"
        from_email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        contact_num = request.POST['contact-num']
        designation = request.POST['designation']
        formatted_message = '<center><div style="width:600px"><img src="https://femfluid.herokuapp.com/static/assets/images/Email-Header.png" style="margin-bottom: 50px; width:100%;"><p style="color:#0b5394; font-size:14px; text-align: left; margin-left:30px; ">From <strong>' + name + '</strong>,<br><br>' + message + '<br><br>Contact no. : <strong>' + contact_num + '</strong><br>Designation : <strong>' + designation + '</strong></p><p style="text-align: left"><strong><strong><br></strong></strong></p><div style="background-color:#2A58A3; padding:1px 0"><p style="text-align: center;color:#fff; font-size: 12px; font-weight: 300; letter-spacing: 0.5px;"><strong><strong>Copyright © 2021 <a href="https://fem-fluid.herokuapp.com/" style="color:#fff; text-decoration:none;">FEM FLUID</a> | Designed by <a href="https://www.linkedin.com/in/coding-comrades-654b3120a/" style="color:#fff; text-decoration:none;" target="blank">Cod\'rades</a></strong></strong></p></div></div></center>'
        to_email_list = ['jeet352002@gmail.com', 'hitpatel1107@gmail.com', 'tandelneelkanth@gmail.com']

        # Computing data for the auto-generated mail
        response_subject = "Thank you for getting in touch!"
        response_mail = '<center><div style="width:600px"><img src="https://femfluid.herokuapp.com/static/assets/images/Email-Header.png" style="margin-bottom: 50px; width:100%;"><p style="color:#0b5394; font-size:14px; text-align: left; margin-left:30px; ">Dear <strong>' + name + '</strong>,<br><br>We appreciate you contacting us.<br>One of our colleagues will get back in touch with you soon!<br><br>Have a great day!<br><br><strong>From Cod\'rades Team.</strong></p><p style="text-align: left"><strong><strong><br></strong></strong></p><div style="background-color:#2A58A3; padding:1px 0"><p style="text-align: center;color:#fff; font-size: 12px; font-weight: 300; letter-spacing: 0.5px;"><strong><strong>Copyright © 2021 <a href="http://fem-fluid.herokuapp.com/" style="color:#fff; text-decoration:none;">FEM FLUID</a> | Designed by <a href="https://www.linkedin.com/in/coding-comrades-654b3120a/" style="color:#fff; text-decoration:none;" target="blank">Cod\'rades</a></strong></strong></p></div></div></center>'

        # User complaint api details ( mailgun )
        complaint_host = 'smtp-relay.sendinblue.com'  # 'smtp.mailgun.org'
        complaint_port = 587
        complaint_username = 'jeet352002@gmail.com'  # 'postmaster@sandboxfbc7c0a359694fc9818c8520713fc6a5.mailgun.org'
        complaint_password = 'Mq67Ns0fzXGptFrD'  # '37d32e369ef3fe65622f1077aaf9e7bb-29561299-f6bb2df3'
        complaint_use_tls = True
        complaint_connection = get_connection(host=complaint_host, port=complaint_port, username=complaint_username, password=complaint_password, use_tls=complaint_use_tls)

        # Auto generated mail api details ( sendgrid )
        response_host = 'smtp-relay.sendinblue.com'  # 'smtp.sendgrid.net'
        response_port = 587
        response_username = 'jeet352002@gmail.com'  # 'apikey'
        response_password = 'Mq67Ns0fzXGptFrD'  # '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'
        response_use_tls = True
        response_connection = get_connection(host=response_host, port=response_port, username=response_username, password=response_password, use_tls=response_use_tls)

        try:
            send_mail(response_subject, response_mail, 'jeet352002@gmail.com', [from_email], fail_silently=False, connection=response_connection)
            send_mail(subject, formatted_message, from_email, to_email_list, fail_silently=False, connection=complaint_connection)
            status['run'] = 1
        except:
            status['run'] = 0

    return render(request, 'index.html', status)


def sd_series(request):
    return render(request, 'sd-series.html')


def mr_series(request):
    return render(request, 'mr-series.html')


def arm_series(request):
    return render(request, 'arm-series.html')


def elec_series(request):
    return render(request, 'elec-series.html')


def fluids_l(request):
    return render(request, 'fluids-l.html')


def paste(request):
    return render(request, 'paste.html')


def fluids_p(request):
    return render(request, 'fluids-p.html')


def dev(request):
    return render(request, 'dev-facility.html')


def test(request):
    return render(request, 'test-facility.html')


def prod(request):
    return render(request, 'prod-facility.html')


def admin_login(request):
    test = {"check": 2}
    request.session['login'] = False

    if request.method == 'POST':

        master_key = "123456789"

        ad1 = Admin()
        ad1.email = "jeet352002@gmail.com"
        ad1.password = master_key

        ad2 = Admin()
        ad2.email = "hitpatel1107@gmail.com"
        ad2.password = master_key

        ad3 = Admin()
        ad3.email = "tandelneelkanth@gmail.com"
        ad3.password = master_key

        ad_list = [ad1, ad2, ad3]

        email = request.POST['email']
        password = request.POST['password']

        flag = "False"

        for i in range(len(ad_list)):
            if ad_list[i].email == email:
                if ad_list[i].password == password:
                    flag = "True"

        if flag == "True":
            for i in range(len(ad_list)):
                if ad_list[i].email == email:
                    if ad_list[i].password == password:
                        request.session['login'] = True
                        test["check"] = 1
                        return redirect('https://femfluid.herokuapp.com/admin_login/stats')

        else:
            request.session['login'] = False
            test["check"] = 0

    return render(request, 'admin-login.html', test)


def stats(request):
    user_det = user.objects.all()

    if request.session.get('login'):
        return render(request, 'stats.html', {"user_det": user_det})

    else:
        return redirect('https://femfluid.herokuapp.com/admin_login')

def handler404(request, exception=None):
    url = request.get_full_path()
    response = render(request, '404.html', {"url": url})
    response.status_code = 404
    return response

def handler500(request, exception=None):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response

def Sitemap(request):
    return HttpResponse(open('sitemap.xml').read())