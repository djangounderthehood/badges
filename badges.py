# -*- coding: utf-8 -*-

from stereo import Layout
from stereo.fields import TextField


class FirstNameField(TextField):
    font_name = 'Lato-Heavy'
    font_size = 35
    fit_text = True
    text_align = TextField.TEXT_ALIGN_CENTER
    color = 'blue'
    top = 115

    def render(self):
        self.data = self.data.upper()
        super(FirstNameField, self).render()


class LastNameField(FirstNameField):
    font_name = 'Lato-Regular'
    font_size = 23
    top = 155


class RoleField(FirstNameField):
    font_name = 'Lato-Light'
    font_size = 16
    top = 200


class Badge(Layout):
    data_file = 'guests.csv'
    template_file = 'template.pdf'
    output_dir = 'output'
    skip_first_row = True
    width = 338
    height = 338
    fields = [
        FirstNameField,
        LastNameField,
        RoleField
    ]
    fonts = {
        'Lato-Heavy': 'fonts/Lato-Heavy.ttf',
        'Lato-Regular': 'fonts/Lato-Regular.ttf',
        'Lato-Light': 'fonts/Lato-Light.ttf'
    }
    debug_fields = False

    def generate_filename(self, row):
        return str(''.join([row[0], row[1]])).strip()
