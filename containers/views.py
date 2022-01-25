from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from students.models import Student
from .models import Container, ContainerInstance
from django.http import HttpResponseRedirect
from .start_container import spawn_container


class ContainerList(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Container
    context_object_name = 'container_list'
    template_name = 'containers/container_list.html'


class ContainerDetail(LoginRequiredMixin, DetailView):
    login_url = 'accounts/login/'
    model = Container
    template_name = 'containers/container_detail.html'


class ContainerInstanceDetail(LoginRequiredMixin, DetailView):
    login_url = 'accounts/login'
    model = ContainerInstance
    template_name = 'containers/container_instance_detail.html'


class StartContainer(View):
    @staticmethod
    def post(request, container_pk):
        arn, ip = spawn_container()
        print('success!')
        if ip:
            instance = ContainerInstance(container=Container.objects.get(pk=container_pk), public_ip=ip,
                                         containerARN=arn)
            instance.save()

            student = Student.objects.get(user=request.user)
            student.running_container = instance
            student.save()

            return HttpResponseRedirect(reverse('container-instance-detail', kwargs={'pk': instance.pk}))

        else:
            return HttpResponseRedirect(reverse('failure'))


class FailedContainer(TemplateView):
    template_name = 'containers/failure.html'
