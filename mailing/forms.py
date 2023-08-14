from django import forms

from mailing.models import Email, SendingTry, MailingSetting, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs['class'] = 'CheckBoxForm'
            else:
                field.widget.attrs['class'] = 'form-control'


class EmailForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'


class MailingSettingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingSetting
        fields = ('date', 'time', 'periodicity', 'clients')