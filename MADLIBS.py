import time
import random
# title
print("Welcome To Liam's MADLIBS\n")
time.sleep(1)
print("please enter the requested words.\n")
time.sleep(1)
#questions
quest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(quest)
 # print(quest)
i = -1
while i <= 9:
  i += 1
  if i == 10:
   quest.append(str(11))
  if quest[i] == 1:
   person1 = input("Enter a person: ")
  elif quest[i] == 2:
   noun1 = input("Enter a noun: ")
  elif quest[i] == 3:
   noun2 = input("Enter a noun: ")
  elif quest[i] == 4:
   verb1 = input("Enter a verb (past): ")
  elif quest[i] == 5:
   verb2 = input("Enter a verb (present): ")
  elif  quest[i] == 6:
   inf = input("Enter an Infinitive: ")
  elif quest[i] == 7:
   adj1 = input("Enter an adjective: ")
  elif quest[i] == 8:
    adj2 = input("Enter an adjective: ")
  elif quest[i] == 9:
    adv1 = input("Enter an adverb: ")
  elif quest[i] == 10:
    place1 = input("Enter a place: ")
  else:
    break
  print("\n")



#arrays
MLnouns = []
MLverbs = []
MLadv = []
MLadj = []
ML = [MLnouns, MLverbs, MLadv, MLadj]
MLnouns.extend([noun1, noun2, person1, place1])
MLverbs.extend([verb1, verb2, inf])
MLadv.append(adv1)
MLadj.extend([adj1, adj2])
#final madlibs
print("the " + ML[3][0] + " " + ML[0][0] + " wanted " + ML[1][2] + " the cake. Then the " + ML[3][1] + " " + ML[0][1] + " decided it was a good idea to " + ML[1][1] + " " + ML[2][0] + " while in " + ML[0][3] + "." )