from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력',
            }
        )
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'rows': 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required': '내용은 필수'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'