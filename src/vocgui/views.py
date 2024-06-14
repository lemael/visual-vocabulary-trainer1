"""
Simple REST API
"""
from django.http import HttpResponse  # pylint: disable=E0401
from django.core import serializers  # pylint: disable=E0401
from django.shortcuts import render, redirect  # pylint: disable=E0401

from .models import TrainingSet, Document, AlternativeWord, PdfFile

from .forms import PdfForm

from PyPDF2 import PdfReader

import os



def index(request):  # pylint: disable=W0613
    """
    Display JS app that lets users train
    """
    # pylint: disable=E1101
    return render(request, 'index.html')


def api_training_sets(request):  # pylint: disable=W0613
    """
    API endpoint to get all training sets
    """
    training_sets = (TrainingSet.objects.all())
    training_set_list = serializers.serialize('json', training_sets)
    return HttpResponse(training_set_list, content_type="application/json")


def api_documents(request, training_set_id=None):  # pylint: disable=W0613
    """
    API endpoint to get all documents of a training set
    """
    documents = Document.objects.filter(training_set__id=training_set_id)
    documents_list = serializers.serialize('json', documents)
    return HttpResponse(documents_list, content_type="application/json")

def api_alternative_words(request, document_id=None):
    """
    API endpoint to get all alternative words of a document
    """

    alternative_words = AlternativeWord.objects.filter(document_id = document_id)
    alternative_words_list = serializers.serialize('json', alternative_words)
    return HttpResponse(alternative_words_list, content_type="application/json")


def pdf_read(request):
    pdfs = PdfFile.objects.all()
    for x in pdfs:
       pdf_path = os.path.join('/home/mael/Dokumente/visual-vocabulary-trainer1/src/media/', x.pdf_file.name)
       pdf_reader = PdfReader(open(pdf_path, 'rb'))

    page_content = {}

    for indx, pdf_page in enumerate(pdf_reader.pages):
        page_content[indx + 1] = pdf_page.extract_text()
    print(page_content)
    return render(request, 'pdf_read.html', { 'pdf_content': page_content, 'pdfs': pdfs})


def upload_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_read')
    else:
        form = PdfForm()
    return render(request, 'upload_pdf.html', {'form': form})