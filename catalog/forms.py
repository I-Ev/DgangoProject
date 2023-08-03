from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    stop_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description', 'price', 'category')
        # exclude = ('id', 'date_created', 'date_updated', 'is_active')

    def clean_name(self, words=stop_words):
        clean_data = self.cleaned_data['name'].lower()

        for word in words:
            if word in clean_data:
                raise forms.ValidationError('Есть запрещенные слова')

        return clean_data

    def clean_description(self, words=stop_words):
        clean_data = self.cleaned_data['description'].lower()

        for word in words:
            if word in clean_data:
                raise forms.ValidationError('Есть запрещенные слова')

        return clean_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'