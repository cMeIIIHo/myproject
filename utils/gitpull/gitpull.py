from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.conf import settings
from django.core.management import call_command
import subprocess


def sys_call(command, shell=True):
    return_code, output = 0, ''
    try:
        output = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=shell
        )
    except subprocess.CalledProcessError as err:
        return_code, output = err.returncode, err.output
    return return_code, output


@staff_member_required
def gitpull(request):
    if not request.user or not request.user.is_superuser:
        return HttpResponse('only_superuser')
    project_dir = settings.BASE_DIR
    sys_call('cd {}'.format(project_dir))

    return_code, output = sys_call('git pull --verbose')
    if int(return_code) != 0:
        return HttpResponse('{}, {}'.format(return_code, output))

    call_command('collectstatic', verbosity=0, interactive=False)
    # import uwsgi
    # uwsgi.reload()
    return_code, output = sys_call('sudo systemctl restart gunicorn')
    if int(return_code) != 0:
        return HttpResponse('{}, {}'.format(return_code, output))

    return HttpResponse('ok')
