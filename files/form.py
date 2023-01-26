from django import forms
from .models import Archive

class ArchiveModelForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = ["type", "date", "value", "cpf", "card", "hour", "store_owner", "store_name"]