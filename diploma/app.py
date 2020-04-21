import datetime
import os
import sys, json

# Read data from stdin


def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])


serverResponse = read_in()
inputPdf = ""  # static value to be replaced
for txt in serverResponse:
    inputPdf += txt

# inputPdf = "en.jpg"

inputLanguage = "English"  # static value to be replaced
# print(os.listdir())
location = "diploma/downloads"
outputTiff = str(datetime.datetime.now().timestamp())
outputText = str(datetime.datetime.now().timestamp()) + "output"

verifierCounter = 0


def action1():
    return True


def action2():
    return True


def action3():
    return True


def action4():
    return True


strings = {'l’enseignement': action1, 'devant le jury': action2, 'université': action3, 'DOCTEUR': action4}
convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText

if inputLanguage == "French":
    strings = {'l’enseignement': action1, 'devant le jury': action2, 'université': action3, 'DOCTEUR': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l fra"
elif inputLanguage == "English":
    strings = {'BY CONDUCTING ORIGINAL RESEARCH': action1, 'HAS DEMONSTRATED THOROUGH KNOWLEDGE OF': action2,
               'DOCTOR OF PHILOSOPHY': action3, 'RESEARCH': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l eng"
elif inputLanguage == "German":
    strings = {'Medizinische Fakultät': action1, 'Doktorin': action2, 'Bundesgesetz': action3,
               'Gegen diesen Bescheid': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l deu"
elif inputLanguage == "Arabic":
    strings = {'إجارة': action1, 'البشري': action2, 'البشري': action3, 'إجارة': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l ara"
elif inputLanguage == "Russian":
    strings = {'лИПЛОоМ': action1, 'ДОКТОРА НАУК': action2, 'ПРИСУЖДЕНА УЧЕНАЯ СТЕПЕНЬ': action3,
               'Совете МинистРов': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l rus"
elif inputLanguage == "Italian":
    strings = {'MINISTRO': action1, 'DIPLOMA': action2, 'RICERCA': action3, 'IN NOME DELLA LEGGE': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l ita"
elif inputLanguage == "Chinese":
    strings = {'MINISTRO': action1, 'DIPLOMA': action2, 'RICERCA': action3, 'IN NOME DELLA LEGGE': action4}
    convertCommand = "tesseract " + location + "/" + inputPdf + " outputs/" + outputText + " -l chi_sim"

os.system(convertCommand)
# print(convertCommand)


with open("diploma/outputs/" + "a" + ".txt", 'r', encoding='utf-8') as file:
    for line in file:
        for search, action in strings.items():
            if search in line:
                if action():
                    verifierCounter += 1

if verifierCounter > 3 or (verifierCounter == 2 and inputLanguage == "Arabic"):
    print("verified")
else:
    print("false")

