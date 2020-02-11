print("""
Epidemic Journey by KK '23. Board game is for Epidemic Day.
Instructions: to start the game, insert a random letter of your choice into the box below. After, read the directions, and move accordingly. Remember, insert the letter that you land on when your turn starts. Remember to answer the questions that the program asks you, and have fun!
Game pieces: use anything that fits in the squares, make sure it's different than the other players' pieces. 2+ people can play.
""")

def IncorrectAnswer():   
  print("Sorry, that's not correct. don't move any spaces, next person's turn") # this function is called when you get an answer wrong

def CorrectAnswer():
  print("correct! Move ahead one space, go again") # this function is called when you get an answer right

def questions():             
  spaceinsert=(input("Insert the letter on the corresponding space here")) # "space insert" stands for when you land on a space, you enter the letter to receive a question

  if spaceinsert==("a"): 
    fluquestion=int(input("how many suffer from the flu every year? Press 1 for ~10,000-20,000, press 2 for ~1,000,000-3,000,000, press 3 for 9,000,000-50,000,000, or press 4 for 4,000-10,000"))
    if fluquestion==3:
      CorrectAnswer()
    elif fluquestion!=3:
      IncorrectAnswer()
    while fluquestion==3 or fluquestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no")) # each one of these "blocks" broadcast a question about epidemics when a letter is inserted into space insert. All do pretty much the same algorithm, and when a question is answered correct/incorrect, it will ask if the player(s) have reached the end. If yes, the project will stop, and signal that the player won. If no, the game will continue. Every block does the same thing except a different question is shown.
      if areyouattheend==("no"): 
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break


  if spaceinsert==("b"):
    AIDSquestion=int(input("What year was AIDS introduced? Press 1 for 2004, press 2 for 1983, press 3 for 1889, and press 4 for 1902"))
    if AIDSquestion==2:
      CorrectAnswer()
    elif AIDSquestion!=2:
      IncorrectAnswer()
    while AIDSquestion==3 or AIDSquestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break


  if spaceinsert==("c"):
    Ebola=int(input("Where did Ebola come from? Press 1 for the Democratic Republic of Congo, Press 2 for Nigeria, Press 3 for Argentina, or press 4 for China"))
    if Ebola==1:
      CorrectAnswer()
    elif Ebola!=1:
      IncorrectAnswer()
    while Ebola==3 or Ebola!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break



  if spaceinsert==("d"):
    CancerDeaths=int(input("Which cancer causes the most deaths? Press 1 for breast cancer, press 2 for lung cancer, press 3 for brain cancer, or press 4 for colon cancer"))
    if CancerDeaths==2:
      CorrectAnswer()
    elif CancerDeaths!=2:
      IncorrectAnswer()
    while CancerDeaths==3 or CancerDeaths!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break


  if spaceinsert==("e"):
    ALSquestion=int(input("What disease prevents you from walking? Press 1 for cancer, press 2 for ALS, press 3 for zika, or press 4 for diabetes"))
    if ALSquestion==2:
      CorrectAnswer()
    elif ALSquestion!=2:
      IncorrectAnswer()
    while ALSquestion==3 or ALSquestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("f"):
    diabetesquestion=int(input("What is the most common way to get type-two diabetes? Press 1 for having blood clots, press 2 for through intercourse, press 3 for through exchange of blood, or press 4 for being not physically active and/or obese"))
    if diabetesquestion==4:
        CorrectAnswer()
    elif diabetesquestion!=4:
      IncorrectAnswer()
    while diabetesquestion==3 or diabetesquestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("g"):
    HepCquestion=int(input("What is a way to get Hepatatitis C? Press 1 for sharing food, press 2 for spreading blood, press 3 for being obese, or press 4 for stubbing your toe"))
    if HepCquestion==2:
        CorrectAnswer()
    elif HepCquestion!=2:
      IncorrectAnswer()
    while HepCquestion==3 or HepCquestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("h"):
    AutismQuestion=int(input("What is the probability of being born with autism? Press 1 for 1 in 254, press 2 for 1 in 59, press 3 for 1 in 324, or press 4 for 1 in 17"))
    if AutismQuestion==2:
      CorrectAnswer()
    elif AutismQuestion!=2:
      IncorrectAnswer()
    while AutismQuestion==3 or AutismQuestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("i"):
    KidneyQuestion=int(input("What is the best way to treat kidney failure? Press 1 for remove both kidneys, press 2 for remove appendix, press 3 for kidney transplant, or press 4 for no cure "))
    if KidneyQuestion==3:
        CorrectAnswer()
    elif KidneyQuestion!=3:
      IncorrectAnswer()
    while KidneyQuestion==3 or KidneyQuestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("j"):
    ColdQuestion=int(input("What is the average amount of colds an adult has every year? Press 1 for 2-3 colds, press 2 for 8-9 colds, press 3 for 4-5 colds, or press 4 for 0-1 colds" ))
    if ColdQuestion==1:
      CorrectAnswer()
    elif ColdQuestion!=1:
      IncorrectAnswer()
    while ColdQuestion==3 or ColdQuestion!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("k"):
    CancerGenetic=int(input("True or false- cancer is a genetic disease. Press 1 for true or press 2 for false." ))
    if CancerGenetic==1:
        CorrectAnswer()
    elif CancerGenetic!=1:
      IncorrectAnswer()
    while CancerGenetic==3 or CancerGenetic!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("l"):
    malaria=int(input("Where does malaria come from? Press 1 for bats, press 2 for rats, press 3 for mosquitoes, or press 4 for lizards"))
    if malaria==3:
        CorrectAnswer()
    elif malaria!=3:
      IncorrectAnswer()
    while malaria==3 or malaria!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("m"):
    smallpox=int(input("true or false- smallpox isn't contagious. Press 1 for true or press 2 for false."))
    if smallpox==2:
        CorrectAnswer()
    elif smallpox!=2:
     IncorrectAnswer()
    while smallpox==3 or smallpox!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
       for x in range (1):
          print("congrats you win!")
       break

  if spaceinsert==("n"):
    alzheimers=int(input("What is the average age that alzheimers victims get the disease? Press 1 for 55, press 2 for 65, press 3 for 50, or press 4 for 60"))
    if alzheimers==4:
      CorrectAnswer()
    elif alzheimers!=4:
      IncorrectAnswer()
    while alzheimers==3 or alzheimers!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("o"):
    TB=int(input("Which option is NOT a way to get Tuberculosis? Press 1 for exchange of blood, press 2 for getting sneezed on, or press 3 for getting spit on "))
    if TB==1:
      CorrectAnswer()
    elif TB!=1:
        IncorrectAnswer()
    while TB==3 or TB!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("p"):
    stroke=int(input("Which is a common way to have a stroke? Press 1 for popped blood vessel, press 2 for diabetic nerve pain, or press 3 for brain tumor"))
    if stroke==1:
        CorrectAnswer()
    elif stroke!=1:
        IncorrectAnswer()
    while stroke==3 or stroke!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("q"):
    braincancer=int(input("Which is NOT a type of brain cancer? Press 1 for Astrocytomas, press 2 for Laryngetas, press 3 for Meningiomas, or press 4 for Oligodendrogliomas"))
    if braincancer==2:
      CorrectAnswer()
    elif braincancer!=2:
        IncorrectAnswer()
    while braincancer==3 or braincancer!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("r"):
    whoopingcough=int(input("What is the average duration of whooping cough? Press 1 for 1-2 months, press 2 for 4-6 weeks, press 3 for 1-6 weeks, or press 4 for 6-12 months"))
    if whoopingcough==3:
        CorrectAnswer()
    elif whoopingcough!=3:
          IncorrectAnswer()
    while whoopingcough==3 or whoopingcough!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("s"):
    historyofcancer=int(input("Who named the disease cancer? Press 1 for Dr. Jekyll, press 2 for Socrates, press 3 for Confucious, or press 4 for Hippocrates"))
    if historyofcancer==4:
        CorrectAnswer()
    elif historyofcancer!=4:
          IncorrectAnswer()
    while historyofcancer==3 or historyofcancer!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("t"):
    Famouspeoplewithhiv=int(input("Which celebrity/former celebrity did not have AIDS/HIV at one point in their lives? Press 1 for Eazy-E, press 2 for Micheal Jackson, press 3 for Freddy Mercury, or press 4 for Jonathan Van Ness (from Queer Eye) "))
    if Famouspeoplewithhiv==2:
      CorrectAnswer()
    elif Famouspeoplewithhiv!=2:
        IncorrectAnswer()
    while Famouspeoplewithhiv==3 or Famouspeoplewithhiv!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("u"):
    mentalilness=int(input("What is the most common mental illness? press 1 for anxiety disorder, press 2 for eating disorder, press 3 for depression, or press 4 personality disorders  "))
    if mentalilness==1:
        CorrectAnswer()
    elif mentalilness!=1:
        IncorrectAnswer()
    while mentalilness==3 or mentalilness!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("v"):
    highbloodpress=int(input("roughly how many adults have high blood pressure? Press 1 for 75 million, press 2 for 60 million, press 3 for 500 thousand, or press 4 for 75 thousand"))
    if highbloodpress==1:
      CorrectAnswer()
    elif highbloodpress!=1:
          IncorrectAnswer()
    while highbloodpress==3 or highbloodpress!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("w"):
    STDs=int(input("Which is not an STD? press 1 for HPV, press 2 for HGV, press 3 for HIV, or press 3 for Herpes"))
    if STDs==2:
      CorrectAnswer()
    elif STDs!=2:
        IncorrectAnswer()
    while STDs==3 or STDs!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("x"):
    lupus=int(input("True or false? Lupus is contagious. Press 1 for true, press 2 for false."))
    if lupus==2:
      CorrectAnswer()
    elif lupus!=2:
        IncorrectAnswer()
    while lupus==3 or lupus!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("y"):
    dengue=int(input("Which creature carries Dengue fever? Press 1 for tigers, press 2 for spiders, or press 3 for mosquitoes "))
    if dengue==3:
        CorrectAnswer()
    elif dengue!=3:
        IncorrectAnswer()
    while dengue==3 or dengue!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break

  if spaceinsert==("z"):
    gout=int(input("What is gout? Press 1 for a cancer, press 2 for an STD, or press 3 for an arthritis"))
    if gout==3: 
      CorrectAnswer()
    elif gout!=3:
        IncorrectAnswer()
    while gout==3 or gout!=3:
      areyouattheend=(input("have you reached the end yet? type yes or no"))
      if areyouattheend==("no"):
        print("ok, continue.")
        questions()
      if areyouattheend==("yes"): 
        for x in range (1):
          print("congrats you win!")
        break


#Main body of code, this function starts the game up, calling "space insert"
questions()
