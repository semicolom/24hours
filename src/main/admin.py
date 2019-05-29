from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models
from .forms import GroupsForm


class TeamInline(admin.TabularInline):
    model = models.Team
    extra = 0

    readonly_fields = [
        'name',
        'category',
        'modality',
        'points',
        'points_against',
        'games_played',
        'games_won',
        'games_lost',
    ]


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'category',
        'modality',
        'group',
        'points',
        'points_against',
        'games_played',
        'games_won',
        'games_lost',
    ]

    readonly_fields = [
        'points',
        'points_against',
        'games_played',
        'games_won',
        'games_lost',
    ]

    list_filter = [
        'category',
        'modality',
        'group',
    ]

    search_fields = [
        'name',
    ]

    actions = ['add_teams']

    def add_teams(self, request, queryset):
        form = None

        if 'post' in request.POST:
            form = GroupsForm(request.POST)

            if form.is_valid():
                group = form.cleaned_data['group']

                queryset.update(group=group)

                self.message_user(request, "Grups afegits correctament")

                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = GroupsForm(
                initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)}
            )

        return render(
            request,
            'main/admin/add_teams.html',
            context={
                **self.admin_site.each_context(request),
                'form': form,
                'teams': queryset,
                'back_url': request.get_full_path(),
            }
        )
    add_teams.short_description = "Afegir equips seleccionats a un grup"


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'category',
        'modality',
    ]

    list_filter = [
        'category',
        'modality',
    ]

    search_fields = [
        'name',
    ]

    inlines = [
        TeamInline,
    ]


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'for_finals',
    ]


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'home_team',
        'home_team_points',
        'away_team',
        'away_team_points',
        'start_time',
        'game_field',
    ]

    list_filter = [
        'game_field',
    ]

    search_fields = [
        'name',
        'home_team__name',
        'away_team__name',
    ]
