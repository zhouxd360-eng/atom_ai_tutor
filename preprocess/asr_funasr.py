from funasr import AutoModel

class ASRProcessor:
    def __init__(self):
        self.model = AutoModel(model="paraformer-zh")
    
    def transcribe(self, audio_path):
        result = self.model.generate(input=audio_path)
        return result[0]["text"]

if __name__ == "__main__":
    processor = ASRProcessor()
    print(processor.transcribe("test.wav"))