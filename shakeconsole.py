
from textindex import textindex
import os


def lookupWords(index,filename):
  "All user to lookup word matches"
  searchTerm=input("\nEnter word to look up, return to end: ")

  while searchTerm !="":
    positions=index.lookup(searchTerm)
    if len(positions)>0:
      textfile=open(filename,"r")
      for pos in positions:
        textfile.seek(pos,0)
        line=textfile.readline()
        print(line.strip())
    else:
      print(searchTerm,"not found,")
    searchTerm=input("\nEnter word to look up, return to end: ")

def printLines(book,lines):
  for line in lines:
    print(book[line])

file="Shakespeare.txt"
wordIndex=textindex(file)
print("Total words:",wordIndex.wordcount())
lookupWords(wordIndex,file)
