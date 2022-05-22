Team1 = 0
Team2 = 0
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
  aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
  aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
  Team1 = Team1 + 100
elif aaa == 0:
  Team1 = Team1
else:
  aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
  Team2 = Team2 + 100
if aa == "200":
  aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
  Team1 = Team1 + 200
elif aab == 0:
  Team1 = Team1
else:
  aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
  Team2 = Team2 + 200
if aa == "300":
  aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
  Team1 = Team1 + 300
elif aac == 0:
  Team1 = Team1
else:
  aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
  Team2 = Team2 + 300
if aa == "400":
  aad = input("What year did the Avengers release? ")
if aad == "2012":
  Team1 = Team1 + 400
elif aad == 0:
  Team1 = Team1
else:
  aada = input("What year did the Avengers release? ")
if aada == "2012":
  Team2 = Team2
if aa == "500":
  aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
  Team1 = Team1 + 500
elif aae == 0:
  Team1 = Team1
else:
  aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
  Team2 = Team2 + 500
if a == "History":
  ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
  aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
  Team1 = Team1 + 100
elif aba == 0:
  Team1 = Team1
else:
  abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
  Team2 = Team2 + 100
if ab == "200":
  abb = input("What year did WWI start? ")
if abb == "1914":
  Team1 = Team1 + 200
elif abb == 0:
  Team1 = Team1
else:
  abba = input("What year did WWI start? ")
if abba == "1914":
  Team2 = Team2 + 200
if ab == "300":
  abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
  Team1 = Team1 + 300
elif abc == 0:
  Team1 = Team1
else:
  abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
  Team2 = Team2 + 300
if ab == "400":
  abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
  Team1 = Team1 + 400
elif abd == 0:
  Team1 = Team1
else:
  abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
  Team2 = Team2 + 400
if ab == "500":
  abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
  Team1 = Team1 + 500
elif abe == 0:
  Team1 = Team1
else:
  abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
  Team2 = Team2 + 500
if a == "Geography":
  ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
  aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
  Team1 = Team1 + 100
elif aca == 0:
  Team1 = Team1
else:
  acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
  Team2 = Team2 + 100
if ac == "200":
  acb = input("What continent is Canada located in? ")
if acb == "North America":
  Team1 = Team1 + 200
elif acb == 0:
  Team1 = Team1
else:
  acba = input("What continent is Canada located in? ")
if acba == "North America":
  Team2 = Team2 + 200
if ac == "300":
  acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
  Team1 = Team1 + 300
elif acc == 0:
  Team1 = Team1
else:
  acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
  Team2 = Team2 + 300
if ac == "400":
  acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
  Team1 = Team1 + 400
elif acd == 0:
  Team1 = Team1
else:
  acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
  Team2 = Team2 + 400
if ac == "500":
  ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
  Team1 = Team1 + 500
elif ace == 0:
  Team1 = Team1
else:
  acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
  Team2 = Team2 + 500
if a == "Science":
  ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
 ada = input("How many planets are there? ")
if ada == "8":
  Team1 = Team1 + 100
elif ada == 0:
  Team1 = Team1
else:
  adaa = input("How many planets are there? ")
if adaa == "8":
  Team2 = Team2 + 100
if ad == "200":
  adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
  Team1 = Team1 + 200
elif adb == 0:
  Team1 = Team1
else:
  adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
  Team2 = Team2 + 200
if ad == "300":
  adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
  Team1 = Team1 + 300
elif adc == 0:
  Team1 = Team1
else:
  adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
  Team2 = Team2 + 300
if ad == "400":
  add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
  Team1 = Team1 + 400
elif add == 0:
  Team1 = Team1
else:
  adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
  Team2 = Team2 + 400
if ad == "500":
  ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
  Team1 = Team1 + 500
elif ade == 0:
  Team1 = Team1
else:
  adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
  Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500

