import telebot
import schedule
import time
from datetime import datetime

TOKEN = "8658573660:AAGnwmZsK78dE_dhwY19gnDeMcyIUw2npUQ"
CHANNEL_ID = "-1003953285196"
AFF = "https://systeme.io/fr?sa=sa02716169698fba2f8cf46266a4c3f25a594834a3"

bot = telebot.TeleBot(TOKEN)

msg0 = "*Lundi - Perplexity AI*\nLe moteur de recherche IA\n\nRecherche en temps reel\nSources verifiees\n100% Gratuit\n\n[Essayer](https://perplexity.ai)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #PromptIA"
msg1 = "*Mardi - Midjourney*\nGenere des images IA\n\nImages ultra realistes\nFacile a utiliser\n\n[Essayer](https://midjourney.com)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #ImageIA"
msg2 = "*Mercredi - Copy AI*\nRedige du contenu en secondes\n\nPosts reseaux sociaux\nEmails marketing\n\n[Essayer](https://copy.ai)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #Copywriting"
msg3 = "*Jeudi - Suno AI*\nCree de la musique avec lIA\n\nChansons completes\n100% Gratuit\n\n[Essayer](https://suno.com)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #MusiqueIA"
msg4 = "*Vendredi - Notion AI*\nTon assistant de productivite\n\nResume tes documents\nRedige a ta place\n\n[Essayer](https://notion.so)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #Productivite"
msg5 = "*Samedi - Runway ML*\nGenere des videos IA\n\nVideos a partir de texte\nQualite professionnelle\n\n[Essayer](https://runwayml.com)\n[Business en ligne](" + AFF + ")\n\n#OutilsIA #VideoIA"
msg6 = "*Dimanche - Prompt IA*\n\nUtilise ce prompt dans ChatGPT :\nAgis comme un expert marketing. Cree 5 idees de posts Telegram sur les outils IA.\n\n[Business en ligne](" + AFF + ")\n\n#PromptIA #OutilsIA"

messages = [msg0, msg1, msg2, msg3, msg4, msg5, msg6]

def poster_message():
    jour = datetime.now().weekday()
    bot.send_message(CHANNEL_ID, messages[jour], parse_mode="Markdown")
    print("Message envoye")

schedule.every().day.at("09:00").do(poster_message)
print("Bot demarre...")

while True:
    schedule.run_pending()
    time.sleep(60)
