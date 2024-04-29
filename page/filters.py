import django_filters
from page.models import Message, User


class MessageFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'user__username', 'status']


class MessageFilter1(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['id']


class UserFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    id = django_filters.AllValuesMultipleFilter(label='id')

    class Meta:
        model = User
        fields = ['username', 'id']
