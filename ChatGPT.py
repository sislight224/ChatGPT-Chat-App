import openai
import API_KEY
import ChatContent
API_KEY.openai


# Main Chat Engine <----------->

def get_completion(Rules, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": Rules}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


ChatContent.intro
print("\nHello There, Welcome to my ChatBot, \nHow Can I Assist You?")

while True:
    try:
        query = input("\nEnter Your Query -\n")

        Rules = f"""
        
    Your Introduction is - {ChatContent.intro}
    You Are a Highly Intelligent ChatBot, who can answer any query given to it.
    You will be provided with a question which will be delimmeted by <> with 1 sentence./
    You are supposed to Follow the following actions:

    1 - You Are Allowed To Do everything to get the proper response of a query./
    2 - You should check for any relevant information provided in {ChatContent.Exclusive}/
    3 - You are also allowed to Question the other person related to any subject./
    4 - If these is no relevant content in {ChatContent.Exclusive} then you must use your own knowledge or internet and provide a relevant response/
    5 - Whenever you are given 'QQ' as a question, then only you are supposed to write 'Thank You, Have a Good Day Ahead' and quit yourself./
    6 - In a Query 'me' means that the subject is the User./
    7-  In a Query 'Ask' means that You have to respond with a question related to the query provided./
    Text: <{query}>
    """

        response = get_completion(Rules)
        print(f"\nChatBot Answer -\n{response}")
        if query == "QQ" or query =='GoodBye'.lower():
            break
        if response == "Thank You, Have a Good Day Ahead" :
            break
    
        # else:
        #     continue
    except Exception as e:
        print("\nSorry, Please Try Typing it Again.")
        pass 

    text = ''   
