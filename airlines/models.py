from django.db import models


class Airport(models.Model):

    class Meta:
        verbose_name = "Аэропорт"
        verbose_name_plural = "Аэропорты"

    def __str__(self):
        return '{}:{}  {}' .format(self.name, self.title, self.id)

    name = models.CharField(max_length=8)
    title = models.CharField(max_length=64)


class Route(models.Model):

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"

    def __str__(self):
        return '{}  ({})'.format(self.name, self.id)

    name = models.CharField(max_length=8)
    schedule = models.ManyToManyField('DayOfWeek', through='ScheduleRecord')


class Flight(models.Model):

    class Meta:
        verbose_name = "Перелет"
        verbose_name_plural = "Перелеты"

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    order = models.IntegerField()


class DayOfWeek(models.Model):

    class Meta:
        verbose_name = "День недели"
        verbose_name_plural = "Дни недели"

    def __str__(self):
        return '{}  {}' .format(self.title, self.id)

    title = models.CharField(max_length=16)


class ScheduleRecord(models.Model):

    class Meta:
        verbose_name = "Записи расписания"
        verbose_name_plural = "Записи расписания"

    day = models.ForeignKey('DayOfWeek', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    per_day = models.IntegerField()


class Airliner(models.Model):

    class Meta:
        verbose_name = "Авиалайнер"
        verbose_name_plural = "Авиалайнеры"

    def __str__(self):
        return '{}: {}  ()' .format(self.name, self.title, self.id)

    routes = models.ManyToManyField(Route)
    name = models.CharField(max_length=8)
    title = models.CharField(max_length=32)


