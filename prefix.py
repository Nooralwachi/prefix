from collections import defaultdict

def find_prefix(filename):
    pre = ''
    with open(filename, 'r') as fileStream:
        lines=readPrefixFromFileStream(fileStream)
        print(lines)
        pre = lines[0]
        for line in lines[1:]:
            word = line.strip()
            pre = compare(pre, word)
    return pre

def readPrefixFromFileStream(fileStream):
    return fileStream.readlines()
 
def compare(left, right):
    if (len(left) > len(right)):    
        left, right = right, left
    for i in range(len(left)):
        if left[i] != right[i]:
            return left[:i]
    return left

def find_common_prefix(words):
    print(words)
    common  = ''
    outer, inner=[], []
    words = sorted(words)
    letter = words[0][0] 
    for word in words:
        if word[0] == letter:
            inner.append(word)
        else:
            outer.append(inner)
            inner= [word]
            letter= word[0] 
    outer.append(inner)
    for words in outer:
        pre = words[0]
        for word in words[1:]:
            pre = compare(pre, word)
            if len(common)!= len(pre):
                common = pre
            if not pre:
                pre = word
    return common

def find_common_prefix2(words):
    print(words)
    words_dict=defaultdict(int)
    for word in words:
        for i in range(len(word)):
            words_dict[word[0:i+1]] +=1
    words_sorted = sorted(words_dict.items(), key=lambda item:(item[1],len(item[0])), reverse=True)
    return words_sorted[0][0]

print(find_prefix('filex.txt'))

words = ['ax', 'apple', 'book', 'banana'] 
print(find_common_prefix(words))
words = ['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']
print(find_common_prefix(words))

words = ['ax', 'apple', 'book', 'banana']
print(find_common_prefix2(words))
words = ['app', 'apple', 'book', 'banana', 'cook', 'coat','common','compare', 'coated']
print(find_common_prefix2(words))



