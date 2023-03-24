from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.

from .models import Entry

"""
Как и было обещано, в настоящее время вам не придется писать много кода.
Запрос Entry.objects.all() в строке 32 вернет все записи, упорядоченные по их первичному ключу.
При добавлении к нему .order_by("-date_created")ваши записи будут возвращаться в порядке возрастания,
причем самая новая запись будет вверху списка.

EntryListView и EntryDetailView являются просмотрами для чтения и не обрабатывают формы. 
Они могут отображать сообщение в шаблоне, но не отправляют его. Это означает, 
что вам не нужно создавать SuccessMessageMixin для них подклассы. 
EntryCreateView, EntryUpdateView и EntryDeleteView, с другой стороны, 
добавить уведомление в хранилище сообщений, поэтому вам нужно настроить их функциональность:
"""


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Новая запись создана успешно!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Ваша запись была обновлена!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )


"""
После наследования SuccessMessageMixin в EntryCreateView строке 39 и EntryUpdateView строке 46 
вы определяете success_message для них, в строках 43 и 49. 
Особенно, когда вы выполняете деструктивное действие, такое как удаление записи, очень важно дать обратную связь, 
что все прошло нормально. Чтобы отобразить сообщение DeleteView, 
вы должны добавить собственный .delete() метод, 
а также добавить свой собственный success_message в структуру сообщений вручную.

Вам понадобится этот дополнительный метод в строке 76, потому что DeleteView класс не является предком класса FormView. 
Вот почему вы можете пропустить добавление SuccessMessageMixin в EntryDeleteView строку 71.
"""


class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Ваша запись удалена!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
