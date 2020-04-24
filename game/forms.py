from django import forms

from .models import PlayerAlias


class NewPlayerAliasForm(forms.ModelForm):
    class Meta:
        model = PlayerAlias
        fields = ['alias']
        help_texts = {
            'alias': 'Choose a nickname',
        }
        widgets = {
            'alias': forms.TextInput(attrs={'placeholder': 'username'}),
        }


class JoinGameForm(forms.Form):
    gcode = forms.CharField(label='Game Code', max_length=5,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter the 5-letter code'}),
                            help_text="Ask the host for the game code")
    alias = forms.CharField(label='Your name', max_length=25, widget=forms.TextInput(attrs={'placeholder': 'username'}),
                            help_text="Choose a nickname")
