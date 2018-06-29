from django.contrib import admin
from airlines.models import Airliner, Airport, Route, Flight, DayOfWeek, ScheduleRecord


admin.site.register(Airport)
admin.site.register(Route)
admin.site.register(Flight)
admin.site.register(DayOfWeek)
admin.site.register(ScheduleRecord)


class AirlinerAdmin(admin.ModelAdmin):
    filter_horizontal = ('routes',)


admin.site.register(Airliner, AirlinerAdmin)
