# Generated by Django 3.0.7 on 2020-06-09 02:00

import os
import csv
from django.db import migrations

# since this is a one-time import:
#   - it is assumed that csv cols correspond 1-to-1 with db cols (because
#     currently they do)
#   - we are not concerned with the possibility of csv layout changing over time

# transform functions

# NOTE: putting the field name second is more readable, but for creating
# a model instance the field name needs to come first, so validation
# functions return a tuple (field_name, validated_value)
# (i.e. the order of the tuple is swapped)

def string_validator(s, field_name):
    ''' Validate a string which is expected to remain a string.

    Right now this function does nothing, but I'm creating it just in case
    there later turns out to be some basic validation that needs to be performed
    on all strings.
    '''
    return (field_name, s)


def integer_validator(s, field_name):
    ''' Validate a string which is expected to be an integer.

    <s> is a string which is expected to be an integer.
    <field_name> is the field name which is returned as the second part of
    the constructed tuple.
    '''
    try:
        return (field_name, int(s))
    except ValueError:
        return (field_name, None)


def float_validator(s, field_name):
    ''' Validate a string which is expected to be a float.

    <s> is a string which is expected to be a float.
    <field_name> is the field name which is returned as the second part of
    the constructed tuple.
    '''
    try:
        ret = float(s)
        ret = round(ret, 1)
        # print('float validator returns: {}'.format(ret))
        return (field_name, ret)
    except ValueError:
        return (field_name, None)


def date_validator(s, field_name):
    ''' Validate a string which is expected to be a date.
    Dates can be in any form, so no assumptions are made in that regard. '''

    from datetime import datetime as dt
    from django.utils import dateparse as dp


    def fill_defaults(date):
        ''' Given a date object, fill in some reasonable defaults for our use
        case. '''

        # From the python docs on strptime():
        #
        # > For the datetime.strptime() class method, the default value is
        # > 1900-01-01T00:00:00.000: any components not specified in the format
        # > string will be pulled from the default value.
        #
        # COVID-19 data is almost certainly from 2020, so there are better
        # defaults we can use in our specific case.

        # TODO: datetime.date objects are required to be valid dates, so there's
        # no way to represent the fact that some components of the date are
        # actually unknown. Perhaps in the future I'll write a wrapper object
        # or something that encapsulates this knowledge so that you can see it
        # in the UI (instead of misleading dates which appear complete but are
        # actually inaccurate).

        if date.year == 1900:
            return date.replace(year=2020)


    date_formats = [
        "%B %d, %Y",
        "%x",
        "%Y",
        "%B %d",
        "%B %Y",
        "%d %B %Y",
    ]

    for fmt in date_formats:
        try:
            d = dt.strptime(s, fmt).date()
            d = fill_defaults(d)
            return (field_name, d)
        except ValueError:
            pass  # keep looping!

    # if none of the above date formats worked, we try ISO format as a last
    # resort, which is conveniently handled by django's date utils
    try:
        d = dp.parse_date(s)
        return (field_name, None) if d is None else (field_name, d.date())
    except ValueError:
        return (field_name, None)


def url_validator(s, field_name):
    ''' Validate a string which is expected to be a URL. '''
    # URL validation is not actually performed here because django does that for
    # us, but I'm creating this method in case I do want to perform some sort of
    # additional validation for URLs in the future.
    return string_validator(s, field_name)


def enum_validator(s, options, field_name):
    ''' Validate a string which is expected to be one of a fixed set of options '''
    if s in options:
        return (field_name, s)
    return (field_name, None)


''' Validate a string which is expected to indicate the xray image perspective '''
perspective_validator = lambda s: (
        enum_validator(
            s,
            ['PA', 'AP', 'L', 'AP Supine', 'Axial', 'Coronal'],
            'xray_view'
        )
)

''' Validate a string which is expected to indicate the image modality '''
modality_validator = lambda s: enum_validator(s, ['X-ray', 'CT'], 'modality')

