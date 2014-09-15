# MANDATORY
# pdf template
PDF_TEMPLATE = 'template.pdf'
PDF_SIZE = (210,295) # in pixels

# csv data
CSV_FILE = 'guests.csv'
COLUMN = 'Ticket First Name'

# text properties
FONT_NAME = ['fonts/Roboto-Thin.ttf', 'fonts/Roboto-Regular.ttf']
# hpostion is counted from the top
HPOSITION = 202 # this means 160 pixels from the top, your text will be centered
FONT_SIZE = 23


# OPTIONAL
# generated files
FILENAME_LENGTH = 12
# this is base filename length - 3 more chars will be added at the end, so you can have non-unique csv fields
# (cause filenames are generated from your csv fields too)

# if the csv field was empty we don't generate pdf file, if you want other behaviour, change this
GENERATE_EMPTY = False
