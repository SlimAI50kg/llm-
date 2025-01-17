{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 class MoodBot:\
    """\
    MoodBot: A small AI to analyze the sentiment of messages and respond.\
    """\
\
    def __init__(self, name="MoodBot"):\
        self.name = name\
        print(f"[INFO] \{self.name\} is ready to chat!")\
\
    def analyze_sentiment(self, message):\
        """\
        Analyze the sentiment of the message using simple rules.\
        :param message: The input message from the user.\
        :return: Sentiment category ('positive', 'negative', or 'neutral').\
        """\
        positive_words = ['happy', 'great', 'good', 'love', 'excellent', 'awesome']\
        negative_words = ['sad', 'bad', 'angry', 'terrible', 'hate', 'awful']\
\
        message_lower = message.lower()\
        if any(word in message_lower for word in positive_words):\
            return 'positive'\
        elif any(word in message_lower for word in negative_words):\
            return 'negative'\
        else:\
            return 'neutral'\
\
    def respond(self, message):\
        """\
        Generate a response based on the sentiment.\
        :param message: The input message from the user.\
        :return: Response message.\
        """\
        sentiment = self.analyze_sentiment(message)\
\
        if sentiment == 'positive':\
            return "I'm so glad to hear that! Keep up the positivity!"\
        elif sentiment == 'negative':\
            return "I'm sorry you're feeling that way. Remember, it's okay to have tough days."\
        else:\
            return "Thanks for sharing. I'm here if you want to talk more!"\
\
    def chat(self):\
        """\
        Start a chat loop where the bot interacts with the user.\
        """\
        print("[MoodBot] Hello! Tell me how you're feeling today. Type 'exit' to end the chat.")\
        while True:\
            user_input = input("You: ")\
            if user_input.lower() == 'exit':\
                print("[MoodBot] Goodbye! Take care.")\
                break\
            response = self.respond(user_input)\
            print(f"[MoodBot]: \{response\}")\
\
if __name__ == "__main__":\
    bot = MoodBot()\
    bot.chat()\
}
