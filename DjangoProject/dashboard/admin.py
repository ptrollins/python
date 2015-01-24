#from TestApp.models import Exercise, Student, Score
from django.contrib import admin

#admin.site.register(Exercise, Student, Score)


'''class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)'''