def yes_no_validator(s, field_name):
    ''' Validate a string which is expected to be either "Y", "N", or blank.

    <s> is a string expected to be one of the aforementioned values.
    <field_name> is the field name which is returned as the second part of
    the constructed tuple.
    '''
    if s.upper() == 'Y':
        return (field_name, True)
    elif s.upper() == 'N':
        return (field_name, False)
    else:
        return (field_name, None)


def sex_validator(s):
    ''' Validate a string which is expected to be either "M" or "F". '''
    s = s.upper()
    if s == 'M' or s == 'F':
        return ('sex', s)
    return ('sex', '')


# each transform function should accept a single argument: a string,
# which it is expected to transform and validate. Each function should return
# a tuple ('fieldName', transformedValue).
TRANSFORM_FUNCTIONS = [
    lambda s: string_validator(s, 'patient_id'),
    lambda s: integer_validator(s, 'offset'),
    sex_validator,
    lambda s: integer_validator(s, 'age'),
    lambda s: string_validator(s, 'finding'),
    lambda s: yes_no_validator(s, 'survival'),
    lambda s: yes_no_validator(s, 'intubated'),
    lambda s: yes_no_validator(s, 'intubation_present'),
    lambda s: yes_no_validator(s, 'went_icu'),
    lambda s: yes_no_validator(s, 'in_icu'),
    lambda s: yes_no_validator(s, 'needed_supplemental_o2'),
    lambda s: yes_no_validator(s, 'extubated'),
    lambda s: float_validator(s, 'temperature'),
    lambda s: float_validator(s, 'percent_o2_saturation'),
    lambda s: float_validator(s, 'wbc_count'),
    lambda s: float_validator(s, 'neutrophil_count'),
    lambda s: float_validator(s, 'lymphocyte_count'),
    perspective_validator,
    modality_validator,
    lambda s: date_validator(s, 'image_date'),
    lambda s: string_validator(s, 'location'),
    lambda s: url_validator(s, 'image_url'),
    lambda s: string_validator(s, 'study_doi'),
    lambda s: url_validator(s, 'study_url'),
    lambda s: string_validator(s, 'image_license'),
    lambda s: string_validator(s, 'clinical_notes'),
    lambda s: string_validator(s, 'other_notes'),
]

CSV_DATA_FILE = os.path.expanduser('~/covid-chestxray-dataset/metadata.csv')

def import_csv_data(apps, schema_editor):
    ChestXrayImage = apps.get_model('chex', 'ChestXrayImage')
    new_models = []

    with open(CSV_DATA_FILE) as f:
        rows = csv.reader(f)
        # filter out all rows corresponding to images in the "volumes/" folder
        # the value "folder" also takes care of the 0th row, which is just headers
        rows = filter(lambda r: r[21] not in ['volumes', 'folder'], rows)
        # remove column 21 from the remaining rows, since it's not part of
        # the data model, as well as extraneous final row
        rows = map(lambda r: r[:21] + r[22:-1], rows)
        for row in rows:
            if len(row) != 27:
                # I've inspected the data manually and it appears like this
                # should never happen, but this is a failsafe against a
                # malformed row corrupting the data import
                print('Warning: Skipping row [{}, {}, {}...], which only has {} columns'
                      .format(row[0], row[1], row[2], len(row)))
            model_values = [fn(s) for fn, s in zip(TRANSFORM_FUNCTIONS, row)]
            model_values_dict = dict(model_values)
            # print('Model values dict is: {}'.format(model_values_dict))
            new_models.append(ChestXrayImage(**model_values_dict))

    db_alias = schema_editor.connection.alias
    ChestXrayImage.objects.using(db_alias).bulk_create(new_models)


class Migration(migrations.Migration):

    dependencies = [
        ('chex', '0008_auto_20200610_2340'),
    ]

    operations = [
        migrations.RunPython(import_csv_data)
    ]