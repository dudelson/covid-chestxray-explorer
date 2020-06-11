from django.db import models

# Create your models here.

class ChestXrayImage(models.Model):
    ''' This metadata comes from the dataset repository. See
        https://github.com/ieee8023/covid-chestxray-dataset/blob/master/SCHEMA.md
        for more details. '''


    ''' internal id used to link multiple images of the same patient '''
    patient_id = models.CharField(max_length=10)

    ''' days since symptoms/hospitalization '''
    offset = models.IntegerField(null=True)

    sex = models.CharField(max_length=1, choices=[('M', 'Male'),('F', 'Female'),('', 'Unknown')])

    age = models.IntegerField(null=True)

    ''' type of pneumonia identified '''
    finding = models.CharField(max_length=100)

    ''' whether the patient survived (Y/N/blank) '''
    survival = models.BooleanField(null=True)

    ''' whether the patient was ventillated at any point (Y/N/blank) '''
    intubated = models.BooleanField(null=True)

    ''' this field is present in the CSV metadata but not in the schema
    description. I think it probably represents whether the patient was
    intubated at the time the image was taken specifically. '''
    intubation_present = models.BooleanField(null=True)

    ''' whether the patient was in the ICU at any point (Y/N/blank) '''
    went_icu = models.BooleanField(null=True)

    ''' this field is present in the CSV metadata but not in the schema
    description. I think it probably represents whether the patient was
    in the ICU at the time the image was taken specifically. '''
    in_icu = models.BooleanField(null=True)

    ''' whether the patient needed supplemental oxygen at any point (Y/N/blank) '''
    needed_supplemental_o2 = models.BooleanField(null=True)

    ''' whether the patient was successfully extubated (Y/N/blank) '''
    extubated = models.BooleanField(null=True)

    ''' temperature of the patient at the time the image was taken, in deg C '''
    # temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperature = models.FloatField(null=True)

    ''' partial pressue of oxygen saturation at the time the image was taken, in percent '''
    # TODO: validate that this is between 0 and 100 inclusive
    # percent_o2_saturation = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    percent_o2_saturation = models.FloatField(null=True)

    ''' white blood cell count at the time the image was taken, in 10^3/uL '''
    # wbc_count = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    wbc_count = models.FloatField(null=True)

    ''' neutrophil cell count at the time the image was taken, in 10^3/uL '''
    # neutrophil_count = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    neutrophil_count = models.FloatField(null=True)

    ''' lymphocyte cell count at the time the image was taken, in 10^3/uL '''
    # lymphocyte_count = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    lymphocyte_count = models.FloatField(null=True)

    ''' perspective that the xray was taken from '''
    perspective_choices = [
        ('PA', 'Posteroanterior'),
        ('AP', 'Anteroposterior'),
        ('L', 'Lateral'),
        ('AP Supine', 'Anteroposterior Supine'),
        ('Axial', 'Axial'),
        ('Coronal', 'Coronal'),
    ]
    xray_view = models.CharField(max_length=10, choices=perspective_choices)

    ''' CT, xray, or something else '''
    modality = models.CharField(max_length=100)

    ''' date on which the image was acquired '''
    image_date = models.DateField(null=True)

    ''' hospital name, city, state, country '''
    location = models.CharField(max_length=1000)

    ''' URL of image file on cloudinary '''
    image_url = models.URLField(max_length=500)

    ''' DOI of the research article that provided the image '''
    study_doi = models.CharField(max_length=200)

    ''' URL of the research article that provided the image '''
    study_url = models.URLField(max_length=500)

    image_license = models.CharField(max_length=50)

    ''' clinical notes about the image and/or the patient '''
    clinical_notes = models.CharField(max_length=10000)

    ''' additional misc notes, e.g. citations/credit '''
    other_notes = models.CharField(max_length=10000)
