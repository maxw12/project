from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question, Choice, Submission


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_submission_list'  # submission_list

    def get_queryset(self):
        return Submission.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
                # Submission


class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Submission

    def get_queryset(self):
        return Submission.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'blog/detail.html', {'question': question,
                                                    'error_message': "you didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return redirect after successful dealing with POST data, prevent from posted twice
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
