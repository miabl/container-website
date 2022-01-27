from django.forms import ModelForm

from units.models import Unit
from students.models import Student

from django.utils.translation import gettext_lazy as _


class EditUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['summary']
        labels = {'summary': _('Unit Description')}
        help_texts = {'summary': _('Enter a brief description of the unit')}


class EditAvailabilityForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['availability']
        labels = {'availability': _('Unit Availability')}
        help_texts = {'availability': _('Change the unit availability')}


class EditTitleForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['title']
        labels = {'title': _('Unit Title')}
        help_texts = {'title': _('Change the title of the unit')}


class EditContainersForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['containers']
        labels = {'containers': _('Unit Containers')}
        help_texts = {'containers': _('Change the containers listed')}


class EditTeachersForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['coordinator', 'lecturer', 'lab_facilitator']
        labels = {'coordinator': _('Unit Coordinator'), 'lecturer': _('Lecturer'),
                  'lab_facilitator': _('Lab Facilitator')}
        help_texts = {'coordinator': _('Change the Units Coordinator'), 'lecturer': _('Change the Units Lecturer'),
                      'lab_facilitator': _('Change the units lab facilitators')}


class AddUnit(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        initial = '__all__'

#
# class EnrolStudent(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['units']
#         labels = {'units': _('Units')}
#         help_texts = {'units': _('Change Enrolled Units')}
