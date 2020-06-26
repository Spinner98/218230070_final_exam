from django.shortcuts import render
from .models import Passenger, Covid
from django.db.models import Count, Q
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def world_population(request):
    return render(request, 'world_population.html')
import json  # ***json 임포트 추가***
# ...

def ticket_class_view_2(request):  # 방법 2
    dataset = Passenger.objects\
        .values('ticket_class',) \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False)),
                  people = Count('ticket_class'),
                  ) \
        .order_by('ticket_class')

    # 빈 리스트 3종 준비
    categories = list()             # for xAxis
    survived_series = list()        # for series named 'Survived'
    not_survived_series = list()
    people=list()
    # 리스트 3종에 형식화된 값을 등록
    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])    # for xAxis
        survived_series.append(entry['survived_count'])          # for series named 'Survived'
        not_survived_series.append(entry['not_survived_count'])
        people.append(entry['survived_count'] /entry['people'] *100 )
        # for series named 'Not survived'


    # json.dumps() 함수로 리스트 3종을 JSON 데이터 형식으로 반환
    return render(request, 'ticket_class_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series),
        'people' : json.dumps(people)
    })
# ...

def covid_class_view(request):

    covid_data = Covid.objects\
        .values('date','France','SouthKorea','Germany','UnitedKingdom','US') \
        .order_by('date')

    date = list()             # for xAxis
    SouthKorea = list()
    US = list()
    UnitedKingdom = list()
    Germany = list()
    France = list()


    for entry in covid_data:
        date.append(entry['date'])    # for xAxis
        France.append(entry['France'])
        SouthKorea.append(entry['SouthKorea'])
        Germany.append(entry['Germany'])
        UnitedKingdom.append(entry['UnitedKingdom'])
        US.append(entry['US'])

    # json.dumps() 함수로 리스트 3종을 JSON 데이터 형식으로 반환
    return render(request, 'covid_class.html', {
        'date' : json.dumps(date,cls=DjangoJSONEncoder),
        'France': json.dumps(France),
        'SouthKorea' : json.dumps(SouthKorea),
        'Germany' : json.dumps(Germany),
        'UnitedKingdom' : json.dumps(UnitedKingdom),
        'US' : json.dumps(US)
    })
def covid_population(request):

    covid_data = Covid.objects\
        .values('date','France','SouthKorea','Germany','UnitedKingdom','US') \
        .order_by('date')

    date = list()             # for xAxis
    SouthKorea = list()
    US = list()
    UnitedKingdom = list()
    Germany = list()
    France = list()


    for entry in covid_data:
        date.append(entry['date'])    # for xAxis
        France.append(entry['France'] / 65273511 * 1000000)
        SouthKorea.append(entry['SouthKorea'] / 51269185*1000000)
        Germany.append(entry['Germany'] / 83783942*1000000)
        UnitedKingdom.append(entry['UnitedKingdom'] / 67886011*1000000)
        US.append(entry['US'] / 331002651*1000000)

    # json.dumps() 함수로 리스트 3종을 JSON 데이터 형식으로 반환
    return render(request, 'covid_populaiton.html', {
        'date' : json.dumps(date,cls=DjangoJSONEncoder),
        'France': json.dumps(France),
        'SouthKorea' : json.dumps(SouthKorea),
        'Germany' : json.dumps(Germany),
        'UnitedKingdom' : json.dumps(UnitedKingdom),
        'US' : json.dumps(US)
    })