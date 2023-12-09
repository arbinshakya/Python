import speech_recognition as sr
import pyttsx3
import pywhatkit

def talk(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say('Playing ' + command)
    engine.runAndWait()

def takeCommand():
    listener = sr.Recognizer()
    is_paused = False

    while True:  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                
                # Print the recognized command
                print("Recognized Command:", command)
                
                if 'play' in command:
                    song = command.replace('play', '')
                    talk(song)
                    pywhatkit.playonyt(song)
                elif 'pause' in command:
                    if not is_paused:
                        print("Pausing playback...")
                        # You can implement the pause logic using the appropriate library or API
                        is_paused = True
                elif 'resume' in command:
                    if is_paused:
                        print("Resuming playback...")
                        # You can implement the resume logic using the appropriate library or API
                        is_paused = False
                elif 'stop' in command:
                    print("Stopping playback...")
                    break  # Exit the loop to stop the program
                else:
                    print("Command not recognized")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    takeCommand()
