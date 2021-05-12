from django import forms


def check_for_k(value):
    if value[0].lower()=='k':
        raise forms.ValidationError('name should not start with k')

def check_for_length(value):
    if len(value)>5:
        raise forms.ValidationError('lengt is more than 5 chars')

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_k,check_for_length])
    email=forms.EmailField()
    reenteremail=forms.EmailField()

    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('reenteremail')
        if e!=r:
            raise forms.ValidationError('emails are not matched')
     


    



