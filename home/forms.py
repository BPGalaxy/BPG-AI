from django import forms
from .models import Settings

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

class SettingsForm(forms.ModelForm):
    # Restricted choices instead of free text
    current_AI = forms.ChoiceField(
        choices=[("local", "Local"), ("online", "Online")],
    )
    AI_Status = forms.TypedChoiceField(
        choices=[(0, "Off"), (1, "On")],
        coerce=int,
    )
 
    class Meta:
        model = Settings
        fields = "__all__"
        widgets = {
            # render_value=False -> the key is never written into the HTML
            "API_KEY": forms.PasswordInput(attrs={"placeholder": "Leave blank to keep current key"}),
            "AI_name": forms.TextInput(attrs={"placeholder": "e.g. google/gemma-4-26b-a4b-it:free"}),
            "ANNOUNCEMENT_VERSION": forms.TextInput(attrs={"placeholder": "e.g. 1.0.0"}),
            "ANNOUNCEMENT_TEXT": forms.Textarea(attrs={"rows": 5}),
            "memoryLimit": forms.NumberInput(attrs={"style": "-moz-appearance: textfield;"}),
            "updateSummary": forms.NumberInput(attrs={"style": "-moz-appearance: textfield;"}),
            "nonrp_system_prompt": forms.Textarea(attrs={"rows": 5}),
            "rp_system_prompt": forms.Textarea(attrs={"rows": 5}),
        }

    OPTIONAL = ["today", "AI_name", "ANNOUNCEMENT_VERSION", "ANNOUNCEMENT_TEXT", "API_KEY", "nonrp_system_prompt", "rp_system_prompt"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.OPTIONAL:
            self.fields[name].required = False
            self.fields[name].empty_value = ""

    def clean_API_KEY(self):
        # blank submit = keep the existing key
        return self.cleaned_data.get("API_KEY") or self.instance.API_KEY

