import json,sys,wave
from vosk import Model, KaldiRecognizer, SetLogLevel

# # You can set log level to -1 to disable debug messages
SetLogLevel(-1)

wf = wave.open('test.wav', "rb")
# Load to Memory
# audio_data = wf.readframes(wf.getnframes())
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model = Model("vosk-model-small-cn-0.22")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
str_ret = ""

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    # Read Audio frames & Trans
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)

        result = json.loads(result)
        if 'text' in result:
            # print(result['text'])
            str_ret += result['text'] + ' '
    # else:
    #     print(rec.PartialResult())

# print(rec.FinalResult())
result = json.loads(rec.FinalResult())
if 'text' in result:
    str_ret += result['text']

print(str_ret)