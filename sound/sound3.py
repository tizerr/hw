import wave

with wave.open('sample.wav', 'rb') as src:
    data = src.readframes(src.getnframes())
    new_data = [i * 2 for i in data]  # увеличение
with wave.open('out.wav', 'wb') as out:
    out.setparams(src.getparams())
    out.writeframes(new_data)
