from faster_whisper import WhisperModel


class SpeechToText:

    def __init__(self, model : str, device : str, compute_type: str):
        self.model = WhisperModel(
            model_size_or_path=model,
            device=device,
            compute_type=compute_type
        )
    
    def transcribe_audio_to_text(self, audio):
        return self.model.transcribe(
            audio=audio,
            language='en'
        )