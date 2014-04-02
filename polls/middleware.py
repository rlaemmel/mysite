# Following http://www.soyoucode.com/2011/really-disable-csrf-django

class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)