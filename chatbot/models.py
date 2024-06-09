
from django.db import models

class PDFFile(models.Model):
    chapter_name = models.CharField(max_length=100)
    chapter_number = models.IntegerField()
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f'{self.chapter_name} - Chapter {self.chapter_number}' 