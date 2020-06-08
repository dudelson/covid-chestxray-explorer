from django.db import models

# Create your models here.

class ChestXrayImage(models.Model):
    ''' This metadata comes from the dataset repository. See
        https://github.com/ieee8023/covid-chestxray-dataset/blob/master/SCHEMA.md
        for more details. '''


    ''' internal id used to link multiple images of the same patient '''
    patient_id = models.IntegerField()

    ''' days since symptoms/hospitalization '''
    offset = models.IntegerField()

    sex = models.CharField(max_length=1, choices=[('M', 'Male'),('F', 'Female')])

    age = models.IntegerField()

    ''' type of pneumonia identified '''
    finding = models.CharField(max_length=10000)

    ''' whether the patient survived (Y/N/blank) '''
    survival = models.BooleanField()

    ''' whether the patient was ventillated at any point (Y/N/blank) '''
    intubated = models.BooleanField()

    ''' whether the patient was in the ICU at any point (Y/N/blank) '''
    went_icu = models.BooleanField()

    ''' whether the patient needed supplemental oxygen at any point (Y/N/blank) '''
    needed_supplemental_o2 = models.BooleanField()

    ''' whether the patient was successfully extubated (Y/N/blank) '''
    extubated = models.BooleanField()

    ''' temperature of the patient at the time the image was taken, in deg C '''
    temperature = models.DecimalField(max_digits=5, decimal_places=2)

    ''' partial pressue of oxygen saturation at the time the image was taken, in percent '''
    percent_o2_saturation = models.DecimalField(max_digits=4, decimal_places=2)

    ''' white blood cell count at the time the image was taken, in 10^3/uL '''
    wbc_count = models.DecimalField(max_digits=6, decimal_places=2)

    ''' neutrophil cell count at the time the image was taken, in 10^3/uL '''
    netrophil_count = models.DecimalField(max_digits=6, decimal_places=2)

    ''' lymphoctye cell count at the time the image was taken, in 10^3/uL '''
    lymphoctye_count = models.DecimalField(max_digits=6, decimal_places=2)

    ''' perspective that the xray was taken from '''
    perspective_choices = [
        ('PA', 'Posteroanterior'),
        ('AP', 'Anteroposterior'),
        ('APS', 'Anteroposterior Supine'),
        ('L', 'Lateral'),
        ('AX', 'Axial'),
        ('CO', 'Coronal'),
    ]
    xray_view = models.CharField(max_length=3, choices=perspective_choices)

    ''' CT, xray, or something else '''
    modality = models.CharField(max_length=100)

    ''' date on which the image was acquired '''
    image_date = models.DateField()

    ''' hospital name, city, state, country '''
    location = models.CharField(max_length=1000)

    ''' URL of image file on cloudinary '''
    image_file = models.URLField(max_length=500)

    ''' DOI of the research article that provided the image '''
    study_doi = models.CharField(max_length=1000)

    ''' URL of the research article that provided the image '''
    study_url = models.URLField(max_length=500)

    image_license = models.CharField(max_length=1000)

    ''' clinical notes about the image and/or the patient '''
    clinical_notes = models.CharField(max_length=10000)

    ''' additional misc notes, e.g. citations/credit '''
    other_notes = models.CharField(max_length=10000)
