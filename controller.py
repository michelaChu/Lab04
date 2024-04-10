import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self, e):
        txtIn= self._view._txtIn.value
        language= self._view._ddLingua.value
        modality= self._view._ddRicerca.value

        if txtIn=="":
            self._view._lvOut.controls.append(ft.Text("Il campo non può essere vuoto", color="red"))
            self._view.update()
            return

        if language== None:
            self._view._lvOut.controls.append(ft.Text("Il campo non può essere vuoto", color="red"))
            self._view.update()
            return

        if modality== None:
            self._view._lvOut.controls.append(ft.Text("Il campo non può essere vuoto", color="red"))
            self._view.update()
            return

        paroleErrate, tempo = self.handleSentence(txtIn, language, modality)

        self._view._lvOut.controls.append(ft.Text("Frase inserita: "+txtIn))
        self._view._lvOut.controls.append(ft.Text("Frase parole errate: " +paroleErrate))
        self._view._lvOut.controls.append(ft.Text("Tempo richoesto dalla ricerca: " +str(tempo)))


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
