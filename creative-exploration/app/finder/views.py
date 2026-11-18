from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Bookmark, Service
from .search import lookup


class DisplayNameForm(forms.Form):
    display_name = forms.CharField(max_length=150)


def signup(request):
    form = UserCreationForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "form.html", {"form": form, "heading": "Create account"})


@login_required
def account(request):
    form = DisplayNameForm(request.POST if request.method == "POST" else None,
                           initial={"display_name": request.user.first_name})
    if request.method == "POST" and form.is_valid():
        request.user.first_name = form.cleaned_data["display_name"]
        request.user.save(update_fields=["first_name"])
        return redirect("home")
    return render(request, "form.html", {"form": form, "heading": "Edit display name"})


@login_required
def home(request):
    query = request.GET.get("q", "")
    label, results = lookup(query[:100], Service.objects.order_by("name"))
    saved = Bookmark.objects.filter(owner=request.user).select_related("service").order_by("-saved", "-pk")
    return render(request, "home.html", {"query": query, "searched": "q" in request.GET,
                  "label": label, "results": results, "saved": saved})


@login_required
@require_POST
def save(request, pk):
    service = get_object_or_404(Service, pk=pk)
    Bookmark.objects.get_or_create(owner=request.user, service=service)
    return redirect("home")
