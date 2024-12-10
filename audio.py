import numpy as np
from scipy.signal import butter, filtfilt
from calculations import BUFFER_TIMES, RATE, ZERO_PADDING, CHUNK
from numpy.fft import fft, fftfreq

class AudioProcessor:
    def __init__(self, CHUNK, RATE, ZERO_PADDING, BUFFER_TIMES, alpha=0.1, change_threshold=10.0):
        self.buffer = np.zeros(CHUNK * BUFFER_TIMES)
        self.hanning_window = np.hanning(len(self.buffer))
        
        self.smoothed_freq = 0
        self.smoothed_mag = 0
        self.alpha = alpha  
        self.change_threshold = change_threshold          
        self.previous_freq = 0

    def butter_pass(self, data, lowcut=20, highcut=10000, order=4):
        nyquist = 0.5 * RATE
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype='band') 
        filtered = filtfilt(b, a, data)
        return filtered

    def harmonic_product_spectrum(self, mag, num_harmonics=7):
        n = len(mag)
        hps = mag.copy()
        for i in range(2, num_harmonics + 1):  
            hps[:n // i] *= mag[i - 1::i]    
        return hps

    def process_audio(self, signal):
        self.buffer[:-CHUNK] = self.buffer[CHUNK:]
        self.buffer[-CHUNK:] = signal
        filtered_signal = self.butter_pass(self.buffer)
        windowed_signal = filtered_signal * self.hanning_window
        fftdata = np.fft.fft(np.pad(windowed_signal, (0, len(self.buffer) * ZERO_PADDING), "constant"))
        mag = np.abs(fftdata)
        mag = mag[:len(mag) // 2]  
        freqs = np.fft.fftfreq(len(fftdata), 1. / RATE)
        freqs = freqs[:len(freqs) // 2]
        hps_mag = self.harmonic_product_spectrum(mag)
        idx = np.argmax(hps_mag)
        newfreq = freqs[idx]
        newmag = hps_mag[idx]
        freq_change = abs(newfreq - self.previous_freq)
        if freq_change > self.change_threshold:
            self.smoothed_freq = newfreq  
            self.smoothed_mag = newmag  
        else:
            self.smoothed_freq = self.alpha * newfreq + (1 - self.alpha) * self.smoothed_freq
            self.smoothed_mag = self.alpha * newmag + (1 - self.alpha) * self.smoothed_mag
        self.previous_freq = self.smoothed_freq
        return self.smoothed_freq, self.smoothed_mag/10**40