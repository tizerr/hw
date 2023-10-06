import wave

with wave.open('sample.wav', 'rb') as src:
    data = src.readframes(src.getnframes())
    new_data = data[::-1]
with wave.open('out.wav', 'wb') as out:
    out.setparams(src.getparams())
    out.writeframes(new_data)
