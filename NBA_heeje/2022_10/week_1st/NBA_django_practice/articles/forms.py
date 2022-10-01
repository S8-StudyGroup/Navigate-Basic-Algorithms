from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력하세요',
                'maxlength': 10,
            }
        ),
        error_messages={
            'required': '제목은 필수',
        }
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용을 입력하세요',
                # 'rows': 5,
                # 'cols': 50,
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'