Wedding Invitation Generator

(Heavily based on HACKWAW's badge generator by @olasitarska, https://gist.github.com/olasitarska/5245471,
I just simplified it, made it configurable, and supported some additional usecases)

It's just a very simple pdf generator. It takes csv file column and put each row text, formats it and inserts into the pdf.
Obviously it will generate a lot of pdfs if you have a lot of rows in a csv file(it takes seconds to generate hundreds, so..)
You can use to generate any type of pdf files which requires embedding different text in each file.

Just put your template pdf file, font file and csv file in the folder with the script and configure settings below

To install or requirements:
pip install -r requirements.txt

When you're done, just do:
python wedding.py

