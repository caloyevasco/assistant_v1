from audio_rec import PicoVoiceWrapped
from speech_to_text import SpeechToText
from llm_wrapper import GeminiWrapped
from dotenv import load_dotenv
from audio_player import AudioFile
from text_to_speech import create_speech
import os

load_dotenv()

recorder = PicoVoiceWrapped(device_index=0, frame_length=512)
s2t = SpeechToText(model='small.en', device='cpu', compute_type='float32')
llm = GeminiWrapped(model=os.getenv('AI_MODEL'), api_key=os.getenv('GEMINI_API_KEY'))

recorder.record_audio()
trancribed_text = s2t.transcribe_audio_to_text(recorder.accumulated_data())

text = ""

for segment in trancribed_text[0]:
    text += segment.text

print(text)

prompt = text + " " + os.getenv("AI_PROMPT")
print(prompt)

response = llm.process(prompt=prompt)

# Usage example for pyaudio
a = AudioFile(create_speech(response))
a.play()
a.close()