from helper import Converter

path = r'hayeren/letters.json'

class To_Armenian():


    def __init__(self, path):

        self.obj = Converter(path)
        

    def search(self, key):

        word = self.obj.deserialization()
        if key in word.keys():
            return word[key]
        else:
            return None
    

    def check(self, text):

        arm_text = []
        text = text.split(' ')
        for word in text:
            index = 0
            while index < len(word):
                walk = 3
                while walk > 0:
                    key = word[index : index + walk].lower()
                    result = self.search(key)
                    if result is None:
                        walk -= 1
                    else:
                        if key == word[index : index + walk]:
                            if (key == 'e') and (index == 0):
                                arm_text.append('է')
                            elif(key == 'o') and (index == 0):
                                arm_text.append('օ')
                            else:
                                arm_text.append(result)
                            index += walk
                            break
                        else:
                            if (key == 'e') and (index == 0):
                                arm_text.append('Է')
                            elif(key == 'o') and (index == 0):
                                arm_text.append('Օ')
                            else:
                                arm_text.append(result.upper())
                            index += walk
                            break
            arm_text.append(' ')
        print(''.join(arm_text))


def main():
    obj = To_Armenian(path)
    text = input("Please enter your text: ")
    obj.check(text)


if __name__ == '__main__':
    main()