class BaseRecorder(object):
    def __init__(self, device_index: int | None, frame_length: int | None):
        self.device_index = device_index
        self.frame_length = frame_length
        self.audio_data = []

    def record_audio(self):
        pass

    def accumulated_data(self):
        pass


class PicoVoiceWrapped(BaseRecorder):
    def __init__(self, device_index: int | None, frame_length: int | None):
        from pvrecorder import PvRecorder
        super().__init__(device_index=device_index, frame_length=frame_length)
        self._recorder = PvRecorder(
            frame_length=self.frame_length,
            device_index=self.device_index
        )

    def record_audio(self):
        self._recorder.start()
        while True:
            try:
                print("\rRecording...", end="", flush=True)
                read = self._recorder.read()
                self.audio_data.extend(read)

            except KeyboardInterrupt:
                print("\nStopped...")
                self._recorder.stop()
                break

    def accumulated_data(self):
        from io import BytesIO
        import wave
        import struct
        
        buffer = BytesIO()
        with wave.open(buffer, 'wb') as wav_file:
            wav_file.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            wav_file.writeframes(
                struct.pack(
                    "h" * len(self.audio_data),
                    *self.audio_data
                )
            )
        
        buffer.seek(0)
        return buffer


if __name__ == "__main__":
    wrapped = PicoVoiceWrapped(device_index=0, frame_length=512)
    wrapped.record_audio()
    wav_data = wrapped.accumulated_data()
    # Optionally save to file
    with open('recorded_audio.wav', 'wb') as f:
        f.write(wav_data)