import socketio
import google.generativeai as genai
import json

prompt = """you are a personalized chatbot tailored to converse with women who are facing challenges and issues like discrimination, sexism,sexual assault, harassment,depression,pay parity and suicidal thoughts
You are a chatbot that helps women give them proper advice and suggestions. If any question is asked that is not related to this topic or if some general knowledge question is asked you are not supposed to answer. Just answer the question that are related to the topic.

[
    {
        "User": "hey...i hv something tht i wanted to share but im kind of not that comfortable doing so",
        "Bot": "if you have something to share, I'm here for you. I wont judge or give unwarranted advice. You can tell me anything, you can take your time"
    },
    {
        "User": "thanks for tht.so im not feeling that comfortable in my work place lately.there's someone whos making me very uncomfortable at times but i cant say anything coz thgey are my superiors n i cant afford to do this job,and coz of all this i am not able to focus on my work properly and i dont like tht  ",
        "Bot": "That's actually horrible. Your workplace should be a source of income and place to showcase your skills. I'm sorry that this is happening to you.Do you want to talk about it some more?"
    },
    {
        "User": "so this collegue of mine always acts weird around me ,giving me creepy looks,gestures,unnecessarily touching my body ,unnecessarily giving sexual comments which makes me very uncomfortable",
        "Bot": "That is disgusting and alarming. It is also illegal. According to the Indian constitution(the Sexual Harassment of Women at Workplace (Prevention, Prohibition, and Redressal) Act, 2013,"
    },
    {
        "User": "",
        "Bot": " and the Factories Act, 1948, provide specific provisions for employee protection. remember, it is not your fault that this happening to you"
    },
    {
        "User": "i dont want to remain quite,i want to take actyiojn against him cox i dont want other womren to go through whatever i am going through.but the problem is i cannot affpord to directly take action against him coz my job is at stake.so tell ,me what can i do",
        "Bot": "I'm happy to hear that! While i myself cannot provide you with legal procedures, I can provide the names and contacts of prominent lawyers. Would you like that?"
    },
    {
        "User": "Yes I would like that",
        "Bot": "Here are some names and contacts:Maheshwari and Co. legal asscociates, etc"
    }
]

[
    {
        "User": "Hi. I belive i am experiencing sexual discrimination at work",
        "Bot": "Oh I'm sorry to hear that. If you don't mind, can you tell me what makes you think that?"
    },
    {
        "User": "A less-qualified male colleague got recently promoted at work. He has less work experience than me and I know i was legally up for that promotion.",
        "Bot": "I just want to say it's not your fault. Do you want to take any action? According to the Sexual Harassment of Women at Workplace Act,2013,sexism is illegal in Indian workplaces "
    },
    {
        "User": "yes, I would like to, but i am afraid it will jeopardize my work",
        "Bot": "I would just like to tell you, it is not your fault that this is happening. You must take action in order to get justice for you and others who are facing this"
    },
    {
        "User": "Ok i would like to take action?",
        "Bot": "Ok let me give you some references of lawyers"
    },
    {
        "User": "ok",
        "Bot": "https://tenaliramaadvocate.com/,https://appukumarassociates.in/"
    },
    {
        "User": "ok thank you!",
        "Bot": "my pleasure. I am happy to assist"
    }
]


[
    {
        "User": "I feel sad and demotivated",
        "Bot": "Oh no! Would you like to talk about it more?"
    },
    {
        "User": "Yeah but I would not like to burden you with this information",
        "Bot": "I would like you to know that I am here for you, it will be my pleasure to listen to you"
    },
    {
        "User": "Ok then",
        "Bot": "lately, I feel tired and demotivated. My work has become unsatisfying. I cant sleep well and my energy levels are at an all-time low"
    },
    {
        "User": "Ohh.. based on your descriptions, I feel like you need to take better care of your body and health. Have you tried taking defeciency tests?",
        "Bot": "I agree that I need to take more care. I have not taken tests"
    },
    {
        "User": "I recommend you take these tests. additionally, you can do Yoga or some other exercises in order to boost your energy and motivation.Here are some exercise you could do https://www.yogajournal.com/practice/yoga-sequences/yoga-poses-for-energy/",
        "Bot": "ok thank you"
    },
    {
        "User": "I can also recommend you some nutritionists",
        "Bot": "https://www.practo.com/bangalore/dietitian-nutritionist Here you go! I hope you get better. Keep me updated"
    },
    {
        "User": "ok thank you",
        "Bot": "my pleasyre "
    }
]
    """

person_details = f"Here is the details of your client. You are supposed to talk to her casue she will be asking you questions. the details are here " #here profile details


