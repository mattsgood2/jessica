from django import forms
from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#added this to show up in admin for better view
#the class must go above the admin.site.reg to work

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',)
    #fields = ('question_text', 'pub_date',)

#class QuestionForm(forms.ModelForm):

    #class Meta:
        #model = Question, Choice
        #fields = ['question_text', 'pub_date', 'choice_text', ]

admin.site.register(Question, QuestionAdmin)
# added Choice so you can see whats there

#added this to show up in admin for better view
#the class must go above the admin.site.reg to work
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

admin.site.register(Choice, ChoiceAdmin)
