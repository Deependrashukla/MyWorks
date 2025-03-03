import requests


#Accessing the body content of website
def body(data):
    
    data = data[data.find('<body'):data.find('</body>')]
    data = data_cleaning(data)
    body_content = ""
    tag_open = False
    for i in data: 
        if i == "<":
            tag_open = True
        elif i == ">":
            tag_open = False
        elif not tag_open:
            body_content = body_content + i
    body_content = body_content.split()
    body = ''
    for i in body_content:
        body = body + " " + i

    return body


def data_cleaning(data):
    for i in range (data.count("<script")):
        data = data[:data.find('<script')] + data[data.find('</script')+9:]

    for i in range (data.count("<style")):
        data = data[:data.find('<style')] + data[data.find('</style')+8:]
    
    return (data)


def is_alphanumeric(word):
    for char in word :
        if (char.isalnum() or char == "'" or char == ","):
            continue
        else:
            return False
    return True


def ngram_converter(body, n = 5):
    dict = {}
    body = body.split()
    for word in body:
        if not is_alphanumeric(word):
            body.remove(word)
            
    for i in range(len(body) - n +1):
        ngram_word = " ".join(body[i : i+n]).lower()
        if ngram_word not in dict.keys():
            dict[ngram_word] = 1
        else:
            dict[ngram_word] += 1
    return dict


#Hash Converter
def hash_bit_converter(word, p=53):
    asci_sum = 0
    for i in range(len(word)):
        asci_sum += ord(word[i])*p**i
    hash_value = asci_sum % (2**64)
    return format(hash(hash_value) & (2**64-1), '064b')

def freq_adder(bin_num, freq):
    num = []
    for i in bin_num:
        if int(i) == 1:
            num.append(freq)
        else:
            num.append(-freq)
    return num

def simhash(body):
    word_count = ngram_converter(body)
    doc_vector = [0 for i in range(64)]
    for word in word_count.keys():
        hash_bit = hash_bit_converter(word)
        hash_vector = freq_adder(hash_bit, word_count[word])
        doc_vector = [doc_vector[j] + hash_vector[j] for j in range(64)]
                
    simhash_value = ""
    for i in doc_vector:
        if i >= 0:
            simhash_value += "1"
        else:
            simhash_value += "0"
    return simhash_value

def main():
    URL1 = input("Enter 1st document's URL: ")
    URL2 = input("Enter 2nd document's URL: ")
    response1 = requests.get(URL1).text
    response2 = requests.get(URL2).text
    body_content1 = body(response1)
    body_content2 = body(response2)
    t1 = simhash(body_content1)
    t2 = simhash(body_content2)
    count = 0
    for i in range(64):
        if t1[i] == t2[i]:
            count += 1 
    print(f"Number of bits simmilar in both documents are: {count}")


#----------------------Main-----------
if __name__ == '__main__':
    main()
    
    