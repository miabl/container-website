from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from students.models import Student
from .models import Container, ContainerInstance
from django.http import HttpResponseRedirect


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
    def post(self, request, container_pk):
        student = Student.objects.get(user=request.user)
        if student.running_container:
            messages.error(request, 'You already have a container running. Please stop it before starting a new one.')
            return HttpResponseRedirect(reverse('container-instance-detail', kwargs={'pk':
                                                                                         student.running_container_id}))
        else:
            instance = ContainerInstance(container=Container.objects.get(pk=container_pk))
            instance.containerARN = instance.start_task()

            if instance.start_instance():
                print("getting ip")
                instance.public_ip = instance.get_ip()
                print(instance.public_ip)
                print("got ip, saving...")
                instance.save()

                student = Student.objects.get(user=request.user)
                student.running_container = instance
                student.save()

                return HttpResponseRedirect(reverse('container-instance-detail', kwargs={'pk': instance.pk}))

            else:
                return HttpResponseRedirect(reverse('failure'))


class FailedContainer(TemplateView):
    template_name = 'containers/failure.html'
