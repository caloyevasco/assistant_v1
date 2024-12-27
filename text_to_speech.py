from pyht import Client
from dotenv import load_dotenv
from pyht.client import TTSOptions
from pyht import Language
import os

load_dotenv()

def create_speech(dialogue: str):
    # Create client only when needed
    client = Client(
        user_id=os.getenv("PLAY_HT_USER_ID"),
        api_key=os.getenv("PLAY_HT_API_KEY"),
    )
    
    options = TTSOptions(voice="s3://voice-cloning-zero-shot/775ae416-49bb-4fb6-bd45-740f205d20a1/jennifersaad/manifest.json", language=Language.TAGALOG)
    
    try:
        with open("output_jenn.wav", "wb") as audio_file:
            for chunk in client.tts(dialogue, options, voice_engine='Play3.0-mini-http'):
                audio_file.write(chunk)
                
    finally:
        # Close the client connection
        client.close()
        
    return "output_jenn.wav"

if __name__ == "__main__":
    create_speech("Hello There Carlo")