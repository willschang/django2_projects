from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Banner
from django.utils.translation import ugettext_lazy as _


class BannerFilter(filters.FilterSet):
    """
    过滤 设置
    """
    min_index = filters.NumberFilter(field_name='index', lookup_expr='gte', help_text=_('大于等于'))
    max_index = filters.NumberFilter(field_name='index', lookup_expr='lte', help_text=_('小于等于'))

    # method
    # top_index_n = filters.NumberFilter(field_name='index', method='top_index_n_fiter')
    #
    # def top_index_n_filter(self, queryset, name, value):
    #     return queryset.filter(...)

    class Meta:
        model = Banner
        fields = ['min_index', 'max_index', 'title']