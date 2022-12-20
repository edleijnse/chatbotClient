# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def chatwithOpenAI(question):
    # Use a breakpoint in the code line below to debug your script.
    import os
    #import openai
    # openai.organization = ""
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # openai.Model.list()
    import openai

    # Set your API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set the model to use
    model_engine = "text-davinci-003"

    # Set the prompt for the model
    # prompt = "Write a short story about a person who goes on a journey"
    prompt = question    # Generate a response from the model
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    # Print the response
    # Access the text attribute
    text = completion.choices[0]["text"]

    # Print the text
    #print(text)
    return text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = "Bitte schreibe einen Email auf Deutsch an Frau Koepli. Ich möchte mitteilen, dass die Heizung zu hoch abgestellt is: der Zimmertemperatur ist 24.5 Grad. Gebäude:Büttenenhalde 37, Apartment 38. Bei dieser Gelegenheit möchte ich Frau Koepli auch eine schöne Weihnachtszeit zuwünschen und ein frohes Neues Jahr."

    print(chatwithOpenAI(question))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
