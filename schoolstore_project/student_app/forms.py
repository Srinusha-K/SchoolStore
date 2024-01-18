from django import forms

from student_app.models import St_data, Courses

MATERIALS_CHOICES = [
    ('Calculator', 'Calculator'),
    ('Exam Paper', 'Exam Paper'),
    ('Pen', 'Pen'),
    ('Notes', 'Notes'),
    ('Folder','Folder'),
    ('Marker','Marker')
]

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))

class StudentCreationForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(label="Materials",choices=MATERIALS_CHOICES, widget=forms.CheckboxSelectMultiple)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)

    class Meta:
        model = St_data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].queryset = Courses.objects.none()


        self.fields['dob'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['courses'].queryset = Courses.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Courses queryset
        elif self.instance.pk:
            self.fields['courses'].queryset = self.instance.department.courses_set.order_by('name')