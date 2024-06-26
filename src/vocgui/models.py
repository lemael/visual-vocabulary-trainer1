"""
Models for the UI
"""
from django.db import models  # pylint: disable=E0401


class TrainingSet(models.Model):  # pylint: disable=R0903
    """
    Training sets have a title and contain words
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    # pylint: disable=R0903
    class Meta:
        """
        Define user readable name of TrainingSet
        """
        verbose_name = 'Lektion'
        verbose_name_plural = 'Lektionen'


class Document(models.Model):  # pylint: disable=R0903
    """
    Contains words + images and relates to a training set
    """
    word = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/')
    audio = models.FileField(upload_to='audio/', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    training_set = models.ForeignKey(TrainingSet,
                                     on_delete=models.CASCADE,
                                     related_name='documents')

    def __str__(self):
        return self.training_set.title + " >> " + self.word

    # pylint: disable=R0903
    class Meta:
        """
        Define user readable name of Document
        """
        verbose_name = 'Wort'
        verbose_name_plural = 'Wörter'

class AlternativeWord(models.Model):
    """
    Contains words for a document
    """
    alt_word = models.CharField(max_length=255)
    document = models.ForeignKey(Document,
                                 on_delete=models.CASCADE,
                                 related_name='alternatives')

    def __str__(self):
        return self.document.training_set.title + " >> " + self.document.word + ">> Alternative Wörter: " + self.alt_word

    # pylint: disable=R0903
    class Meta:
        """
        Define user readable name of Document
        """
        verbose_name = 'Alternatives Wort'
        verbose_name_plural = 'Alternative Wörter'

#create class pdfFile
class PdfFile(models.Model):
    pdf_file = models.FileField(upload_to='pdfFile/')
    title = models.CharField(max_length=100, default='default title')
    def __str__(self):
        return str(self.pdf)