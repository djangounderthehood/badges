# -*- coding: utf-8 -*-

from stereo import Layout
from stereo.fields import TextField


class NameField(TextField):
    font_name = 'Lato-Heavy'
    font_size = 35
    text_align = TextField.TEXT_ALIGN_CENTER
    color = 'blue'
    top = 120
    left = 55
    width = 180
    
    def get_name(self):
        ticket_name, preferred_name = self.data.split('||')[0], self.data.split('||')[1]
        if not preferred_name or preferred_name == '-':
            return ticket_name.upper()
        else:
            return preferred_name.upper()

    def render(self):
        name = self.get_name()
        
        first_line = name.split(' ')[0]
        second_line = name.replace(first_line, '')
        
        if not second_line:
            self.data = first_line
            super(NameField, self).render()
        else:
            self.data = first_line
            self.top -= int(self.font_size / 2)
            super(NameField, self).render()
            
            self.data = second_line
            self.top += int(self.font_size / 2) + 10
            self.font_size -= 10
            self.font_name = 'Lato-Regular'
            super(NameField, self).render()


class RoleField(TextField):
    font_name = 'Lato-Light'
    font_size = 16
    top = 200
    text_align = TextField.TEXT_ALIGN_CENTER
    color = 'blue'

    def render(self):
        self.data = self.data.upper()
        super(RoleField, self).render()


class Badge(Layout):
    data_file = 'tito.csv'
    template_file = 'template.pdf'
    output_dir = 'output'
    skip_first_row = True
    width = 290
    height = 290
    fields = [
        RoleField,
        NameField,
    ]
    fonts = {
        'Lato-Heavy': 'fonts/Lato-Heavy.ttf',
        'Lato-Regular': 'fonts/Lato-Regular.ttf',
        'Lato-Light': 'fonts/Lato-Light.ttf'
    }
    debug_fields = False

    def generate_filename(self, row):
        return str(''.join([row[0], row[1]])).strip()
