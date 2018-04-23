from django.contrib import admin
from data_scraping.models import State,County,Indicator,Year,StatePop,CountyPop
import requests

def run_state_indicator(modeladmin, request, queryset):
    for state in queryset:
        for i in Indicator.objects.all():
            for y in Year.objects.all():
                print (y.year, i.indicator_id, state.state_id)
                statepop, created = StatePop.objects.get_or_create(state=state, indicator=i, year=y)
                data = requests.get('https://api.census.gov/data/'+ y.year +'/acs/acs5?get=NAME,'+ i.indicator_id + '&for=state:'+ state.state_id)
                statepop.population = data.json()[1][1]
                statepop.save()

run_state_indicator.short_description = "Run selected state indicator"

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_name', 'state_id']
    ordering = ['state_id']
    actions = [run_state_indicator]
admin.site.register(State, StateAdmin)


admin.site.register(County)
admin.site.register(Indicator)
admin.site.register(Year)

class StatePopAdmin(admin.ModelAdmin):
    list_display = ['state', 'indicator', 'year', 'population']
    ordering = ['id']


admin.site.register(StatePop,StatePopAdmin)
admin.site.register(CountyPop)

