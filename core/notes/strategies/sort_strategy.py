class BaseSortStrategy:
    def sort(self, queryset):
        return queryset


class SortByTitleStrategy(BaseSortStrategy):
    def sort(self, queryset):
        return queryset.order_by("title")


class SortByTitleDescStrategy(BaseSortStrategy):
    def sort(self, queryset):
        return queryset.order_by("-title")


class SortByCreatedAtStrategy(BaseSortStrategy):
    def sort(self, queryset):
        return queryset.order_by("-created_at")


class SortByCreatedAtAscStrategy(BaseSortStrategy):
    def sort(self, queryset):
        return queryset.order_by("created_at")


STRATEGY_MAP = {
    "title": SortByTitleStrategy,
    "title_desc": SortByTitleDescStrategy,
    "created_at": SortByCreatedAtStrategy,
    "created_at_asc": SortByCreatedAtAscStrategy,
}


def get_sort_strategy(sort_by):
    strategy_class = STRATEGY_MAP.get(sort_by, BaseSortStrategy)
    return strategy_class()