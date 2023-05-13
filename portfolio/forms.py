from django import forms

from portfolio.models import Assets


class MailingForm(forms.ModelForm):
    name_of_work = forms.ModelChoiceField(
        label='Название работы',
        queryset=Assets.objects.all(),
        widget=forms.Select(
            attrs={
                'placeholder':'Название',
                'class':'form-control js-example-basic-single'
            })
    )

    class Meta:
        model = Assets
        fields = [
            'id',
        ]