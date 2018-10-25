from django.http import HttpResponse


def chk(req):
    return HttpResponse('ok, service, %s, %s, %s' % (req.get_raw_uri(), req.get_full_path(), req.get_host()))
