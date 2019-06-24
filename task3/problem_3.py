"""
    HUFFMAN CODING AND DECODING:
    
    Take a string and determine the relevant frequencies of the characters.
    Build and sort a list of tuples from lowest to highest frequencies.
    Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
    Trim the Huffman Tree (remove the frequencies from the previously built tree).
    Encode the text into its compressed form.
    Decode the text from its compressed form.
"""
import sys

codes = {}

def acceptedChar(ch):
    if ord(ch) >= 32 and ord(ch) <= 126:
        return True
    return False

def frequency(data):
    freq = {}
    if data == None:
        return freq
    for ch in data:
        if acceptedChar(ch):
            if freq.get(ch) is None:
                freq[ch]=1
            else:
                freq[ch] += 1
        else:
            print("Invalid character!!")
            return {}
    return freq

def sortFrequency(freq) :
    keys = freq.keys()
    keyVal = []
    for val in keys :
        keyVal.append((freq[val],val))
    keyVal.sort()
    return keyVal

def buildHuffman(keyVals) :
    while len(keyVals) != 1 :
        loVal = keyVals[0]
        nextLoVal = keyVals[1]
        theRest  = keyVals[2:]
        combFreq = loVal[0] + nextLoVal[0]
        keyVals   = theRest + [(combFreq,(loVal,nextLoVal))]
        keyVals.sort(key=lambda t: t[0])
    return keyVals[0] 

def trimHuffman(tree) :
    p = tree[1]
    if type(p) == type("") :
        return p
    else :
        return (trimHuffman(p[0]), trimHuffman(p[1]))

def setCodes(node,val='') :
    global codes
    if type(node) == type("") :
        codes[node] = val
    else  : 
        setCodes(node[0], val+"0")
        setCodes(node[1], val+"1") 

def huffman_encoding(data) :
    if data == "" or data == None:
        return None, None
    global codes
    freqs = frequency(data)
    if len(freqs) == 0: return None
    tuples = sortFrequency(freqs)
    tree = buildHuffman(tuples)
    tree = trimHuffman(tree)
    setCodes(tree)
    output = ""
    for ch in data :
        output += codes[ch]
    return output, tree

def huffman_decoding(data,tree) :
    if data == "" or data == None:
        return None
    output = ""
    node = tree
    for bit in data :
        if bit == '0' :
            node = node[0]
        else          :
            node = node[1]
        if type(node) == type("") :
            output += node
            node = tree
    return output

if __name__ == "__main__":

    """
    TEST CASE 1
    """

    a_great_sentence = "The bird is the word"
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    """
    The content of the data is: The bird is the word

    The content of the encoded data is: 0110000111111001110010101110110001100111010100001111110101110000101110

    The content of the decoded data is: The bird is the word
    """


    """
    TEST CASE 2
    """

    a_great_sentence = ""
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    """
    The content of the data is: 

    The content of the encoded data is: None

    The content of the decoded data is: None
    """


    """
    TEST CASE 3
    """

    a_great_sentence = "This IS CaSe SenSITIve"
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    """
    The content of the data is: This IS CaSe SenSITIve

    The content of the encoded data is: 110100100011010101110011101100000001111101011111101010011110011011001100101

    The content of the decoded data is: This IS CaSe SenSITIve
    """

