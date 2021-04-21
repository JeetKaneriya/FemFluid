from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.mail import get_connection, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
import pygeoip
import requests
import pytz
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

    """#Database for geolocation
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    res = gip.record_by_addr(ip)"""

    if ip == "127.0.0.1":
        city = "localhost"
        state = "-"
        country = "-"
    else:
        city = res['city']
        state = res['regionName']
        country = res['country']

    #timezone = res['timezone']

    dt = datetime.now(tz=pytz.UTC)
    dt_timezone = dt.astimezone(pytz.timezone('Asia/Kolkata'))
    date = dt_timezone.strftime('%A, %d-%m-%Y')
    time = dt_timezone.strftime('%H : %M : %S')

    login_list = user.objects.all()

    flag = "False"

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
    return render(request, 'index.html')


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