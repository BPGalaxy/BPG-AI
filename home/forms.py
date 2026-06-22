from django import forms

from django import forms


class CharacterPrompt(forms.Form):
    Genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    Picture = forms.ImageField(
        label="Character Picture (optional)",
        required=False,
        widget=forms.FileInput(attrs={
            'accept': 'image/*',
            'class': 'picture-input',
        })
    )
    # --- Core Identity ---
    Name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"placeholder": "e.g. Elara"})
    )
    Gender = forms.ChoiceField(choices=Genders, label="Gender")
    Age = forms.IntegerField(label="Age", min_value=0, max_value=1000)
    Description = forms.CharField(
        label="Description",
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Add a short description of the character, e.g. "A witty and resourceful space smuggler with a mysterious past."',
            'class': 'textarea-form',
        })
    )
    Backstory = forms.CharField(
        label="Backstory",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Where are they from? What shaped them? Key life events.',
            'class': 'textarea-form',
        })
    )

    # --- Voice & Tone ---
    Tone = forms.CharField(
        label="Tone",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. dry and sarcastic, warm but guarded, blunt and impatient'
        })
    )
    SpeechStyle = forms.CharField(
        label="Speech style",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. short clipped sentences, uses slang, formal vocabulary'
        })
    )
    Behavior = forms.CharField(
        label="Additional behavior notes",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Anything else about how this character acts, e.g. shows affection through actions not words, avoids eye contact when lying.',
            'class': 'textarea-form',
        })
    )
    CharacteristicPhrases = forms.CharField(
        label="Characteristic phrases (optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. "Whatever.", "You wouldn\'t understand.", "Fine."'
        })
    )

    # --- Behavior ---
    BaselineMood = forms.CharField(
        label="Baseline Mood (optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. calm, cheerful, guarded'
        })
    )
    ReactsBadlyTo = forms.CharField(
        label="Reacts badly to (optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. rudeness, being ignored, personal questions'
        })
    )
    ReactsWellTo = forms.CharField(
        label="Reacts well to (optional)",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. humor, kindness, shared interests'
        })
    )


    OpeningLine = forms.CharField(
        label="Opening line",
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'The first thing the character says when the chat begins.',
            'class': 'textarea-form',
        })
    )    