# Chatbot

A chatbot to answer questions people may have about the Methodist University of Angola.  
Currently, I've added more than 400 questions and answers people may have about the university, but it's a work in progress.  
Since at least half of the questions people seem to have are generic and not specific at all, I'm thinking about integrating an AI model to deal with the basic chatter, while I manually train it to handle the specific questions.

---

## How to run it?

1. Clone the repo.  
2. Install the dependencies. (it's a good ideia to use a virtual environment here)
3. Train the answers using `python treinador.py` and your own questions.  
   (Save the questions in a `.txt` file inside the `dados` folder.)  
4. Run the main script using `python main.py` 


After running the app, it should redirect you to a website where you can ask questions to the bot.
(or just paste `http://127.0.0.1:5000` on your browser)

---


## Future features?

- Possibly expand the bot to handle general questions about higher education in Angola (e.g., other colleges or universities).  

## Notes

I'm not really thinking of adding new features.  
To be honest, I don’t enjoy building chatbots — it's boring — but I’m going to complete the project.
