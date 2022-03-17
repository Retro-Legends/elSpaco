from dataclasses import field, fields
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, DateInput, DateField, BooleanField
from .models import Cladire, Office, Desk, Employee, Remote
# from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Column
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class CladireForm(ModelForm):
    class Meta:
        model = Cladire
        fields = ['denCladire', 'adresaCladire', 'nrEtaje']
        labels = {
            'denCladire': ('Name'),
            'adresaCladire': ('Address'),
            'nrEtaje': ('Floor num.'),
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            # HTML('<h2>Create Building</h2>'),
            Field('denCladire'),
            Field('adresaCladire'),
            Field('nrEtaje'),

        )
        return helper

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'POST'

    #     self.helper.layout = Layout(
    #         Row(Column('denCladire')),
    #         Row(
    #             Column('adresaCladire'),
    #             Column('nrEtaje')
    #         ),
    #         FormActions(
    #             Submit('submit', 'Salvare'),
    #             # Submit('cancel', 'Cancel', css_class='btn btn-danger')
    #         )

    #     )


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = ('nameOffice', 'floor', 'building', 'deskCount',
                  'adminOffice', 'lengthOffice', 'widthOffice')
        labels = {
            'nameOffice': ('Office Name'),
            'floor': ('Floor'),
            'building': ('Building'),
            'deskCount': ('Desk Count'),
            'adminOffice': ('Administrator'),
            'lengthOffice': ('Length - cm'),
            'widthOffice': ('Width - cm')
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            # HTML('<h2>Create Office</h2>'),
            Field('nameOffice'),
            Field('floor'),
            Field('building'),
            Field('deskCount'),
            Field('adminOffice'),
            Field('lengthOffice'),
            Field('widthOffice')
            # Submit('submit', 'Submit obiect', css_class='btn-success')
        )
        return helper


class DeskForm(ModelForm):
    class Meta:
        model = Desk
        fields = ('office', 'deskCount', 'adminOffice',
                  'lengthDesk', 'widthDesk', 'isOccupied')
        labels = {
            'office': ('Office'),
            'deskCount': ('Desk count'),
            'adminOffice': ('Admin'),
            'lengthDesk': ('Length - cm'),
            'widthDesk': ('Width - cm'),
            'isOccupied': ('Occupied')
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            # HTML('<h2>Create Employee</h2>'),
            Field('office'),
            Field('deskCount'),
            Field('adminOffice'),
            Field('lengthDesk'),
            Field('widthDesk'),
            Field('isOccupied'),
        )
        return helper


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('firstName', 'lastName', 'role', 'gender',
                  'birthDate - yyyy-mm-dd', 'nationality', 'address', 'desk',  'isActive')
        labels = {
            'firstName': ('First name'),
            'lastName': ('Last name'),
            'role': ('Role'),
            'gender': ('Gender'),
            'birthDate': ('Birth date'),
            'nationality': ('nationality'),
            'address': ('Address'),
            'desk': ('Desk'),
            'isActive': ('Active')
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            HTML('<h2>Create Employee</h2>'),
            Field('firstName'),
            Field('lastName'),
            Field('role'),
            Field('gender'),
            Field('birthDate'),
            Field('nationality'),
            Field('address'),
            Field('desk'),
            Field('isActive'),
            Submit('submit', 'Submit obiect', css_class='btn-success')
        )
        return helper


class RemoteForm(ModelForm):
    class Meta:
        model = Remote
        fields = ('employee', 'startDate - yyyy-mm-dd', 'duration - days',
                  'isApproved', 'approvedBy')
        labels = {
            'employee': ('Employee'),
            'startDate': ('Start Date'),
            'duration': ('Duration'),
            'isApproved': ('Approved'),
            'approvedBy': ('Approved By')
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            # HTML('<h2>Create Employee</h2>'),
            Field('employee'),
            Field('startDate'),
            Field('duration'),
            Field('isApproved'),
            Field('approvedBy')

        )
        return helper
