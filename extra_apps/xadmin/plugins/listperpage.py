from django.utils.safestring import mark_safe

import xadmin
from xadmin.views import BaseAdminPlugin
from django.template import loader
from django.utils.html import escape

class ListPerPagePlugin(BaseAdminPlugin):
    show_list_per_page = True
    list_per_page_choices = [10, 20, 50, 100, 500]

    def init_request(self, *args, **kwargs):
        try:
            self.admin_view.list_per_page = int(self.request.GET.get('list_per_page', self.admin_view.list_per_page))
        except ValueError as e:
            print(repr(e))

        if self.admin_view.list_per_page>10000:
            self.admin_view.list_per_page = 10000 # 最大10000

        return bool(self.show_list_per_page)

    def get_context(self, context):
        list_per_page_range = []
        for per_page in self.list_per_page_choices:
            list_per_page_range.append(mark_safe('<a href="%s"%s><p class="text-left">%d</p></a> ' % (escape(self.get_query_string({'list_per_page': per_page})),
                                                    (per_page == self.admin_view.list_per_page and ' class="btn btn-sm disabled"' or ' class="btn btn-sm"'), per_page)))

        context.update({'list_per_page_range': list_per_page_range, 'list_per_page_required': (not self.admin_view.show_all or not self.admin_view.can_show_all) and self.admin_view.multi_page})
        return context

    # 对应model_list.html中的view_block 'bx_list_per_page'
    def block_bx_list_per_page(self, context, nodes):
       nodes.append(loader.render_to_string('xadmin/views/bx_list_per_page.html', context=context))