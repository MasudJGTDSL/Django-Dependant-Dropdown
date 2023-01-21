from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField, BS5Accordion

class PresentAddressForm(forms.ModelForm):
    class Meta:
        model = PresentAddress
        fields = '__all__'
        labels={
            'PersionName':'নামঃ',
            'Address1':'ঠিকানাঃ',
            'Address2':'  ',
            'Division':'বিভাগঃ',
            'District':'জেলাঃ',
            'Upazila':'উপজেলা/থানাঃ',
            'PostOffice':'ডাকঘরঃ',
            'PostalCode':'পোষ্ট কোডঃ'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # BS5Accordion(
            Row(
                Column(FloatingField('PersionName'), css_class='form-group mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(FloatingField('Address1'), css_class='form-group mb-0'),
                Column(FloatingField('Address2'), css_class='form-group mt-0'),
                css_class='form-row'
            ),
            Row(
                Column(FloatingField('Division'), css_class='form-group mb-0'),
                Column(FloatingField('District'), css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Upazila', css_class='form-group mb-0'),
                Column('PostOffice', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('PostalCode', css_class='form-group mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class="btn-primary")
        )
        # )
