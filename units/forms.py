from django.forms import ModelForm

from units.models import Unit

from django.utils.translation import gettext_lazy as _


class EditUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['title', 'code', 'summary', 'availability']
        labels = {'title': _('Unit Title'), 'code': _('Unit Code'), 'summary': _('Unit Description'),
                  'availability': _('Unit Availability')}
        help_texts = {'title': _('Change the title of the unit'), 'code': _('Change Unit Code'),
                      'summary': _('Enter a brief description of the unit'),
                      'availability': _('Change the unit availability')}


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
