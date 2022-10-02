from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용을 입력해주세요.',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용 입력은 필수입니다.'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'