import csv
import os
from django.db import migrations
from django.conf import settings

# csv 파일의 해당 열 번호를 상수로 정의
date = 0
SouthKorea = 1
US = 2
UnitedKingdom= 3
Germany = 4
France =5

def add_covid(apps, schema_editor):
    Covid = apps.get_model('chart', 'Covid')  # (app_label, model_name)
    csv_file = os.path.join(settings.BASE_DIR, 'covid.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        for entry in reader:                            # 판독기에 대하여 반복 처리
            Covid.objects.create(                       # DB 행 생성
                date = entry[date],
                SouthKorea =float(entry[SouthKorea]),
                US = float(entry[US]),
                UnitedKingdom = float(entry[UnitedKingdom]),
                Germany = float(entry[Germany]),
                France = float(entry[France])
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('chart', '0001_initial'),         # app_label, preceding migration file
    ]
    operations = [                              # 작업
        migrations.RunPython(add_covid),   # add_passengers 함수를 호출
    ]