import mechanize
br = mechanize.Browser()
br.open("http://www.google.com/")
for f in br.forms():
    print f