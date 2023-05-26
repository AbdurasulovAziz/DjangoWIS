from django.contrib.admin import action


@action(description="Put on stop list")
def put_on_stop_list(modeladmin, request, queryset):
    queryset.update(on_stop=True)


@action(description="Remove from stop list")
def remove_from_stop_list(modeladmin, request, queryset):
    queryset.update(on_stop=False)
