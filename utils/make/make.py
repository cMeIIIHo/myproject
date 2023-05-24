from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def make(request):
    msg = 'no params provided'
    if 'sdfsdf' in request.GET:
        msg = 'func here'

    return HttpResponse(msg)
