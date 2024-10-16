#!/bin/python3

import time
import random
import re

patterns = {

}

responses = { 
"Hoe kan ik een pakket terugsturen?"                    :"Dit kunt u doen door uw retour aan te melden via het online retourformulier. U pakt uw retourpakket weer in en binnen éen uur ontvangt u een mail met de bevestiging en de verzendlabel. Nu kunt u uw pakket naar de lokale postnl-punt brengen.",
"Mijn geld is niet teruggestort. Wat moet ik nu doen?"  :"Hoeveel dagen zit u al te wachten sinds u uw paket heeft geretouneerd? Als het meer dan 5 werkdagen is moet u contact opnemen met de service balie.",
"Hoe wijzig ik mijn bestelling?"                        :"U kunt uw bestelling alleen wijzigen als u nog geen verzendbewijs heeft gekregen. Neem contact op met onze klantenservice om de naam of het adres van je bestelling aan te passen.",
"Hoe annuleer ik mijn bestelling?"                      :"Als u naar mijn bestellingen gaat in mijn Coolblue dan kunt u daar uw besteling annuleren.",
"Is mijn product op"
""


}


  
  
def get_response(message): 
  for pattern in patterns:
    match = re.search(pattern,message)
    if match:
      computer_message = random.choice(patterns[pattern])
      user_answer = match.group(1)
      return computer_message.format(user_answer)
  
  if message in responses: 
      return random.choice(responses[message])
      
  else: 
    return "Ik snap niet wat je bedoelt, dit zei je: " + message 



def construct_dialogue():
   message = input("YOU: ")
   time.sleep(random.randint(0,1))
   print(get_response(message))

while True: 
   construct_dialogue()
   