a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team1 = Team1 + 100
elif aaa == 0:
 Team1 = Team1
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team2 = Team2 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team1 = Team1 + 200
elif aab == 0:
 Team1 = Team1
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team2 = Team2 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team1 = Team1 + 300
elif aac == 0:
 Team1 = Team1
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team2 = Team2 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team1 = Team1 + 400
elif aad == 0:
 Team1 = Team1
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team2 = Team2
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team1 = Team1 + 500
elif aae == 0:
 Team1 = Team1
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team2 = Team2 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team1 = Team1 + 100
elif aba == 0:
 Team1 = Team1
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team2 = Team2 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team1 = Team1 + 200
elif abb == 0:
 Team1 = Team1
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team2 = Team2 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team1 = Team1 + 300
elif abc == 0:
 Team1 = Team1
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team2 = Team2 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team1 = Team1 + 400
elif abd == 0:
 Team1 = Team1
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team2 = Team2 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team1 = Team1 + 500
elif abe == 0:
 Team1 = Team1
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team2 = Team2 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team1 = Team1 + 100
elif aca == 0:
 Team1 = Team1
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team2 = Team2 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team1 = Team1 + 200
elif acb == 0:
 Team1 = Team1
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team2 = Team2 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team1 = Team1 + 300
elif acc == 0:
 Team1 = Team1
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team2 = Team2 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team1 = Team1 + 400
elif acd == 0:
 Team1 = Team1
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team2 = Team2 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team1 = Team1 + 500
elif ace == 0:
 Team1 = Team1
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team2 = Team2 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team1 = Team1 + 100
elif ada == 0:
 Team1 = Team1
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team2 = Team2 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team1 = Team1 + 200
elif adb == 0:
 Team1 = Team1
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team2 = Team2 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
elif adc == 0:
 Team1 = Team1
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team1 = Team1 + 400
elif add == 0:
 Team1 = Team1
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team2 = Team2 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team1 = Team1 + 500
elif ade == 0:
 Team1 = Team1
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team2 = Team2 + 500
a = input("Choose a category: Movie Trivia, History, Geography, Science ")
aa = 0
aaa = 0
aaaa = 0
aab = 0
aaba = 0
aac = 0
aaca = 0
aad = 0
aada = 0
aae = 0
aaea = 0
ab = 0
aba = 0
abaa = 0
abb = 0
abba = 0
abc = 0
abca = 0
abd = 0
abda = 0
abe = 0
abea = 0
ac = 0
aca = 0
acaa = 0
acb = 0
acba = 0
acc = 0
acca = 0
acd = 0
acda = 0
ace = 0
acea = 0
ad = 0
ada = 0
adaa = 0
adb = 0
adba = 0
adc = 0
adca = 0
add = 0
adda = 0
ade = 0
adea = 0
if a == "Movie Trivia":
 aa = input("What difficulty: 100, 200, 300, 400, 500")
if aa == "100":
 aaa = input("How many Star Wars films are there?  ")
if aaa == "9":
 Team2 = Team2 + 100
elif aaa == 0:
 Team2 = Team2
else:
 aaaa = input("How many Star Wars films are there?  ")
if aaaa == "9":
 Team1 = Team1 + 100
if aa == "200":
 aab = input("Who played Harry Potter? ")
if aab == "Daniel Radcliffe":
 Team2 = Team2 + 200
elif aab == 0:
 Team2 = Team2
else:
 aaba = input("Who played Harry Potter? ")
if aaba == "Daniel Radcliffe":
 Team1 = Team1 + 200
if aa == "300":
 aac = input("Who played John Wick? ")
if aac == "Keanu Reeves":
 Team2 = Team2 + 300
elif aac == 0:
 Team2 = Team2
else:
 aaca = input("Who played John Wick? ")
if aaca == "Keanu Reeves":
 Team1 = Team1 + 300
if aa == "400":
 aad = input("What year did the Avengers release? ")
if aad == "2012":
 Team2 = Team2 + 400
elif aad == 0:
 Team2 = Team2
else:
 aada = input("What year did the Avengers release? ")
if aada == "2012":
 Team1 = Team1
if aa == "500":
 aae = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aae == "Thomas Anderson":
 Team2 = Team2 + 500
elif aae == 0:
 Team2 = Team2
else:
 aaea = input("What is the full name of Neo in the Matrix quadriliogy? ")
if aaea == "Thomas Anderson":
 Team1 = Team1 + 500
if a == "History":
 ab = input("What difficulty: 100, 200, 300, 400, 500")
if ab == "100":
 aba = input("Who was the leader of the nazi party during WWII? ")
if aba == "Adolf Hitler":
 Team2 = Team2 + 100
elif aba == 0:
 Team2 = Team2
else:
 abaa = input("Who was the leader of the nazi party during WWII? ")
if abaa == "Adolf Hitler":
 Team1 = Team1 + 100
if ab == "200":
 abb = input("What year did WWI start? ")
if abb == "1914":
 Team2 = Team2 + 200
