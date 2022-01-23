# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
#
#
# class EditUnit(forms.Form):
#     change_title = forms.CharField(help_text="Change Unit Title")
#     change_summary = forms.CharField(help_text="Change Summary")
#     change_offering = forms.CharField(help_text="Change Offering")
#
#     def clean_change_title(self):
#         data = self.cleaned_data['change_title']
#         return data
#
#
# class ChangeStaff(forms.Form):
#     change_coordinator = forms.CharField(help_text="Change Coordinator")
#     change_lecturer = forms.CharField(help_text="Change Lecturer")
#     change_lab_facilitator = forms.CharField(help_text="Change Facilitator")
#
#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#         return data
