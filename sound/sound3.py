import wave
import struct

source = wave.open("in.wav", mode="rb")
dest = wave.open("out3.wav", mode="wb")

dest.setparams(source.getparams())

frames_count = source.getnframes()
data = struct.unpack(
    "<" + str(frames_count) + "h",
    source.readframes(frames_count))
# ---------------
newdata = [i * 3 if abs(i * 3) <= 32767 else 32767 * (i // abs(i)) for i in data]
# ---------------
newframes = struct.pack(
    "<" + str(len(newdata)) +
    "h", *newdata)
dest.writeframes(newframes)

source.close()
dest.close()