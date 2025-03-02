#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    #letterCount = len(line) #for some reason this is only counting line 3 for character count count
    letter = len(line)
    for c in letter:
      letterCount = letterCount + 1

    print(letterCount)




  print("Lines:", lineCount) 
  print("Words:", wordCount)
  print("Characters:", letterCount)

 

if __name__ == '__main__':
  main()
