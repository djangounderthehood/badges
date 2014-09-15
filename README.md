# HACKWAW #4 Badge Generator

(Heavily based on wedding invitation generator by @83tb, which was based on HACKWAW's badge generator by @olasitarska, https://gist.github.com/olasitarska/5245471 :D)

It's just a very simple pdf generator. It takes csv file column and put each row text, formats it and inserts into the pdf.
Obviously it will generate a lot of pdfs if you have a lot of rows in a csv file (it takes seconds to generate hundreds, so..)
You can use to generate any type of pdf files which requires embedding different text in each file.

Just put your template pdf file, font file and csv file in the folder with the script and configure settings below

To install all requirements:

    pip install -r requirements.txt

When you're done, just do:

    python generate.py
