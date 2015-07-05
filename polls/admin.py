from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Question Information',{'fields':['ques_text']}),
        ('Date Informatiion',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceInline]
admin.site.register(Question,QuestionAdmin)

