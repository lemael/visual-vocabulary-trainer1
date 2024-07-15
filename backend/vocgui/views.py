"""
Simple REST API
"""
import os

import pyttsx3
from django.contrib.auth.decorators import login_required
from django.core import serializers  # pylint: disable=E0401
from django.http import HttpResponse  # pylint: disable=E0401
from django.shortcuts import redirect, render  # pylint: disable=E0401
from gtts import gTTS
from PyPDF2 import PdfReader

from .forms import PdfForm
from .models import AlternativeWord, Document, PdfFile, TrainingSet


@login_required

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

    alternative_words = AlternativeWord.objects.filter(document_id=document_id)
    alternative_words_list = serializers.serialize('json', alternative_words)
    return HttpResponse(alternative_words_list,
                        content_type="application/json")

import io
import os

from django.shortcuts import render
from gtts import gTTS
from PyPDF2 import PdfReader

from .models import PdfFile


def pdf_read(request):
    pdfs = PdfFile.objects.all()
    dernier_objet = pdfs.last()

    # Supprimer tous les objets sauf le dernier
    for objet in pdfs:
        if objet != dernier_objet:
            objet.delete()

    if not dernier_objet:
        return render(request, 'pdf_read.html', {
            'error': "Aucun fichier PDF trouvé."
        })

    pdf_path = os.path.join(
        '/home/mael/Dokumente/visual-vocabulary-trainer1/src/media/',
        dernier_objet.pdf_file.name
    )

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            page_content = {}
            for indx, pdf_page in enumerate(pdf_reader.pages):
                page_content[indx + 1] = pdf_page.extract_text()
    except FileNotFoundError:
        return render(request, 'pdf_read.html', {
            'error': f"Le fichier {pdf_path} n'a pas été trouvé."
        })

    # Convertir le texte en parole
    audio_fp = io.BytesIO()
    speech = gTTS(text=' '.join(page_content.values()), lang='fr')
    speech.write_to_fp(audio_fp)
    audio_fp.seek(0)
    mp3_filename = dernier_objet.title+".mp3"
    # Enregistrer le résultat en tant que fichier MP3
    mp3_path = os.path.join(
        "/home/mael/Dokumente/visual-vocabulary-trainer1/src/media/",
        mp3_filename
    )
    with open(mp3_path, 'wb') as f:
        f.write(audio_fp.getbuffer())

    # Vérifier que le fichier MP3 a été créé
    if os.path.exists(mp3_path):
        print("Le fichier MP3 a été créé avec succès.")
    else:
        print("Une erreur s'est produite lors de la création du fichier MP3.")

    return render(request, 'pdf_read.html', {
        'pdf_content': page_content,
        'pdfs': [dernier_objet],
        'audio_file': mp3_filename
    })



def upload_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_read')
    else:
        form = PdfForm()
    return render(request, 'upload_pdf.html', {'form': form})

def grammar(request):
    return render(request, 'grammar.html')

def vocabulary(request):
    return render(request, 'vocabulary.html')

def bucher(request):
    return render(request, 'bucher.html')