from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PDFFile
from .forms import UploadPDFForm, QuestionForm
from .utils import get_pdf_text, get_text_chunks, get_vector_store, user_input
import os
from googleapiclient.discovery import build
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'Home_Student.html')

def es(request):
    return render(request, 'ES.html')

def unit(request):
    return render(request, 'unit.html')

def home_faculty(request):
    return render(request, 'Home_Faculty.html')

def upload(request):
    if request.method == 'POST':
        pdf_form = UploadPDFForm(request.POST, request.FILES) 
        pdfs = request.FILES.getlist('pdfs')
        chapter_name = request.POST.get('chapter_name')
        chapter_number = request.POST.get('chapter_number')
        print(chapter_name)
        print(chapter_number)
        
        for i in pdfs:
            print(str(i))
        # pdfs = request.FILES.getlist('pdfs')[0]
        # return HttpResponse("the file uploaded is" + str(pdfs))
        
        raw_text = get_pdf_text(pdfs)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks)
        return redirect('unit')

    else:
        pdf_form = UploadPDFForm()
    
    return render(request, 'Upload.html', {'pdf_form': pdf_form})

def unit(request):
    response = None
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.cleaned_data['question']
            response = user_input(question)  # Your custom function to handle the question
            return render(request, 'unit.html', {'question_form': question_form, 'question': question, 'response': response})
    else:
        question_form = QuestionForm()

    return render(request, 'unit.html', {'question_form': question_form})

def youtube_search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query:
            api_key = 'AIzaSyDe5wciQ_9A-rMqCJ13ALwvjEoZ0A6fvR0'  # Replace with your YouTube API key
            youtube = build('youtube', 'v3', developerKey=api_key)
            
            search_response = youtube.search().list(
                q=query,
                part='snippet',
                maxResults=5
            ).execute()
            
            results = []
            for item in search_response.get('items', []):
                if item['id']['kind'] == 'youtube#video':
                    video_data = {
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                        'thumbnail': item['snippet']['thumbnails']['default']['url'],
                        'channel': item['snippet']['channelTitle'],
                    }
                    results.append(video_data)
            
            return render(request, 'youtube_results.html', {'results': results})
        else:
            return JsonResponse({'results': []})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def youtube_page(request):
    return render(request, 'youtube_results.html')