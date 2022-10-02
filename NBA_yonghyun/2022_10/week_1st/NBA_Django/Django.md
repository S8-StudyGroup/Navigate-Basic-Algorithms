## 목차
[사전 작업](#사전-작업)  
[게시물 CRUD](#게시물-crud)  
[유저 CRUD](#유저-crud)

<br><br>

# 사전 작업

## 1️⃣ 가상환경
◽ 설치  
``` 
$ python -m venv venv
```

◽ 활성화
```
$ source venv/Scripts/activate
```

<br>

## 2️⃣ 장고 및 패키지 설치
```
$ pip install django==3.2.13
```
❌ 띄어쓰기 또는 = 하나만 사용 시 에러

<br>

## 3️⃣ requirements.txt
◽ 생성
```
$ pip freeze > requirements.txt
```

◽ 목록 설치
```
$ pip install -r reqirements.txt
```

<br>

## 4️⃣ 프로젝트 생성
```
$ django-admin startproject crud .
```
여기서 crud는 프로젝트명  
. 은 현재 폴더를 의미 (없으면 에러)

<br>

## 5️⃣ 애플리케이션 생성
```
$ python manage.py startapp articles
$ python manage.py startapp accounts
```
article과 accounts는 앱 이름  

이후 settings.py의 **INSTALLED_APPS**에 앱 등록 (꼭 생성 후 등록)

<br>

## 6️⃣ base.html 
◽ 바깥에 templates 폴더 생성 후 작성  
◽ settings.py에 템플릿 경로 추가 ➡ **'DIRS' : [BASE_DIR / 'templates', ]**

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>
<body>
  <div class='container'>
    {% block content %}

    {% endblock content %}
  <div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</body>
</html>
```

<br>

## 7️⃣ Namespace
### 🔹 crud/urls.py
``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
```
◽ 각각 앱폴더에 urls.py 만들어줌  
◽ html 작성할 폴더 만들어줌 ➡ **templates/앱 이름**

<br>

### **⭐코드 작성 순서⭐ URL ➡ VIEW ➡ TEMPLATES ⭐**
<br>

<br><br>

# 게시물 CRUD

## 1️⃣ Model 작성 & 마이그레이션
### ⭐ articles/models.py
``` python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
```

<br>

### ⭐ accounts/models.py
``` python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
```
◽ 커스텀 유저 모델의 경우 첫 번째 마이그레이션 이전 등록이 필요함 ➡ 미리 만들어놓자!!  
◽ settinds.py에 등록 ➡ **AUTH_USER_MODEL = 'accounts.User'**  
◽ admin.py에 등록 ➡ **from . models import User**

<br>

### 마이그레이션
◽ 생성
```
$ python manage.py makemigrations
```

◽ 반영
``` 
$ python manage.py migrates
```

<br><br>

## 2️⃣ URL
◽ 하나의 view함수를 만들 때마다 url을 먼저 작성함  
◽ 아래는 최종
``` python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), 
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

<br><br>

## 3️⃣ 메인화면 (index)

### 🔹 index 함수
``` python
from django.shortcuts import render


def index(request):
    return render(request, 'articles/index.html', context)
```

<br>

### 🔸 index.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="#">CREATE</a>
{% endblock content %}
```

<br><br>

## 4️⃣ Form 작성
### ⭐ articles/forms.py  
◽ 파일 직접 생성

``` python
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
```
◽ 라벨, 위젯, 에러 메시지 등은 선택사항


<br><br>

## 5️⃣ 게시물 생성 (create)
### 🔹 create 함수 (GET 요청만 처리)
``` python
from django.shortcuts import render
from .forms import ArticleForm


def create(request):
    if request.method == 'POST':
				pass
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

<br>

### 🔸 create.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="CREATE">
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```
◽ POST 요청을 처리할 때는 csrf 토큰 필수!!

<br>

### 🔹 수정된 index 함수 & create 함수 (GET + POST)
``` python
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def index(request):
    article = Article.objects.all()
    context = {
        'articles': article, 
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```
◽ 인덱스 함수도 게시물을 조회할 수 있도록 수정해줌

<br>

🔸 index.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  <a href="{% url 'articles:create' %}">CREATE</a>
  <hr>
  {% for article in articles %}
  <h2>Title : {{ article.title }}</h2>
  <a href="#">DETALE</a>
  {% endfor %}
{% endblock content %}
```

<br><br>

## 6️⃣ 상세정보 (detail)
### 🔹 detail 함수
``` python
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)
```
◽ 하나의 게시물의 상세정보를 열람해야 하므로 **pk**값이 필요함

<br>

### 🔸 detail.html
``` html
{% extends 'base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<h2>글 번호 : {{ article.pk }}</h2>
<h2>글 제목 : {{ article.title }}</h2>
<p>글 내용 : {{ article.content }}</p>
<p>생성시각 : {{ article.created_at }}</p>
<p>수정시각 : {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

<br>

### 🔹 수정된 create 함수
``` python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```
◽ pk값을 보내주기 위해 폼을 article로 저장

<br><br>

## 7️⃣ 게시물 수정 (update)
### 🔹 update 함수 (GET 요청만)
``` python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        pass
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)
```
◽ 수정과 관련한 폼은 instance 필요  
◽ **instance** : 기존 인자를 받아오는 역할  
◽ context에 form 뿐만 아니라 article에 들어있는 값도 보내줘야 함

<br>

### 🔸 update.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE">
  </form>
  <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endblock content %}
```
◽ create.html과 다른 점 : 수정할 내용을 가지고 있어야 하기 때문에 **article.pk** 붙여줌  

<br>

### 🔹 create 함수 (GET + POST)
``` python
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)
```
◽ create에서 저장한 데이러를 article로 받아서 redirect 시 article.pk로 보냄  

<br><br>

## 8️⃣ 게시물 삭제 (delete)
### 🔹 delete 함수
``` python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

<br>

### 🔸 detail.html
``` html
{% extends 'base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<h2>글 번호 : {{ article.pk }}</h2>
<h2>글 제목 : {{ article.title }}</h2>
<p>글 내용 : {{ article.content }}</p>
<p>생성시각 : {{ article.created_at }}</p>
<p>수정시각 : {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:update' article.pk %}">UPDATE</a>
<br>
<a href="{% url 'articles:index' %}">BACK</a>
<form action="{% url 'articles:delete' article.pk %}">
  {% csrf_token %}
  <input type="submit" value="DELETE">
</form>
{% endblock content %}
```
◽ 상세 페이지에 수정(페이지 이동), 삭제 명령어 추가

<br><br>

# 유저 CRUD
## 1️⃣ URL
``` python
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
    
]
```
<br><br>

## 2️⃣ 메인 화면 (index)
### 🔹 index 함수
``` python
from django.shortcuts import render


def index(request):
    return render(request, 'accounts/index.html')
```

<br>

### 🔸 index.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Accounts</h1>
{% endblock content %}
```


<br><br>

## 3️⃣ Admin

```
python manage.py createsuperuser
```

<br>

### ⭐ accounts/admin.py
``` python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)
```

<br>

### ⭐ articles/admin.py
``` python
from django.contrib import admin
from .models import Article


admin.site.register(Article)
```

<br><br>

## 4️⃣ 회원가입 (signup)
### ⭐ forms.py
``` python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```
◽ 내장되어있는 UserCreationForm을 상속받아 커스텀 폼 생성  
◽ model = User 대신 **model = get_user_model()**으로 작성

<br>

### 🔹 수정된 index 함수 & signup 함수 (GET 요청만)
``` python
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import User


def index(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.method == "POST":
				pass
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```

<br>

### 🔸 수정된 index.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Accounts</h1>
  <br>
  {% for user in users %}
    <h2>번호 : {{ user.pk }}</h2>
    <p>아이디 : {{ user.username }}</p>
  
  {% endfor %}
{% endblock content %}
```

<br>

### 🔹 signup 함수 (GET + POST)
``` python
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from .models import User


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
```
◽ 회원가입 시 자동 로그인이 되도록 폼의 정보를 user에 저장하고, **auth_login(request, user)**로 로그인을 시켜줌

<br>

### 🔸 signup.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Signup</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="SIGNUP">
  </form>
  <a href="{% url 'accounts:index' %}">BACK</a>
{% endblock content %}
```

<br><br>

## 3️⃣ 로그인 (login) & 로그아웃 (logout)
### 🔹 login 함수 (GET 요청만)
``` python
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User


def login(request):
    if request.method == "POST":
        pass
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
```

<br>

### 🔸 login.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="LOGIN">
  </form>
  <a href="{% url 'accounts:index' %}">BACK</a>
{% endblock content %}
```

<br>

### 🔹 logout 함수
``` python
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
```

<br>

### 🔹 login 함수 (GET + POST)
``` python
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
```

<br><br>

## 4️⃣ 회원 정보 변경 (update)
### ⭐ forms.py
``` python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', )
```
◽ 불필요한 정보 노출을 막기 위해 보일 필드를 지정해줌

<br>

### 🔹 update 함수
``` python
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
```
◽ request.POST를 instance에 넣어준다는 뜻  
◽ instance = request.user : 요청한 곳에서 받아옴  
◽ 하나의 정보만 보는데도 pk 안 넣어줌 ➡ 현재 로그인 정보를 request에서 받고있기 때문  
<br><br>

## 5️⃣ 회원 정보 삭제 (delete)
### 🔹 delete 함수
``` python
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')
```
◽ 회원 정보 삭제와 후 로그아웃도 해줌 (순서가 바뀌면 안됨!!)


<br><br>

## 6️⃣ 비밀번호 변경 
### 🔹 change_password 함수
``` python
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
```
◽ request.user를 받을 때 instance를 쓰지 않음  
> 정보 수정 시,  
> 
> 커스텀 폼 : instance = request.user  
> 내장 폼 : request.user

◽ 변경 후 로그인 정보가 풀리는 이유? ➡ 요청-응답마다 인증여부를 계속 보내줌. 비밀번호 변경 시 현재 session 값과 DB에 저장되어 있는 값이 달라짐 (즉, 인증이 풀림)  
◽ 비밀번호 변경 + session 값 변경 ➡ **update_session_auth_hash**

<br>

### 🔸 change_password.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Change Password</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="CHANGE">
  </form>
  <a href="{% url 'accounts:update' %}">BACK</a>
{% endblock content %}
```


<br><br>

## 7️⃣ base.html 설정
◽ 기본적으로 hello, 유저이름과 사용가능한 기능들이 표시되도록 함

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>
<body>
  <div class='container'>
    <h1>Hello, {{ user }}</h1>
    {% if request.user.is_authenticated %}
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="LOGOUT">
      </form>
      <a href="{% url 'accounts:update' %}">UPDATE</a>
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      {% else %}
        <a href="{% url 'accounts:login' %}">LOGIN</a>
        <a href="{% url 'accounts:signup' %}">SIGNUP</a>
      {% endif %}
    <hr>
    {% block content %}

    {% endblock content %}
  <div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</body>
</html>
```
◽ {{ user }} : settings.py에 내장되어 있음  
◽ 로그인 이전과 이후 필요한 기능이 다름 ➡ **is_authenticated**  
◽ 로그인 이전 (else문) : LOGIN, SIGNUP  
◽ 로그인 이후 (if문) : LOGOUT, UPDATE, DELETE  

<br><br>

## 8️⃣ 데코레이터
악성사용자 멈춰✋  

◽ 데코레이터 : 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수

<br>

◽ require_safe : GET 요청에만 코드 실행  
◽ require_POST : POST 요청에만 코드 실행  
◽ require_http_methods() : 특정 요청에만 코드 실행  

<br>

◽ login_required : 로그인 상태에만 코드 실행
> 로그인 상태가 아닐 시 로그인 페이지로 넘어감  
> 로그인 후 원하는 페이지로 가고싶으면 **next** 파라미터 안에 가야할 경로 지정  
> login.html에서 액션을 지워줘야 함 (그래야 자기자신으로 들어감)

<br>

### 🔸 수정된 login.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="LOGIN">
  </form>
  <a href="{% url 'accounts:index' %}">BACK</a>
{% endblock content %}
```

<br>

### 🔹 accounts/views.py (데코레이터 사용)
``` python
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


@require_safe
def index(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)



@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)



@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:index')


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
```
◽ **return redirect(request.GET.get('next') or 'accounts:index')** : 로그인의 next 파라미터 사용  
◽ logout, delete는 로그인 후에만 사용할 수 있는 기능이지만, POST 요청을 받음 ➡ next로 들어가게되면 POST 요청이 GET 요청이 됨  
◽ @login_required 를 없애주고 **is_authenticated**로 조건 설정해줌

> POST, GET 요청을 같이 받는 경우(update, change_password),  
> 유효성 검사가 있기 때문에 @login_required 사용 O

<br>

### 🔹 articles/views.py
``` python
from django.shortcuts import redirect, render
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


@require_safe
def index(request):
    article = Article.objects.all()
    context = {
        'articles': article, 
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
```


