
# legacy way # traditional way
fw = open("languages.txt","w")
fw.write('unix\n')
fw.write('java\n')
fw.close()


# pythonic way
# context manager
# if any line starts with keyword  with .. we call it as context manager
# not required to close the file
# file gets closed automatically
with open("languagesinfo.txt","w") as fw:
    fw.write('unix\n')
    fw.write('java\n')

