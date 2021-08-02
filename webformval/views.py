from django.db.models import Q, Count
from .models import Template
from django.http import JsonResponse
from django.views import View
from .utils import form_type


class Templates_views (View):

    def get(self, request):
        form_fields_types = form_type(request.GET)
        form_search_cond = Q()                                  # django.db.models.Q

        for k, v in form_fields_types.items():                  # Собираем запрос
            form_search_cond.add(Q(sample__name_field=k, sample__type_field=v), Q.OR)
        template = Template.objects.filter(form_search_cond).annotate(count_fields=Count('id')).order_by('-count_fields')

        for i in template.values():                             # Проверяем
            count_fields = int(i['count_fields'])
            if count_fields == len(form_fields_types):
                if count_fields == len(Template.objects.filter(id=i['id']).values('sample__id')):
                    return JsonResponse({"name": i['name']})

        return JsonResponse(form_fields_types)
