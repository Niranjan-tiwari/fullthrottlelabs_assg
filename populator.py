import json
import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullthrottle_backend.settings')
django.setup()

from activity_api.models import Member, MemberActivity
json_path = "path to sample.json file"
file = open(json_path)

data = json.load(file)
for i in data['members']:
    id = i['id']
    real_name = i['real_name']
    tz = i['tz']
    data_fill = Member.objects.get_or_create(id=id, real_name=real_name, tz=tz)
    print('MemberTable filled')
    for j in i['activity_periods']:
        start_time = j['start_time']
        end_time = j['end_time']
        member = Member.objects.get(id=id)
        data_fill1 = MemberActivity.objects.get_or_create(start_time=start_time, end_time=end_time,member=member)
        print('ActivityTable filled')
