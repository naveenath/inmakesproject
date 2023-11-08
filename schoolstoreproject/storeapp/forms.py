from django import forms

from .models import Order
from department.models import Course


class PersonCreationForm(forms.ModelForm):

    class Meta:
        model = Order

        options = (
            ('male', 'male'),
            ('female', 'female')
        )
        fields =  '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            'age': forms.TextInput(attrs={"class": "form-control"}),
            'gender': forms.RadioSelect(attrs={"class": "form-control form-radioselect form-check-inline'"}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'mailid': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'materials': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

