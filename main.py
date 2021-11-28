def sort_sentence(sentence):
    sentence = sentence + " +"
    i=0
    j=-1
    words = []
    for c in sentence:
        if c == ' ':
            words.append(sentence[j+1:i])
            j=i
        i+=1

    words = sorted(words,key=len)

    sentence = ""
    for w in words:
        sentence = sentence + " " + w

    return sentence[1:].capitalize()