from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister

users = ["user1", "user2", "user3"]         # список текущих пользователей


def check_form(info, username, password, repeat_password, age):
    info["users"] = users
    if password != repeat_password:
        info["error"] = "Пароли не совпадают"
    elif int(age) < 18:
        info["error"] = "Вы должны быть старше 18"
    elif username in info["users"]:
        info["error"] = "Пользователь уже существует"


def sign_up_by_html(request):
    info = dict()
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        # Проверяем данные формы
        check_form(info, username, password, repeat_password, age)
        if "error" not in info:
            return HttpResponse(f"<p align=center>Приветствуем, {username}!</p>")

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    info = dict()
    if request.method == 'POST':
        # Получаем данные из формы
        form = UserRegister(request.POST)  # Создание объекта формы
        if form.is_valid():  # Проверка формы на корректность
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            # Проверяем данные формы
            check_form(info, username, password, repeat_password, age)
            if "error" not in info:
                return HttpResponse(f"<p align=center>Приветствуем, {username}!</p>")

    # Если это GET запрос
    else:
        form = UserRegister()

    info["form"] = form
    return render(request, 'fifth_task/registration_page.html', context=info)
