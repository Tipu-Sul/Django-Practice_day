from django import forms
from django.core import validators
import datetime

class LoginForm(forms.Form):
    name= forms.CharField(max_length=30)
    email= forms.EmailField(required=False)
    comment= forms.CharField(widget=forms.Textarea)
    comments= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Agree= forms.BooleanField(required=True)
    date= forms.DateField()
    year=['1990', '2001', '2002', '2003', ]
    birthday= forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    birthYear= forms.DateField(widget=forms.SelectDateWidget(years=year))
    value=forms.DecimalField()
    details=forms.CharField(min_length=20)
    email_address=forms.EmailField(label='Please enter your email address')
    detels=forms.CharField(widget=forms.Textarea, initial='Enter deiails about your problem:')
    aggreement=forms.BooleanField(initial=True)
    day=forms.DateField(initial=datetime.datetime.today)
    color=[
        ('blue', 'blue'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('black','black')
    ]
    favoirite_color=forms.ChoiceField(choices=color)
    favoirite=forms.ChoiceField(widget=forms.RadioSelect, choices=color)
    favoirite_mlt=forms.MultipleChoiceField(choices=color)
    multi_choice=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=color)
    # model_choice=forms.ModelChoiceField(queryset=MyModel.objects.all(),initial=0)
    # model_choice=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=MyModel.objects.all(),initial=0)
    # field_name=forms.FieldType(**options)
    password=forms.CharField(widget=forms.PasswordInput)
    choice=forms.TypedChoiceField(choices=color)
    num=forms.DecimalField()
    timetable=forms.DurationField()
    file=forms.FileField()
    file2=forms.FilePathField(path='C:\MY PHONE\Facebook')
    num2=forms.FloatField()
    img=forms.ImageField()
    num3=forms.IntegerField()
    format=forms.GenericIPAddressField()
    agr=forms.NullBooleanField()
    n='my name is tipu sultan'
    # reg=forms.RegexField(max_length=20,min_length=10)
    abt=forms.SlugField()
    time=forms.TimeField()
    url=forms.URLField()
    uuid=forms.UUIDField()



# from django import forms
# from django.core import validators
    
# class contractForm(forms.Form):
#     name=forms.CharField(label='User Name',
#                           help_text='Name of the contract', 
#                           required=False, widget=forms.Textarea(attrs={'id':'textarea', 'class':'form-control', 'placeholder':'Name of the user'}))
#     # file=forms.FileField()
#     # img=forms.ImageField()
#     email=forms.EmailField(label='Email Address')
#     age=forms.CharField(label='Age', widget=forms.NumberInput())
#     weight=forms.FloatField(label='Weight')
#     balance=forms.DecimalField(label='Balance')
#     check=forms.BooleanField(label='Check')
#     bitrhday=forms.DateField(label='Bitrh Day', widget=forms.DateInput(attrs={'type':'date'}))
#     appointment=forms.DateTimeField(label='Appointment', widget=forms.DateInput(attrs={'type':'datetime-local'}) )
#     Choices=[('s','Small'), ('m','Medium'), ('l','Long')]
#     size=forms.ChoiceField(choices=Choices, label='Size', widget=forms.RadioSelect)
#     box=[('P','Peparoni'), ('M','Masrum'), ('B','Beef')]
#     piza=forms.MultipleChoiceField(choices=box, label='Piza',widget=forms.CheckboxSelectMultiple)

