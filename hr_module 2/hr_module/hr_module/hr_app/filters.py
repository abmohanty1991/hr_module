import django_filters
from .models import *

class MasterOfficersFilter(django_filters.FilterSet):
    class Meta:
        model = PersonnelMasters
        fields = '__all__'
        exclude = ['qualification',
                    'pno',
                    'name',
                    'course_1',
                    'course_1_status',
                    'course_2',
                    'course_2_status',
                    'course_3',
                    'course_3_status',
                    'course_4',
                    'course_4_status',
                    'course_5',
                    'course_5_status',
                    'doj',
                    'doj_station',
                    'seniority_in_rank',
                    'dob',
                    'date_of_commission',
                    'date_of_retirement',
                    'date_ of_ leaving_service',
                    'date_of_supperannuation',
                    'marital_status',
                    'spouse_name',
                    'ex_units',
                    'ex_unit_grp',
                    'future_unit',
                    'future_appt',
                    'dtbr',
                    'duration_in_present_unit',
                    'select_list_year',
                    'chance_selection',
                    'command_sceS_result',
                    'sea_command_yn',
                    'sublt_seniority',
                    'special_skills',
                    'spouse_nationality',
                    'state',
                    'station_seniority',
                    'remarks'
                    ]