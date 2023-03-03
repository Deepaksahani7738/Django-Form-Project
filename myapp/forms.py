from django import forms
from .models import students


class postdata(forms.ModelForm):
    class Meta:
        model=students
        fields=['name','LastName','Roll_No','Fees','address']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Enter Your Name'}),
            'LastName':forms.TextInput(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Enter Your LastName'}),
            'Roll_No':forms.TextInput(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Enter Your Roll No'}),
            'Fees':forms.TextInput(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Fees'}),
            'date':forms.TextInput(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Date',}),
            'address':forms.Textarea(attrs={'class':'form-control',
            'style':'max-width:300px','placeholder':'Enter Your Address Here !',}),
        }        
    
        
