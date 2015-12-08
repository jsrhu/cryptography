def main():
    cipher = requestData()
    cipherFrequency = cipherFreq(cipher)
    alphaProb = probabilityArray()
    phiArray = Phi(cipherFrequency,alphaProb)
    phi = phiArray[0]
    key = phiArray[1]
    decodedText = decode(cipher,key)
    print "Encoded Text: ",cipher
    print "Phi Value: ",phi
    print "Key: ",key
    print "Decoded Text: "
    printOrdArray(decodedText)
    
def requestData():
    cipherText = input('ciphertext: ')
    return cipherText

def arrayCreate():
    array = []
    for i in range(26):
        array.append(0)

    return array

def printOrdArray(array):
    for i in array:
        print chr(i)

#init probability array
def probabilityArray():
    alphaProb = []
    alphaProb.append(.080)
    alphaProb.append(.015)
    alphaProb.append(.030)
    alphaProb.append(.040)
    alphaProb.append(.130)
    alphaProb.append(.020)
    alphaProb.append(.015)
    alphaProb.append(.060)
    alphaProb.append(.065)
    alphaProb.append(.005)
    alphaProb.append(.005)
    alphaProb.append(.035)
    alphaProb.append(.030)
    alphaProb.append(.070)
    alphaProb.append(.080)
    alphaProb.append(.020)
    alphaProb.append(.002)
    alphaProb.append(.065)
    alphaProb.append(.060)
    alphaProb.append(.090)
    alphaProb.append(.030)
    alphaProb.append(.010)
    alphaProb.append(.015)
    alphaProb.append(.005)
    alphaProb.append(.020)
    alphaProb.append(.002)

    return alphaProb

def cipherFreq(cipherText):

    alpha = arrayCreate()
    alphA = arrayCreate()
    cipherFreq = arrayCreate()
    
    for j in cipherText:
        if ord(j)<97:
            chrVal=ord(j)-65
            alphA[chrVal]=   alphA[chrVal]+1
        else:
            chrVal=ord(j)-97
            alpha[chrVal]=   alpha[chrVal]+1

    for i in range(26):
        cipherFreq[i] = alpha[i] + alphA[i]

    return cipherFreq

def Phi(cipherFreq,alphaProb):
    array = [0,0]
    Phi = 0

    I = 0
    
    while I<26:
        Phi = 0
        for k in range(26):
            #iob on alphaProb
            Phi = Phi + cipherFreq[k]*alphaProb[k-I]
        if Phi > array[0]:
            array[0] = Phi
            array[1] = I
        I+=1
    return array

def decode(cipherText,key):
    decodeArray = []
    for i in cipherText:
        if ord(i)<97:
            x = ((ord(i)-65-key)+26)%26
            decodeArray.append(x+65)
        else:
            X = ((ord(i)-97-key)+26)%26
            decodeArray.append(X+97)
        

    return decodeArray
'''
def cycleAlpha(offset):
    for i in range(offset):
        
    #print for testing
    #different case testing
    '''
'''
    for k in range(26):
        x=k+97
        print chr(x)+": ",alpha[k],"\n"
    for k in range(26):
        y=k+65
        print chr(y)+": ",alphA[k],"\n"

    #frequency array testing
    for k in range(26):
        print "Number of ",chr(65+k),chr(97+k),": ",alphaFreq[k]

    #probability array testing
    for k in range(26):
        print "Probability of ",chr(65+k),chr(97+k),": ",alphaProb[k]
        
    print "Phi = ",oldPhi
    '''
    
main()
