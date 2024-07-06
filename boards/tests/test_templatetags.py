from django import forms
from django.test import SimpleTestCase
from ..templatetags import form_tags

class ExampleForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class FieldTypeTests(SimpleTestCase):
    def test_field_widget_type(self):
        form = ExampleForm()
        self.assertEqual('TextInput', form_tags.field_type(form['name']))
        self.assertEqual('PasswordInput', form_tags.field_type(form['password']))

class InputClassTests(SimpleTestCase):
    def test_unbound_field_initial_state(self):
        form = ExampleForm()  # unbound form
        self.assertEqual('form-control ', form_tags.input_class(form['name']))

    def test_valid_bound_field(self):
        form = ExampleForm({'name': 'john', 'password': '123'})  # bound form (field + data)
        self.assertEqual('form-control is-valid', form_tags.input_class(form['name']))

    def test_invalid_bound_field(self):
        form = ExampleForm({'name': '', 'password': '123'})  # bound form (field + data)
        self.assertEqual('form-control is-invalid', form_tags.input_class(form['name']))
