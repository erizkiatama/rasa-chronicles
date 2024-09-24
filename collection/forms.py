from django import forms

from main.models import User


class CollectionFilterForm(forms.Form):
    category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        choices=[("book", "Book"), ("movie", "Movie"), ("game", "Game")],
    )

    owner = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CollectionFilterForm, self).__init__(*args, **kwargs)
        self.fields['owner'].choices = [(user.id, user.nickname) for user in User.objects.all()]
