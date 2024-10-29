import customtkinter as ctk
import speech_recognition as sr

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class SpeechRecognitionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Voice Tool")
        self.geometry("400x200")

        self.input_label = ctk.CTkLabel(self, text="")
        self.input_label.pack(pady=10)

        self.input_entry = ctk.CTkEntry(self, width=300)
        self.input_entry.pack(pady=10)
        self.input_entry.configure(state="readonly")

        self.recognize_button = ctk.CTkButton(self, text="Распознать речь", command=self.recognize_speech)
        self.recognize_button.pack(pady=10)

    def recognize_speech(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Говорите что-нибудь!")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {text}")
            self.input_entry.configure(state="normal")
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, text)
            self.input_entry.configure(state="readonly")
        except sr.UnknownValueError:
            print("Не удалось распознать аудио")
            self.show_no_result_message()
        except sr.RequestError as e:
            print(f"Не удалось получить результаты от Google Speech Recognition; {e}")
            self.show_no_result_message()

    def show_no_result_message(self):
        self.input_entry.configure(state="normal")
        self.input_entry.delete(0, "end")
        self.input_entry.insert(0, "Ничего не распознано")
        self.input_entry.configure(state="readonly")

if __name__ == "__main__":
    app = SpeechRecognitionApp()
    app.mainloop()
