import whisper

model = whisper.load_model("turbo")
print('hi')
result = model.transcribe("d.m4a", language='fa')
print(result["text"])
