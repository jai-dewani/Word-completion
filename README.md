# Word-completion
A system which takes a part of a word and returns set of possible words.  
It speeds up the process by using a [Trie data structure](https://en.wikipedia.org/wiki/Trie) insted of linerarly searching though a huge list of words.  
## How it works
What a Trie is a tree where every node contains single letters.  
In this case, every word is broken and inserted letter by letter in this special tree.  
How this speeds up the process is that we go down the tree letter by letter and adding up the letters in the way, when you reach the leaf node you have a complete word with you.  
![Image of Trie](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/250px-Trie_example.svg.png?sanitize=true)

Read more about Tries [here](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014) and [here](https://www.geeksforgeeks.org/trie-insert-and-search/)
