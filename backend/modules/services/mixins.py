from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


class UserIsNotAuthenticated(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_authenticated:
            messages.info(self.request, 'Вы уже авторизованы')
            raise PermissionDenied
        return True

    def handle_no_permission(self):
        return redirect('home')


class AuthorRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().author or request.user.is_staff:
                messages.info(request, 'Изменение и удаление статьи доступно только автору')
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)