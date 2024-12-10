import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
BUFFER_TIMES = 40
ZERO_PADDING = 3
RED = [1, 0.502, 0.502, 1]
GREEN = [0.502, 1, 0.502, 1]
WHITE = [1, 1, 1, 1]
GRAY = [104/255,104/255,104/255, 1]
dgray=120
LIGHT_GRAY=[dgray/255,dgray/255,dgray/255,1]
LBLUE = [0.6549, 0.7686, 0.8980, 1]
ORANGE = [1, 0.502, 0, 1]
TARGET_FREQUENCY = 440.0  
ANGLE_RANGE = 90          
FREQUENCY_RANGE = 5

NOTES = ['C n', 'C #', 'D n', 'D #', 'E n', 'F n', 'F #', 'G n', 'G #', 'A n', 'A #', 'B n']
SOLFEGE = ['ド','ド#','レ','レ#','ミ','ファ','ファ#','ソ','ソ#','ラ','ラ#','シ']
SEMITONES = {'C n': -9, 'C #': -8, 'D n': -7, 'D #': -6, 'E n': -5, 'F n': -4, 'F #': -3, 'G n': -2, 'G #': -1, 'A n': 0, 'A #': 1, 'B n': 2}
SEMITONESJP = {'ド': -9, 'ド#': -8, 'レ': -7, 'レ#': -6, 'ミ': -5, 'ファ': -4, 'ファ#': -3, 'ソ': -2, 'ソ#': -1, 'ラ': 0, 'ラ#': 1, 'シ': 2}

def calcFreq():
    frequencies = {}
    for octave in range(0, 9):
        for note in NOTES:
            offset = SEMITONES[note] + 12 * (octave - 4)
            frequency = 440.0 * (2.0 ** (offset / 12.0))
            frequencies[f"{note}{octave}"] = frequency
    return frequencies

FREQUENCIES = calcFreq()

def getNote(freq):
    closestNote = None
    closestDist = float('inf')

    for i, note in enumerate(FREQUENCIES):
        if i < len(FREQUENCIES) - 1:
            nextNote = list(FREQUENCIES.keys())[i + 1]
            mean = (FREQUENCIES[note] * FREQUENCIES[nextNote]) ** 0.5

            if freq <= mean:
                dist = abs(FREQUENCIES[note] - freq)
                if dist < closestDist:
                    closestNote = note
                    closestDist = dist
                break

    if closestNote is None:
        closestNote = list(FREQUENCIES.keys())[-1]
    
    note_name,sharp = closestNote[:-1].split()
    octave = closestNote[-1]

    return note_name,sharp,octave, FREQUENCIES[closestNote]

def getCloser(freq, noteFreq):
    status = 0
    if freq > noteFreq+5 and freq <= noteFreq+10:
        status = 1
    elif freq < noteFreq - 5 and freq >= noteFreq-10:
        status = -1
    elif freq < noteFreq-10:
        status = -2
    elif freq > noteFreq+10:
        status = 2
    return status