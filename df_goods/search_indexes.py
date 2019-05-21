from .models import GoodsInfo
from haystack import indexes


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return GoodsInfo

    def index_queryset(self, using=None):  # 重载index_..函数
        return self.get_model().objects.all()
