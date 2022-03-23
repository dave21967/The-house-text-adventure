from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.scena = "main menu"
        self.run = True

    def update(self):
        while self.run:
            if self.scena == 'main menu':
                self.main_menu()
            elif self.scena == 'chapter1':
                self.capitolo_1()

    def main_menu(self):
        print("Benvenuto in The House!")
        print("Un'avventura testuale horror investigativa...")
        print("Seleziona la tua scelta: ")
        print("1) Inizia")
        print("2) Carica")
        print("3) Esci")
        
        scelta = input("--> ")
        if scelta == '1':
            self.scena = 'chapter1'
        elif scelta == '2':
            pass
        elif scelta == '3':
            self.run = False

    def capitolo_1(self):
        print("Benvenuto nella nuova avventura!")
        self.run = False