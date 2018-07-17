import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from DjangoUeditor.models import UEditorField
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=6,
        verbose_name="性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100,
        verbose_name="头像",
        blank=True, null=True
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载__str__方法，打印实例会打印username，username为继承自AbstractUser
    def __str__(self):
        return self.username


# 轮播图model
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name="轮播图",
        max_length=100,
        # default= '',
        # blank=True,
        # null=True
    )
    # https://pypi.org/project/django-stdimage/
    image1 = StdImageField(max_length=100, default= '',
        upload_to=UploadToUUID(path=datetime.datetime.now().strftime('banner/%Y/%m')),
        verbose_name="轮播图11",
        variations={'thumbnail': {'width': 100, 'height': 75}})
    url = models.URLField(max_length=200, verbose_name="访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name="顺序")
    # desc = models.TextField(verbose_name='内容描述')
    # 修改imagepath,不能传y m 进来，不能加斜杠是一个相对路径，相对于setting中配置的mediaroot
    desc = UEditorField(verbose_name="内容描述", width=800, height=300, imagePath="banner/ueditor/",
                          filePath="banner/ueditor/", default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    # 在后台管理页面 列表里 显示图片缩略图
    # https://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
    def image_data(self):
        if self.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
        else:
            return '图片未上传'

    # 页面显示的字段名称
    image_data.short_description = '图片缩略图'
    # image_data.sallow_tag = True

    def image_img(self):
        if self.image1:
            return mark_safe('<img src="%s" />' % self.image1.thumbnail.url)
        else:
            return '上传图片'

    image_img.short_description = '轮播图'
    image_img.allow_tags = True


    # def desc_html(self):
    #     return format_html(self.desc)
    #
    # desc_html.short_description = '描述内容'

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name


    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}(位于第{1}位)'.format(self.title, self.index)
