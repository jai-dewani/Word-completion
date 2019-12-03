class Node:
        def __init__(self,value):
                self.value = value
                self.next = {}
                self.freq = 0
                self.end = False
                for i in range(97,123):
                        self.next[chr(i)] = None

        def __repr__(self):
                return str(self.value)

def inorder(root):
        print(root)
        for i in range(97,123):
                if root.next[chr(i)]!=None:
                        inorder(root.next[chr(i)])

def guessfun(node,word,words):
        word = word+str(node.value)
        next = False
        if node.end:
                words.append([node.freq,word])
        for i in range(97,123):
                if node.next[chr(i)]!=None:
                        next = True
                        guessfun(node.next[chr(i)],word,words)
        
def guess(root,word):
        words = []
        guessfun(root,word,words)
        #print(words)
        words.sort(reverse=True)
        #print(words)
        for i in range(min(10,len(words))):
                print(words[i][1]+'\t'+str(words[i][0]))

def createTree():
        print("Creting tree")
        file = open('unigram_freq.csv')
        text = file.read().split('\n')
        text.pop()
        text.pop(0)
        for i in range(len(text)):
                text[i] = text[i].split(',')
        print(len(text))
        text = text[:100000]
        t = len(text)
        # print(t)
        for tr in range(t):
                string = text[tr][0]
                current = Root
                for i in range(len(string)):
                        if current.next[string[i]]==None:
                                newNode = Node(string[i])
                                current.next[string[i]] = newNode
                                current = current.next[string[i]]          
                        else:
                                current = current.next[string[i]]
                current.freq = int(text[tr][1])
                current.end = True
        file.close()
        print('Done.')

Root = Node(0)
text = ''
createTree()
print("Enter exit() to end program.")
while(True):
        # Root = loadPickle()
        
        print('Enter part word and then press enter for word suggestions')
        word = list(input())
        if word=="exit()":
                break
        current = Root
        for i in range(len(word)):
                #print(word[i],current,current.next)
                current = current.next[word[i]] 
        print('TOP 10 GUESSES')
        word = ''.join(x for x in word)
        word = word[:-1]
        guess(current,''.join(x for x in word))

