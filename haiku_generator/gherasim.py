"""
Main
"""
import random

class GherasimGenerator():
    def __init__(self):
        self.debuts = [
            "Je te ",
            "Tu me ",
            "mais toi, tu me ",
            "alors je te ",
            "alors toi tu te ",
            "et si, ",
            "jour et nuit, je te ",
            "jour et nuit, tu me ",
            "Tu nous ",
            "Je nous ",
        ]

        self.debuts_voyelle = [
            "Je t'",
            "Tu m'",
            "mais toi, tu m'",
            "alors je t'",
            "alors toi tu t'",
            "et si, ",
            "jour et nuit, je t'",
            "jour et nuit, tu m'",
            "Tu nous ",
            "Je nous ",
        ]

        self.voyelles = ["a", "e", "i", "o", "u", "y"]


    def generate_gherasim_haiku(self, words):
        poem = []
        for word in words:
            word = '-' + word + '-'
            if word.endswith('ant'):
                temp = word
            elif word.endswith('ent'):
                temp = "Ils " + word
            elif word.endswith('ez'):
                temp = "Vous " + word
            elif word.endswith('er'):
                temp = "Pour " + word
            elif word[0] not in self.voyelles:
                choice = random.choice(self.debuts)
                temp = choice + word
            else:
                choice = random.choice(self.debuts_voyelle)
                temp = choice + word
            poem.append(temp)
        full_poem = '\n'.join(poem)
        return full_poem
        
