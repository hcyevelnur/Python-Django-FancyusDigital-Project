from django.shortcuts import render,get_object_or_404
from .models import TeamPost

# Create your views here.


def team(request):
    teams = TeamPost.objects.all()
    context = {
        'title': 'Team',
        'teams': teams

    }
    return render(request, 'team.html', context=context)


def team_detail(request, pk):
    team = get_object_or_404(TeamPost, pk=pk)
    title = team.name

    return render(request, 'team-detail.html', {'team': team, 'title': title})