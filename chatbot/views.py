from django.shortcuts import render, redirect
from .forms import UploadPDFForm, QuestionForm
from .utils import get_pdf_text, get_text_chunks, get_vector_store, user_input

def index(request):
    if request.method == 'POST':
        pdf_form = UploadPDFForm(request.POST, request.FILES)
        if pdf_form.is_valid():
            pdf_files = request.FILES.getlist('pdfs')
            raw_text = get_pdf_text(pdf_files)
            text_chunks = get_text_chunks(raw_text)
            get_vector_store(text_chunks)
            return redirect('ask_question')
    else:
        pdf_form = UploadPDFForm()
    
    return render(request, 'index.html', {'pdf_form': pdf_form})

def ask_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.cleaned_data['question']
            response = user_input(question)
            return render(request, 'answer.html', {'question': question, 'response': response})
    else:
        question_form = QuestionForm()

    return render(request, 'ask_question.html', {'question_form': question_form})
