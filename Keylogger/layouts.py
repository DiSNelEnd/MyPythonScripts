from datetime import datetime


class Layouts:

    __rus_layout = { 'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 
                    'p':'з' ,'[':'х', ']':'ъ','a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р', 
                    'j':'о', 'k':'л', 'l':'д', ';':'ж', "'":'э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м',
                    'b':'и', 'n':'т', 'm': 'ь', ',':'б', '.':'ю', '/':'.', '?':',', '!':'!', '&':'?'
                    }
    __rus_word = " | " 

    @staticmethod
    def write_char(char):
        symbol = str(char).lower()
        if(len(symbol) > 1):
            return 
        Layouts.__rus_word += Layouts.__get_rus_char(Layouts,symbol)
    
    @staticmethod
    def get_word():
        word= Layouts.__rus_word
        date= Layouts.__get_date()
        if word == " | ":
            return ""
        Layouts.__rus_word = " | "
        return word + date
    
    def __get_rus_char(self,char):
        if char in self.__rus_layout:
            return self.__rus_layout[char]
        else:
            return '' 

    def __get_date():
        date= datetime.now()
        return " | " + date.strftime("%H:%M:%S %d.%m.%Y")  