#!/bin/python3


import time
import random
import re
import json
import urllib.request


def get_cat_fact():
  url = 'https://meowfacts.herokuapp.com/'
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  cat_facts = result["data"]
  cat_fact = cat_facts[0]
  return cat_fact


patterns = {
"postNL(.*)"         :"Een link naar je Track & Trace vind je in 'Mijn Coolblue', je verzendbevestiging en de website en app van PostNL. Je ontvangt de verzendbevestiging via e-mail, één dag voordat je pakketje wordt bezorgd. Hiermee kun je precies zien wanneer je pakket aankomt."
"CoolblueBezorgt(.*)":"Als je pakket via CoolblueBezorgt wordt bezorgd, vind je een link naar je Track & Trace in 'Mijn Coolblue', de verzendbevestiging en de e-mail met het tijdvak van 1 uur die je de nacht voor de levering ontvangt. Hiermee kun je precies zien wanneer je pakket aankomt."
"CoolblueFietst(.*)" :"Als je pakket via CoolblueFietst wordt bezorgd, vind je een link naar je Track & Trace in Mijn Coolblue, de verzendbevestiging en de e-mail met het tijdvak van 1 uur die je de nacht voor de levering ontvangt. Hiermee kun je precies zien wanneer je pakket aankomt."
"kat"                :get_cat_fact()
}


responses = {
"Hoe kan ik een pakket terugsturen?"                    :"Dit kunt u doen door uw retour aan te melden via het online retourformulier. U pakt uw retourpakket weer in en binnen éen uur ontvangt u een mail met de bevestiging en de verzendlabel. Nu kunt u uw pakket naar de lokale postnl-punt brengen.",
"Mijn geld is niet teruggestort. Wat moet ik nu doen?"  :"Hoeveel dagen zit u al te wachten sinds u uw paket heeft geretouneerd? Als het meer dan 5 werkdagen is moet u contact opnemen met de service balie.",
"Hoe wijzig ik mijn bestelling?"                        :"U kunt uw bestelling alleen wijzigen als u nog geen verzendbewijs heeft gekregen. Neem contact op met onze klantenservice om de naam of het adres van je bestelling aan te passen.",
"Hoe annuleer ik mijn bestelling?"                      :"Als u naar mijn bestellingen gaat in mijn Coolblue dan kunt u daar uw besteling annuleren.",
"Is mijn product op voorraad?"                          :"Dit kun je zien op de productpagina, onder de prijs van het product. Hier vind je altijd de meest actuele voorraadstatus van het product, online en in onze winkels."
"Hoe weet ik wanneer mijn bestelling aankomt?"          :"Wordt je pakket bezorgd via PostNL, CoolblueBezorgt of CoolblueFietst? Dan kan ik je verder helpen met de juiste informatie."




}




 
 
def get_response(message):
  responses["kat"] = get_cat_fact()
  if message == "kat":
    return get_cat_fact()
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
   time.sleep(random.randint(0,1,2,3))
   print(get_response(message))


while True:
   construct_dialogue()
   

