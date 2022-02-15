from django.http import HttpResponse


def myview(request):
    num_visits = request.session.get('num_visits', 0)+1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))

    oldval = request.COOKIES.get('zap', None)
    if oldval:
        resp.set_cookie('zap', int(oldval)+1)
    else:
        resp.set_cookie('zap', 42)
    resp.set_cookie('sakaicar', 42, max_age=100)
    resp.set_cookie('dj4e_cookie', 'd44ea21d', max_age=1000)
    return resp