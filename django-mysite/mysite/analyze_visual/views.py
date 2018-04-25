from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from data_scraping.models import State, County, StatePop, CountyPop, Indicator
import json
# Create your views here.

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('analyze_visual/home.html')
    indicator = Indicator.objects.get(indicator_name='TotalPop')
    context = {
        'states': StatePop.objects.filter(indicator=indicator)
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
def jing(request):
    return HttpResponse("<h2>I'm Jing</h2>")
    
def geo_api(request):
    if request.method == 'GET':
        geo_type = request.GET.get("geo_type", None) # all_state, all_county, state, county
        geo_state_id = request.GET.get("geo_state_id", None)
        geo_county_id = request.GET.get("geo_county_id", None)
        if geo_type == "all_state":
            result = {"type":"FeatureCollection", "features":[]}
            for state in State.objects.all():
                i = {"type":"Feature", "id":"USA-%s"%state.state_short_name,
                     "properties":{"state_id":state.state_id,"name":state.state_name},
                     "geometry": json.loads(state.geometry.replace("'",'"'))}
                result["features"].append(i)
            return JsonResponse(result)
        if geo_type == "all_county" and geo_state_id != None:
            state = State.objects.first(state_id=geo_state_id)
            result = {"type":"FeatureCollection", 
                      "properties":{"kind":"state", "state":state.state_short_name},
                      "features":[]}
            for county in County.objects.filter(state = state):
                i = {"type":"Feature",
                    "properties":{"kind":"county","county_id":county.county_id, "name":county.county_name, "state":state.state_short_name},
                    "geometry": json.loads(county.geometry.replace("'",'"'))
                    }
                result["features"].append(i)
            return JsonResponse(result)
        if geo_type == "state" and geo_state_id != None:
            state = State.objects.first(state_id=geo_state_id)
            result = {"type":"FeatureCollection", 
                      "properties":{"kind":"state", "state":state.state_short_name},
                      "features":[{"type":"Feature", "id":"USA-%s"%state.state_short_name,
                     "properties":{"state_id":state.state_id,"name":state.state_name},
                     "geometry": json.loads(state.geometry.replace("'",'"'))}]}
            return JsonResponse(result)
        if geo_type == "county" and geo_state_id != None and geo_county_id != None:
            state = State.objects.first(state_id=geo_state_id)
            county = County.objects.first(state=state, county_id=geo_county_id)
            result = {"type":"FeatureCollection", 
                      "properties":{"kind":"state", "state":state.state_short_name},
                      "features":[{"type":"Feature",
                      "properties":{"kind":"county","county_id":county.county_id, "name":county.county_name, "state":state.state_short_name},
                      "geometry": json.loads(county.geometry.replace("'",'"'))
                      }]}
            return JsonResponse(result)
        if geo_type == "all_county":
            result = {"type":"FeatureCollection", 
                      "properties":{"kind":"state"},
                      "features":[]}
            for county in County.objects.all():
                i = {"type":"Feature",
                    "properties":{"kind":"county","county_id":county.county_id, "name":county.county_name, "state":county.state.state_short_name},
                    "geometry": json.loads(county.geometry.replace("'",'"'))
                    }
                result["features"].append(i)
            return JsonResponse(result)
        
    return JsonResponse({'message':'error'})
    