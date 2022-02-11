def populateDictionary():
  with open("store.txt", "r") as f:
    for line in f:
      kv = line[:-1].split(':')
      globalDict[kv[0]] = kv[1]

globalDict = {}
populateDictionary()
while True:
  cmd = input("Enter R to read a value, A to add a new value or Q to quit: ")

  if cmd not in ['R', 'A', 'Q']:
    print("Not a valid command!")
  elif cmd == 'Q':
    break
  elif cmd == 'R':
    word = input("Enter the word you want to lookup (all lowercase): ")
    if word in globalDict:
      print(word + ": " + globalDict[word])
    else:
      print("This word isn't in the dictionary!")
  else:
    word = input("Enter the word you want to define (all lowercase): ")
    if word in globalDict:
      print("This word is already defined!")
    else:
      definition = input("What is the definition of this word? ")
      globalDict[word] = definition

      s = word + ":" + definition + "\n"

      with open("store.txt", "a") as f:
        f.write(s)
        f.close()
  print('-------------------------------------')