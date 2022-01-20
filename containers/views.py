from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Container
from django.http import HttpResponse
from .start_container import spawn_container


class ContainerList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Container
    context_object_name = 'container_list'
    template_name = 'containers/container_list.html'


class ContainerDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    model = Container
    template_name = 'containers/container_detail.html'


def startContainer(request):
    public_ip = None
    if request.method == 'POST':
        public_ip = spawn_container()
        print('success!')
    if public_ip:
        html = f"<html><body>IP: {public_ip}</body></html>"
    else:
        html = "<html><body>Failure!</body></html>"
    return HttpResponse(html)
