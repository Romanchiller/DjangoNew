from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope
from pprint import pprint

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        total = 0
        for form in self.forms:
            try:
                if form.cleaned_data['is_main'] is True:
                    total += 1
            except KeyError:
                pass

        if total > 1:
            raise ValidationError('Выбрано больше одного основного тега')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 2
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']