elif abb == 0:
 Team2 = Team2
else:
 abba = input("What year did WWI start? ")
if abba == "1914":
 Team1 = Team1 + 200
if ab == "300":
 abc = input("Who is the first president of the USA? ")
if abc == "George Washington":
 Team2 = Team2 + 300
elif abc == 0:
 Team2 = Team2
else:
 abca = input("Who is the first president of the USA? ")
if abca == "George Washington":
 Team1 = Team1 + 300
if ab == "400":
 abd = input("What day was the Czech Republic born? ")
if abd == "1. 1. 1993":
 Team2 = Team2 + 400
elif abd == 0:
 Team2 = Team2
else:
 abda = input("What day was the Czech Republic born? ")
if abda == "1. 1. 1993":
 Team1 = Team1 + 400
if ab == "500":
 abe = input("Who was the third ruler of the USSR? ")
if abe == "Khrushchev":
 Team2 = Team2 + 500
elif abe == 0:
 Team2 = Team2
else:
 abea = input("Who was the third ruler of thr USSR? ")
if abea == "Khrushchev":
 Team1 = Team1 + 500
if a == "Geography":
 ac = input("Choose a difficulty: 100, 200, 300, 400, 500")
if ac == "100":
 aca = input("What continent is the Czech Republic located in? ")
if aca == "Europe":
 Team2 = Team2 + 100
elif aca == 0:
 Team2 = Team2
else:
 acaa = input("What continent is the Czech Republic located in? ")
if acaa == "Europe":
 Team1 = Team1 + 100
if ac == "200":
 acb = input("What continent is Canada located in? ")
if acb == "North America":
 Team2 = Team2 + 200
elif acb == 0:
 Team2 = Team2
else:
 acba = input("What continent is Canada located in? ")
if acba == "North America":
 Team1 = Team1 + 200
if ac == "300":
 acc = input("What is the capital city of Germany? ")
if acc == "Berlin":
 Team2 = Team2 + 300
elif acc == 0:
 Team2 = Team2
else:
 acca = input("What is the capital city of Germany? ")
if acca == "Berlin":
 Team1 = Team1 + 300
if ac == "400":
 acd = input("What is the capital city of Iceland? ")
if acd == "Rejkavik":
 Team2 = Team2 + 400
elif acd == 0:
 Team2 = Team2
else:
 acda = input("What is the capital city of Iceland? ")
if acda == "Rejkavik":
 Team1 = Team1 + 400
if ac == "500":
 ace = input("What is the capital city of Greenland? ")
if ace == "Nuuk":
 Team2 = Team2 + 500
elif ace == 0:
 Team2 = Team2
else:
 acea = input("What is the capital city of Greenland? ")
if acea == "Nuuk":
 Team1 = Team1 + 500
if a == "Science":
 ad = input("Choose a dificulty 100, 200, 300, 400, 500")
if ad == "100":
  ada = input("How many planets are there? ")
if ada == "8":
 Team2 = Team2 + 100
elif ada == 0:
 Team2 = Team2
else:
 adaa = input("How many planets are there? ")
if adaa == "8":
 Team1 = Team1 + 100
if ad == "200":
 adb = input("The process of turning sunlight into glucose is called what? ")
if adb == "Photosynthesis":
 Team2 = Team2 + 200
elif adb == 0:
 Team2 = Team2
else:
 adba = input("The process of turning sunlight into glucose is called what? ")
if adba == "Photosynthesis":
 Team1 = Team1 + 200
if ad == "300":
 adc = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team2 = Team2 + 300
elif adc == 0:
 Team2 = Team2
else:
 adca = input("What is the formula for force? ")
if adc == "Mass x acceleration":
 Team1 = Team1 + 300
if ad == "400":
 add = input("What is the scientific name for planets out of the Solar System? ")
if add == "Exoplanets":
 Team2 = Team2 + 400
elif add == 0:
 Team2 = Team2
else:
 adda = input("What is the scientific name for planets out of the Solar System? ")
if adda == "Exoplanets":
 Team1 = Team1 + 400
if ad == "500":
 ade = input("What is the chemical composition of table salt? ")
if ade == "NaCl":
 Team2 = Team2 + 500
elif ade == 0:
 Team2 = Team2
else:
 adea = input("What is the chemical composition of table salt? ")
if adea == "NaCl":
 Team1 = Team1 + 500



print("Team 1's score is:")
print(Team1)

print("Team 2's score is:")
print(Team2)