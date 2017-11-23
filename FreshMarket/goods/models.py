from django.db import models
from datetime import datetime
# from DjangoUeditor3.DjangoUeditor.models import UEditorField


# 开始写数据库
class GoodCategory(models.Model):
    """商品的类别"""
    Category_type = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名称", help_text="类别名称")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="分类描述", help_text="分类描述")
    category_type = models.IntegerField(choices=Category_type, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父类目", related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 品牌名称
class GoodsCategoryBrand(models.Model):
    category = models.ForeignKey(GoodCategory, related_name="brands", null=True, blank=True, verbose_name="商品类目")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名称", help_text="品牌名称")
    desc = models.CharField(default="品牌详情", max_length=256, verbose_name="品牌详情", help_text="品牌详情")
    image = models.ImageField(max_length=256, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand" # 这里就死给这张表自定义一个表明而不是默认的表名。

    def __str__(self):
        return self.name


# 商品详情的数据表
class Goods(models.Model):
    category = models.ForeignKey(GoodCategory, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=60, default="", verbose_name="商品的唯一的货号")
    name = models.CharField(max_length=100, verbose_name="商品名称")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存量")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店售价")
    good_brief = models.TextField(max_length=512, verbose_name="商品简述")
    # good_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300, filePath="goods/files/", default="")
    postage_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热卖")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 首页商品类别广告
class IndexAd(models.Model):
    category = models.ForeignKey(GoodCategory, related_name="category", verbose_name="商品类目")
    goods = models.ForeignKey(Goods, related_name="goods", verbose_name="商品名称")

    class Meta:
        verbose_name = "首页商品类别广告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


# 轮播的商品
class Banner(models.Model):
    goods = models.ForeignKey(Goods, verbose_name="商品名称")
    image = models.ImageField(upload_to="banner", verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


# 商品轮播图
class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, related_name="images", verbose_name="商品名称")
    image = models.ImageField(upload_to="", verbose_name="轮播图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


# 热搜词
class HotSearchWords(models.Model):
    keywords = models.CharField(max_length=20, default="", verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "热搜词"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords