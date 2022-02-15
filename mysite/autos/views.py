from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
from autos.forms import AutoForm

# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = "__all__"
    success_url = reverse_lazy('autos:all')


class AutoCreate(LoginRequiredMixin, View):
    template = "autos/auto_form.html"
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = AutoForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AutoForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class AutoUpdate(LoginRequiredMixin, View):
    template = "autos/auto_form.html"
    success_url = reverse_lazy('autos:all')
    model = Auto

    def get(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(request.POST, instance=auto)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)

class AutoDelete(LoginRequiredMixin, View):
    template = "autos/auto_confirm_delete.html"
    success_url = reverse_lazy('autos:all')
    model = Auto

    def get(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = AutoForm(instance=auto)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        auto.delete()
        return redirect(self.success_url)