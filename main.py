# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    import os
    #import openai
    # openai.organization = ""
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # openai.Model.list()
    import openai

    # Set your API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Set the model to use
    model_engine = "text-davinci-002"

    # Set the prompt for the model
    prompt = "Write a short story about a person who goes on a journey"

    # Generate a response from the model
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Print the response
    # Access the text attribute
    text = completion.choices[0]["text"]

    # Print the text
    print(text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
