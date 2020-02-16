from django.forms import ModelForm

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:#which will allow us to set model
        model=Poll
        fields=['question','option_one','option_two','option_three']    