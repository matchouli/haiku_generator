import random
import torch


class BertGenerator():
    def __init__(self, bert=True):
        if bert:
            self.model = self._load_bert()
        
        self.masked_lines = [
            'Je <mask> ',
            'Tu <mask> ',
            'Il <mask> ',
        ]

    def _load_bert(self):
        print('Loading BERT ...')
        model = torch.hub.load('pytorch/fairseq', 'camembert')
        return model

    def generate_bert_haiku(self, password):
        poem = []
        words = password.split('_')
        for word in words:
            if word.endswith('er'):
                masked_line = 'Pour ' + word + ' à <mask> !'
            elif word.endswith('ons'):
                masked_line = 'Mais ' + word + " <mask> !"
            else:
                masked_line = random.choice(self.masked_lines) + word.upper()
            temp = self.model.fill_mask(masked_line, topk=3)
            poem.append(temp[0][0])
        full_poem = self._join_poem(poem)
        return full_poem


    def _join_poem(self, poem):
        possibilities = []
        possibilities.append(poem[0] + ' et ' + poem[1] + ' quand ' + poem[2] + ' et que ' + poem[3])
        possibilities.append(poem[0] + ' quand ' + poem[1] + ' si ' + poem[2] + ' et que ' + poem[3])
        possibilities.append(poem[0] + ' et ' + poem[1] + ' car ' + poem[2] + ' quand ' + poem[3])
        
        return random.choice(possibilities)

