from django import forms

from .models import Article, Comment


class CommentCreateForm(forms.ModelForm):
    # Форма добавления комментария под статьей
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': 30, 'row': 5, 'placeholder': 'Комментарии',
                                                                     'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('content',)


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'category', 'short_description', 'full_description', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class ArticleUpdateForm(ArticleCreateForm):
    class Meta:
        model = Article
        fields = ArticleCreateForm.Meta.fields + ('updater', 'fixed')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fixed'].widget.attrs.update({
            'class' : 'form-check-input'
        })

