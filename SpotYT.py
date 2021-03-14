'''
project in which a telegram Bot is creared which
directly download the songs from Spotify track
link or YouTube Video link into .mp3 format
A project by hkonvict
'''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os 


def start(update, context):
  if os.path.isfile('key.hk'):
    update.message.reply_text('Welcome Back Again!!\nSend URL')
  else:
    update.message.reply_text('Hello Listener!!')
    update.message.reply_text('Enter the access Password')


def help(update, context):
    update.message.reply_text('Reply me with any YouTube video or Spotify track url and Get the mp3 directly!!')
    
def start_download(update , context):
  
  if os.path.isfile('key.hk'):
 
    initial_count = len([name for name in os.listdir('.') if os.path.isfile(name)])
    url = update.message.text
    print(url)

    command_cli = "spotdl --song " + url + " -f ."
    os.system(command_cli)
    final_count = len([name for name in os.listdir('.') if os.path.isfile(name)])
    if final_count!=initial_count:
      update.message.reply_text("Great!! Got the song. \nCheck the Folder!")
    else:
      update.message.reply_text("INVALID URL!!\nGreat to see you can text me random things. \nNow Send me YouTube video or Spotify track url.")
      
     
  else:
    #make sure to add your password
    password = "featzai"
    if update.message.text == password:
      os.system('echo YouAreIn > key.hk')
      update.message.reply_text('Great!! You are logged in.\nNow Start Sending the URL')
    else:
      update.message.reply_text('This is aint the Correct Password.\nYou must login first to use the Bot.\nTry Again')
      

def main():
    """Start the bot."""
    #Make sure to add the token of your bot
    updater = Updater("1596190609:AAGa61q2Qx2sktVbjnRyjyxnyVHzf8VQIGg", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler(CommandHandler("help", help))
    
    dp.add_handler(MessageHandler(Filters.text, start_download))

    updater.start_polling()
    
    updater.idle()


if __name__ == '__main__':
    main()
