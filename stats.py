
def get_word_count(text):
    words = []
    word_count = 0

    words = text.split()

    for i in range(0,len(words)):
        word_count += 1

    return word_count

def count_characters(text):
   
    character_dct = {}
    words = []

    words = text.split()

    for i in range(0,len(words)):

        for c in words[i]:

            character = c.lower()

            if character not in character_dct:
                character_dct[character] = 0

            if character in character_dct:
                character_dct[character] += 1
       
    return character_dct

def sort_dict(dict):

    sorted_list = []

    for char in dict:
        if char.isalpha() == True:
            innerdict= {}
            innerdict["char"] = char
            innerdict["num"] = dict[char]
            sorted_list.append(innerdict)

    def sort_on(dict):
        return dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)

   

    return sorted_list

