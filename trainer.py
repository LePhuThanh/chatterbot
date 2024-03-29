from chatterbot import languages, ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from chatterbot.comparisons import levenshtein_distance, my_bert

chatbot = ChatBot("chatbot",
                  read_only=True,
                  preprocessors=[
                      'chatterbot.preprocessors.clean_whitespace'
                  ],
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                      }
                  ],
                  statement_comparison_function=levenshtein_distance,
                  response_selection_method=get_random_response,
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  tagger_language=languages.VIE,
                  database_uri='sqlite:///database.sqlite3'
                  )

if __name__ == "__main__":

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('./data/train/')
