from django import forms

from blog.models import BlogEntry


class BlogEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'CheckboxInput':
                field.widget.attrs['class'] = 'CheckBoxForm'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = BlogEntry
        # fields = '__all__'
        fields = ('title', 'body', 'preview')
        # exclude = ('id', 'date_created', 'date_updated', 'is_active')
