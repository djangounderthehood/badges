# MANDATORY
# pdf template
PDF_TEMPLATE = 'template.pdf'
PDF_SIZE = (338,338) # in pixels

# csv data
CSV_FILE = 'guests.csv'

# text properties
FONT_NAME = ['fonts/Lato-Regular.ttf', 'fonts/Lato-Semibold.ttf', 'fonts/Lato-Heavy.ttf', 'fonts/Lato-Light.ttf']
# hpostion is counted from the top
HPOSITION = 130 # pixels from the top, your text will be centered
FONT_SIZE = 23


# OPTIONAL
# generated files
FILENAME_LENGTH = 12
# this is base filename length - 3 more chars will be added at the end, so you can have non-unique csv fields
# (cause filenames are generated from your csv fields too)

# if the csv field was empty we don't generate pdf file, if you want other behaviour, change this
GENERATE_EMPTY = False
