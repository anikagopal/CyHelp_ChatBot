{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww18800\viewh11200\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #CyHelp Starter Code\
cybersecurtiyBirthYear = 1970\
\
#Greets user\
print("Hello! I'm CyHelp.")\
userName = input("What's your name?\\n")\
print("Nice to meet you " + userName)\
#Recounts start of Cybersecurity\
todayYear = input("What year is it?\\n")\
timePased = int(todayYear) - cybersecurtiyBirthYear\
print("Wow! That means it has been " + str(timePased) + " years sine Cybersecurity began!")\
\
\
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")\
input("Press enter to continue.\\n")\
\
\
#Describes Cybersecurity\
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")\
print("These people can be government, nations, companies, community organizations, and individuals.\\n")\
\
#Introduces CIA Triad\
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, avaliability.")\
print("Would you like to learn about the CIA Triad?")\
giveInfo = input("Type 'yes' or 'no'\\n")\
\
\
#Explains pillars of CIA Triad\
while giveInfo == "yes":\
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \\n(a) confidentiality, (b) integrity, (c)     avaliability, (d) none")\
  topic = input()\
  \
  if topic.lower() == "a": \
    print("Confidentiality makes sure data is private.")\
  \
  elif topic.lower() == "b":\
    print("Integrity makes sure that data has not been tampered with and can be trusted.")\
  \
  elif topic.lower() == "c":\
      print("Avalibility makes sure authorized people can access the data.")\
  \
  elif topic.lower() == "d":\
      print("Okay.")\
      break \
  \
  else: \
    print("Sorry, I didn't catch that. Choose one of the options listed.")\
  \
#Chatbot ends conversation\
print("Thanks for chatting with me, and I hope you learned something new!")}