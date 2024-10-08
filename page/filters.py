import django_filters
from page.models import *


class MessageFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'user__username', 'status', 'status2']


class MessageFilter1(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id']


class MalumotUchunFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = MalumotUchun
        fields = ['id', 'status']


class UserFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    id = django_filters.AllValuesMultipleFilter(label='id')

    class Meta:
        model = User
        fields = ['username', 'id']
