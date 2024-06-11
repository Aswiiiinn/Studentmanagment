from django import forms
from .models import *

class imageForm(forms.ModelForm):
    class Meta:
        model = imageuploder1
        fields = '__all__'
class dropdwonForm(forms.ModelForm):
    class Meta:
        model = student_detail
        fields='__all__'
        def __init__(self,*args, **kwargs):
            super.__init__(*args, **kwargs)
            self.fields['city'].queryset =City.objects.none()
            self.fields['state'].queryset= State.objects.none()
            if 'country'in self.data:
                try:
                    country_id = int(self.data['country'])
                    self.fields['state'].queryset=State.objects.filter(country=country_id).order_by('name')
                    if 'state' in self.data:
                        state_id = int(self.data['state'])
                        self.fields['city'].queryset=City.objects.filter(state = state_id).order_by('name')
                    
                except(TypeError,ValueError):
                    pass
            elif self.instance.pk:
                if self.instance.country:
                    self.fields['state'].queryset = self.instance.country.state_set.order_by('name')
                if self.instance.state:
                    self.fields['city'].queryset = self.instance.state.city_set.order_by('name'
                                                                                     )
                    
                
                