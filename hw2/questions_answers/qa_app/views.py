from .models import Question
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import AddQuestionForm, AnswerForm

class QuestionList(ListView):
    model = Question
    context_object_name = 'questions'

def new_question(request):
    if request.method == "POST":
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            print(question)
            question.save()
        return redirect('questions')
    else:
        form = AddQuestionForm()
        return render(request, 'qa_app/new_question.html', {'form': form})

def new_answer(request, question_id):
    if request.method == "POST":
        form = AnsweForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
        return redirect('questions')
    else:
        data = {
            'question': question_id
        }
        form = AnswerForm(data)
        return render(request, 'qa_app/answer.html', {'form': form})
