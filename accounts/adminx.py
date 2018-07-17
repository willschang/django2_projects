import xadmin
# 和X admin的view绑定
from xadmin import views
from .models import Banner
from django.utils.safestring import mark_safe

# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True

# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "深思海数: 智能教育后台管理"
    site_footer = "sensehiso tech"
    # 收起菜单
    menu_style = "accordion"

# 创建banner的管理类
class BannerAdmin():
    list_display = ['title', 'image_img', 'image_data', 'desc', 'index', 'created_at']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'created_at']
    # 富文本
    style_fields = {"desc": "ueditor"}
    readonly_fields = ('image_data',)  # 必须加这行 否则访问编辑页面会报错 ????
    # 设置显示图标
    model_icon = 'fa fa-camera-retro'
    #自动刷新列表页面（秒数）
    # refresh_times = [3,5]
    # 每页显示
    # list_per_page = 50
    # import_excel = True


# 将model与admin管理器进行关联注册
xadmin.site.register(Banner, BannerAdmin)
# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)