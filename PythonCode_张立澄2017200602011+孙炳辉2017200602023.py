#Created by Zhang Licheng(2017200602011) & Sun Binghui(2017200602023)

import re

#Error detection
try:
    f1=open(r"A_Game_of_Thrones.txt",encoding='utf-8')
    s=f1.readlines()  # s is a list of strings
    f1.seek(0,0)
    f1.close()
except FileNotFoundError:
    print ("File is not found")
    input('Please press ENTER to quit')
except PermissionError:
    print("You don't have permission")
    input('Please press ENTER to quit')

a=range(97,123) #a-z
b=range(65,91) #A-Z
c=range(32,33) #space
d=set(a) | set(b) #union
e=set(d) | set(c) #union

char2=[]
count2=[]

print ("Symbol\tWeight")
for i in e:  # i is int，mapping to ASCII code of each symbol
    count = 0
    for y in s:      
        l=re.findall(chr(i),y)  # Utilize findall function to match each string in the list of strings with chr(i)
        count += len(l)
    count2.append(count)
    char2.append(chr(i))
    print(chr(i),'\t%d'%count)
    
array=list(zip(char2,count2))


# Create tree node
class TreeNode(object):
    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""

# Create node queue function
def createnodeQueue(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q

# Add node to the queue and create priority queue to make sure it is sorted from large to small
def addQueue(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]

# Define sequence
class nodeQueue(object):

    def __init__(self, code):
        self.que = createnodeQueue(code)
        self.size = len(self.que)

    def addNode(self, node):
        self.que = addQueue(self.que, node)
        self.size += 1

    def popNode(self):
        self.size -= 1
        return self.que.pop(0)

# Recieve the frequence of letters and space
def freChar(array):

 return sorted(array, key=lambda x: x[1])

# Create Huffman Tree
def createHuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority + node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()

# Obtain Huffman Table in terms of Huffman Tree
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x + '0')
        head.code += x
        if head.val:
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x + '1')

# Encode string
def TransEncode(string):
    m=0
    global codeDic1
    transcode = ""
    for ch in string:
        if ch in char2:
            transcode += codeDic1[ch]
    return transcode

# Print  200 words per row
def PrintFunction(results):
    n = 200  # print  200 words per row
    for q in range(len(results)):
        print(results[q], end=' ')
        if (q + 1) % n == 0:
            print(' ')

codeDic1 = {}

t = nodeQueue(freChar(array))
tree = createHuffmanTree(t)
HuffmanCodeDic(tree, '')

list1= sorted(codeDic1.items(),key=lambda x:x[0])

print ("\n")
print ("Symbol\tHuffman code")

for head, x in list1:
    print(head,'\t',x)

print('The encoded novel is:')

test='a4 b+;;;'
list3=''.join(s)
PrintFunction(TransEncode(list3))
print(' ')
input('Please press ENTER to quit')
