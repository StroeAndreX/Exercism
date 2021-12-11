def convert(number):
    sounds = ["Pling", "Plang", "Plong"]
    value = [(number % 3 == 0), (number % 5 == 0), (number % 7 == 0)];
    result = ""

    for x in range(3):
        if(value[x]): result += sounds[x] 

    if(result != ""): return result
    else: return str(number)