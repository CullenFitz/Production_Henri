#Trains Henri using some specified training file 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

train = os.path.join(THIS_FOLDER, 'SmallTalk.yml')

Henri = ChatBot('Henri')

trainer = ChatterBotCorpusTrainer(Henri, show_training_progress=True)


trainer.train(
    train
)
