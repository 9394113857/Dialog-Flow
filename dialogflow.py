from flask import Flask, request
import requests
import wikipedia
import randfacts

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=["POST"])
def chat_bot():
    incoming_msg = request.values.get('Body', '').lower()
    # resp = MessagingResponse()
    msg = ""

    if 'good morning' in incoming_msg:
        # ! Return a gesture good morning
        msg.body('Good Morning..\nHave a nice day..')

    elif 'good afternoon' in incoming_msg:
        # ! Return a gesture good morning
        msg.body('Good Afternoon..')

    elif 'good evening' in incoming_msg:
        # ! Return a gesture good evening
        msg.body('Good Evening..\nHow was your day today?')

    elif 'good night' in incoming_msg:
        # ! Return a good night gesture
        msg.body('Good Night..\nSee you tomorrow..')

    elif 'fine' in incoming_msg:
        # ! Return a sweet gesture and ask what to do
        msg.body('Nice to hear that..\nWhat can I do for you master?')

    elif 'who made you' in incoming_msg:
        # ! Telling about your developer
        msg.body('Raghunadh Barlapudi made me.❤️❤️')

    elif "who are you" in incoming_msg:
        # ! Telling who am I
        msg.body('I am called Whatsapp Bot made by Raghunadh Barlapudi.❤️❤️')

    elif 'who developed you' in incoming_msg:
        # ! Returning whatsapp obeying
        msg.body('I obey whatsapp messenger.')

    elif 'how are you' in incoming_msg:
        # ! Telling how am I
        msg.body('I am fine..\nWhat about you??')

    elif 'about' in incoming_msg:
        # ! Telling your features
        msg.body(
            "Hi! I am Whatsapp Bot made By Raghunadh Barlapudi. Did you know that you can find out the weather, a movie rating and much more on whatsapp with just a few words!\nTry one of the following and I'll look it up for you!\n\n#weather PLACE: Check out the weather at any place.\n\n#wiki NAME: Search Wikipedia for anything you want.\n\n#quote: We'll send you awesome quote whenever you want it.\n\n#movie NAME: Checkout the IMDB Rating about any movie.\n\n#book NAME: Get details of any book you're interested in.\n\n#meaning WORD: Don't know the meaning of a word someone just messaged you? Try out my built in dictionary\n\n#synonym WORD: Don't know the synonyms of any word. Try my built in synonym finder.\n\n#coronastats: To get current status of Coronavirus in India\n\n#fact: Awesome facts, served streaming hot, whenever you want it!\n\n#news: Get the top 5 breaking news.\n\n#joke: Get jokes.")

    elif 'joke' in incoming_msg:
        # ! Return random joke.
        url = 'https://official-joke-api.appspot.com/jokes/general/random'
        r = requests.get(url)
        rj = r.json()
        try:
            for joke in rj:
                setup = joke['setup']
                punch = joke['punchline']
                msg.body(f'{setup}\n{punch}')
        except:
            msg.body('Sorry.. No Joke Found!!')
    else:
        msg.body("Sorry.. I didn't get that..\nTry *#about* ")

    return str(msg)


if __name__ == "__main__":
    app.run(debug=True)
