# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
def callChatWithOpenAI():
    # chatwithOpenAI(question)
    print("question: " + question)
    print("answer: " + chatwithOpenAI(question))
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
    # Place the label, text field, and button in the window




# Example usage
def copy_text():
  input_text = input_text_field.get()
  output_text_field.delete(0, tk.END)
  output_text_field.insert(0, input_text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = "Bitte schreibe einen Email auf Deutsch an Frau Koepli. Ich möchte mitteilen, dass die Heizung zu hoch abgestellt is: der Zimmertemperatur ist 24.5 Grad. Gebäude:Büttenenhalde 37, Apartment 38. Bei dieser Gelegenheit möchte ich Frau Koepli auch eine schöne Weihnachtszeit zuwünschen und ein frohes Neues Jahr."

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Text Field Example")

# Create a label and an input text field
input_label = tk.Label(window, text="Enter some text:")
input_text_field = tk.Entry(window)

# Create an output label and an output text field
output_label = tk.Label(window, text="Output:")
output_text_field = tk.Entry(window)

# Create a button
button = tk.Button(window, text="Copy", command=copy_text)

# Place the labels and text fields in the window
input_label.pack()
input_text_field.pack()
output_label.pack()
output_text_field.pack()
button.pack()

# Run the main loop
window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
