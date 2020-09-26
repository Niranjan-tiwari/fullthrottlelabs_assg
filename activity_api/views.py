# core imports
import traceback
from collections import OrderedDict

# django imports
from rest_framework.views import APIView

# project imports
from .helper.messages import Message
from .helper.util import JSONResponse
from .models import Member, MemberActivity


class UserActivityView(APIView):
    def get(self, request):
        try:
            members_quryset = Member.objects.all()
            if members_quryset.exists():
                members = []
                for member in members_quryset:
                    data_dict = OrderedDict()
                    activity_list = []
                    data_dict["id"] = member.id if (member and member.id) else None
                    data_dict["real_name"] = member.real_name if (member and member.real_name) else None
                    data_dict["tz"] = str(member.tz) if (member and member.tz) else None
                    activity_queryset = MemberActivity.objects.filter(member__id=member.id)
                    if activity_queryset.exists():
                        for activity in activity_queryset:
                            activity_list.append({
                                'start_time': activity.start_time if (activity and activity.start_time) else None,
                                'end_time': activity.end_time if (activity and activity.end_time) else None})

                        data_dict["activity_periods"] = activity_list
                        members.append(data_dict)
                    else:
                        return JSONResponse({
                            'code': 0,
                            'response': {},
                            'message': Message.code(4)
                        })
                return JSONResponse({
                    'code': 1,
                    'response': {"ok": True, "members": members},
                    'message': Message.code(1)
                })
            else:
                return JSONResponse({
                    'code': 0,
                    'response': {},
                    'message': Message.code(2)
                })
        except Exception as e:
            print(e, traceback.format_exc())
            return JSONResponse({
                'code': -1,
                'response': {},
                'message': Message.code(3)
            })