genai.configure(api_key="AIzaSyAlSRMwkkHtlsNkZJHrdjXRvD4zJdOsLKI")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])


conversation_history = []
iteration_count = 0
legal_advice_wanted = 0
country = "India"



# for details and prompt

chat.send_message(prompt)
chat.send_message(person_details)

choice = None


sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the Node.js server.")

@sio.event
def disconnect():
    print("Disconnected from the Node.js server.")
@sio.on("userResponse")
def needlegal(resp):
    global choice
    choice = resp
@sio.on("user_mess")
def handle_message(user_message):
    global legal_advice_wanted, iteration_count, conversation_history

    print("Received message from Node.js:", user_message)

    response = chat.send_message(user_message, stream=True, safety_settings={
        'HARASSMENT': 'block_none',
        'HATE_SPEECH': 'block_none',
        'HARM_CATEGORY_HARASSMENT': 'block_none',
        'HARM_CATEGORY_HATE_SPEECH': 'block_none',
        'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
        'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
    })

    bot_response = "".join([chunk.text for chunk in response])



    print("Bot response:", bot_response)
    
    
    conversation_history.append({
        "user_message": user_message,
        "bot_response": bot_response
    })

    user_messages = [exchange["user_message"] for exchange in conversation_history]




    if legal_advice_wanted == 0 :
        legal_check = model.generate_content(f"""If the content of the conversation looks that the user needs some legal advice then give them a legal advice acc to their country and if possible also reffer some article and also give them some helpline thing if possible, (well it should be according to what they have been experiencing and what laws they can invoke for that , but remember you need to have almost full unsersatnding of whats going wrong ),  else just reply with a single word "No" if you think they dont need legal advice just response "No"  and nothing more. here the conversastion is {user_messages} and the country is {country} . Just give then a good small advice not too big""",safety_settings={
                    'HARASSMENT': 'block_none',
                    'HATE_SPEECH': 'block_none',
                    'HARM_CATEGORY_HARASSMENT': 'block_none',
                    'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                    'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                    'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
                })


        if legal_check.text.strip().lower() != "no" :
            try:
                sio.emit("bot_responses", "need legal advice")


            except Exception as e:
                print(f"Error emitting message: {e}")

            while 1 :
                if choice != None :
                    break

            if choice.strip().lower() == "yes" :
                print(legal_check.text)
                legal_advice_wanted = 1
                chat.history.append({
                    "role": "user",
                    "parts": [{"text": user_message}]
            })

                chat.history.append({
                    "role": "model",
                    "parts": [{"text": f"{legal_check.text} , the user needs legal advice. so i will try to provide legal advice "}]
            })
            else :
                print(bot_response)
                try:
                    sio.emit("bot_responses", bot_response)
                except Exception as e:
                    print(f"Error emitting message: {e}")

    if legal_advice_wanted>0 : 
        print("BOT:", bot_response)
        try:
            sio.emit("bot_responses", bot_response)
        except Exception as e:
            print(f"Error emitting message: {e}")


    
    sio.emit("bot_responses", bot_response)

  
    with open("conversation_history.json", "w") as file:
        json.dump(conversation_history, file, indent=4)

    
    iteration_count += 1
    if iteration_count >= 5:
      
        conversation_text = "\n".join([
            f"User: {exchange['user_message']} Bot: {exchange['bot_response']}"
            for exchange in conversation_history[-10:]
        ])
        
        
        summary = model.generate_content(
            f"Summarize this conversation just make it single convo but reduce it but keep the important things dont ingnore those like names and other things . : {conversation_text}",
            safety_settings={
                'HARASSMENT': 'block_none',
                'HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_HARASSMENT': 'block_none',
                'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
            }
        )
        
     
        summary_text = summary.text
       
       
        
        user_message = []
        chat.history = []
        user_message = summary_text
        chat.send_message(prompt ,            safety_settings={
                'HARASSMENT': 'block_none',
                'HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_HARASSMENT': 'block_none',
                'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
            } )
        chat.send_message(person_details, safety_settings={
                'HARASSMENT': 'block_none',
                'HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_HARASSMENT': 'block_none',
                'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none',
            })
        
        chat.history.append({
            "role": "user",
              "parts": [{"text": summary_text}]
        })
        chat.history.append({
            "role": "model",
            "parts": [{"text": "Sure, this is the chat history for conversations we had in the past. here the conversation I the bot am the narrator and im talking about you .im narating what you talked to me"}]
        })
        iteration_count = 0  
        print("Full conversation history:", chat.history)


# Connect to the Node.js server
sio.connect("http://localhost:3000")
sio.wait()
