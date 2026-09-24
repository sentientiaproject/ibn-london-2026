import numpy as np
import wave
import struct

def generate_cinematic_soundtrack(output_wav="soundtrack.wav", duration=15.0, sample_rate=44100):
    total_samples = int(duration * sample_rate)
    audio = np.zeros(total_samples, dtype=np.float32)
    time = np.linspace(0, duration, total_samples, endpoint=False)

    def add_sub_bass(start_time, pitch_start=60, pitch_end=30, dur=2.5, volume=0.8):
        start_idx = int(start_time * sample_rate)
        n_samples = int(dur * sample_rate)
        if start_idx >= total_samples:
            return
        actual_samples = min(n_samples, total_samples - start_idx)
        t = np.linspace(0, dur, actual_samples, endpoint=False)
        freq = np.linspace(pitch_start, pitch_end, actual_samples)
        phase = 2 * np.pi * np.cumsum(freq) / sample_rate
        # Envelope: fast attack, exponential decay
        env = np.exp(-t * 2.2) * (1.0 - np.exp(-t * 50.0))
        audio[start_idx : start_idx + actual_samples] += np.sin(phase) * env * volume

    def add_brass_swell(start_time, root_freq=110.0, dur=3.5, volume=0.5):
        # 110 Hz (A2), 164.81 Hz (E3 - fifth), 220 Hz (A3 - octave)
        start_idx = int(start_time * sample_rate)
        n_samples = int(dur * sample_rate)
        if start_idx >= total_samples:
            return
        actual_samples = min(n_samples, total_samples - start_idx)
        t = np.linspace(0, dur, actual_samples, endpoint=False)
        # Swell envelope
        env = np.sin(np.pi * (t / dur) ** 0.6) * np.exp(-t * 0.4)
        
        # Sawtooth harmonic warmth
        harmonics = (
            np.sin(2 * np.pi * root_freq * t) +
            0.6 * np.sin(2 * np.pi * root_freq * 1.5 * t) +
            0.4 * np.sin(2 * np.pi * root_freq * 2.0 * t) +
            0.2 * np.sin(2 * np.pi * root_freq * 3.0 * t)
        )
        audio[start_idx : start_idx + actual_samples] += harmonics * env * volume * 0.25

    def add_chime(start_time, freq=1046.5, dur=1.8, volume=0.3):
        start_idx = int(start_time * sample_rate)
        n_samples = int(dur * sample_rate)
        if start_idx >= total_samples:
            return
        actual_samples = min(n_samples, total_samples - start_idx)
        t = np.linspace(0, dur, actual_samples, endpoint=False)
        env = np.exp(-t * 3.5)
        chime = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * freq * 2.0 * t)
        audio[start_idx : start_idx + actual_samples] += chime * env * volume

    # Scene 1: Opening Sub-bass drop + Lotus Chimes (0.0s)
    add_sub_bass(0.05, pitch_start=75, pitch_end=32, dur=3.0, volume=0.85)
    add_brass_swell(0.2, root_freq=98.0, dur=3.6, volume=0.6)
    add_chime(0.5, freq=880.0, dur=1.5, volume=0.25)
    add_chime(1.2, freq=1174.66, dur=1.8, volume=0.28)
    add_chime(2.0, freq=1318.51, dur=1.8, volume=0.3)

    # Scene 2: House of Commons Impact + Big Ben Bell Tone (3.8s)
    add_sub_bass(3.8, pitch_start=85, pitch_end=35, dur=2.8, volume=0.9)
    add_brass_swell(3.9, root_freq=110.0, dur=3.6, volume=0.7)
    # Big Ben E4 chime (329.6 Hz)
    add_chime(3.85, freq=329.63, dur=2.5, volume=0.5)
    add_chime(4.8, freq=392.0, dur=2.0, volume=0.35)
    add_chime(5.8, freq=523.25, dur=2.2, volume=0.4)

    # Scene 3: Oxford & Cambridge Prestige Crescendo (7.5s)
    add_sub_bass(7.5, pitch_start=95, pitch_end=40, dur=2.8, volume=0.8)
    add_brass_swell(7.6, root_freq=130.81, dur=3.8, volume=0.75)
    add_chime(8.0, freq=1046.5, dur=1.6, volume=0.3)
    add_chime(9.5, freq=1318.51, dur=1.8, volume=0.35)

    # Scene 4: Climax & Royal Fanfare (11.5s - 15.0s)
    add_sub_bass(11.5, pitch_start=110, pitch_end=28, dur=3.5, volume=1.0)
    add_brass_swell(11.6, root_freq=87.31, dur=3.4, volume=0.85)
    add_brass_swell(11.7, root_freq=130.81, dur=3.3, volume=0.7)
    add_chime(11.8, freq=1760.0, dur=2.5, volume=0.45)
    add_chime(12.5, freq=1318.51, dur=2.2, volume=0.4)

    # Add gentle ambient rumble
    rumble = np.sin(2 * np.pi * 38.0 * time) * 0.05 * np.exp(-time * 0.08)
    audio += rumble

    # Master Limiter / Normalization
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val * 0.95

    # Write 16-bit PCM WAV
    with wave.open(output_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        int_data = (audio * 32767).astype(np.int16)
        wf.writeframes(int_data.tobytes())

    print(f"Soundtrack generated: {output_wav} ({duration}s @ {sample_rate}Hz)")

if __name__ == "__main__":
    generate_cinematic_soundtrack()
