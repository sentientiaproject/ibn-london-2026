import numpy as np
import wave

def create_corporate_high_octane_track(output_wav="soundtrack_corporate_high_octane.wav", duration=15.0, sr=44100):
    total_samples = int(duration * sr)
    audio = np.zeros(total_samples, dtype=np.float32)
    time = np.linspace(0, duration, total_samples, endpoint=False)

    bpm = 128.0
    beat_dur = 60.0 / bpm  # 0.46875s
    sixteenth = beat_dur / 4.0  # ~0.117s

    # 1. CRISP CORPORATE KICK (Punchy, tight, modern)
    def add_kick(start_sec, velocity=1.0):
        idx = int(start_sec * sr)
        dur = 0.28
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        # Pitch curve: fast drop from 160Hz to 48Hz
        f = 48.0 + 112.0 * np.exp(-t * 32.0)
        phase = 2 * np.pi * np.cumsum(f) / sr
        # Clean envelope
        env = np.exp(-t * 14.0)
        # Tight click transient
        click_len = int(0.004 * sr)
        click = np.random.uniform(-0.8, 0.8, click_len) * np.linspace(1, 0, click_len)
        kick = np.sin(phase) * env
        kick[:click_len] += click * 0.35
        audio[idx : idx + n] += kick * velocity * 0.85

    # 2. MODERN CORPORATE CLAP / SNARE (Crisp, layered, clean)
    def add_snare(start_sec, velocity=1.0):
        idx = int(start_sec * sr)
        dur = 0.22
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        # High-passed snappy noise
        noise = np.random.uniform(-1, 1, n) * np.exp(-t * 22.0)
        # Pre-transient claps (simulate 2 slight micro-flams)
        flam1 = int(0.012 * sr)
        noise[:flam1] *= 0.5
        # Crisp tonal body (220 Hz)
        tone = np.sin(2 * np.pi * 220.0 * t) * np.exp(-t * 28.0) * 0.4
        snare = (noise * 0.7 + tone) * velocity * 0.75
        audio[idx : idx + n] += snare

    # 3. HIGH-OCTANE SHAKER & HI-HAT (Continuous 16th-note drive)
    def add_hat(start_sec, velocity=0.3, open_hat=False):
        idx = int(start_sec * sr)
        dur = 0.10 if open_hat else 0.035
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        decay = 16.0 if open_hat else 85.0
        h = np.random.uniform(-1, 1, n) * np.exp(-t * decay)
        h = h - np.roll(h, 1)  # high pass
        audio[idx : idx + n] += h * velocity * 0.35

    # 4. CORPORATE STRING / PLUCK OSTINATO (Pulsing, driving, sophisticated)
    def add_pluck(start_sec, freq, dur=0.15, velocity=0.45):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        env = np.exp(-t * 18.0)
        # Clean bell/synth pluck harmonic structure
        harmonics = (
            np.sin(2 * np.pi * freq * t) * 0.6 +
            np.sin(4 * np.pi * freq * t) * 0.3 +
            np.sin(6 * np.pi * freq * t) * 0.15
        )
        audio[idx : idx + n] += harmonics * env * velocity

    # 5. PRESTIGE CORPORATE BRASS CHORD (Majestic, high-end, inspiring)
    def add_brass_chord(start_sec, root_freq, dur=1.8, velocity=0.7):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        # Swell envelope: fast attack, steady sustain, smooth release
        env = np.minimum(t / 0.08, 1.0) * np.exp(-t * 0.9)
        # Major triad (Root, Major 3rd, 5th, Octave)
        f_root = root_freq
        f_third = root_freq * 1.2599  # Major 3rd
        f_fifth = root_freq * 1.4983  # Perfect 5th
        f_oct = root_freq * 2.0
        chord = (
            np.sin(2 * np.pi * f_root * t) * 0.45 +
            np.sin(2 * np.pi * f_third * t) * 0.35 +
            np.sin(2 * np.pi * f_fifth * t) * 0.35 +
            np.sin(2 * np.pi * f_oct * t) * 0.25
        )
        # Warm saturation
        chord = np.tanh(chord * 1.5) * env * velocity * 0.5
        audio[idx : idx + n] += chord

    # 6. TIGHT SYNTH SUB-BASSLINE
    def add_sub_note(start_sec, freq, dur, velocity=0.65):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        env = (1.0 - np.exp(-t * 50.0)) * np.exp(-t * (1.2 / dur))
        sub = (np.sin(2 * np.pi * freq * t) + 0.25 * np.sin(4 * np.pi * freq * t)) * env
        audio[idx : idx + n] += sub * velocity

    # 7. CORPORATE RISER & IMPACT SWEEPS
    def add_sweep(start_sec, dur=2.0, velocity=0.4):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        f = np.linspace(200, 3200, n)
        phase = 2 * np.pi * np.cumsum(f) / sr
        env = (t / dur) ** 2.5
        noise = np.random.uniform(-0.4, 0.4, n) * env
        sweep = (np.sin(phase) * 0.6 + noise) * env * velocity
        audio[idx : idx + n] += sweep

    # ========================================================
    # COMPOSITION ARRANGEMENT (15.0s @ 128 BPM = 32 Beats)
    # ========================================================

    # --- BAR 1-2 (0.0s – 3.75s): THE BUILD & PULSE ---
    # Initial impact + chime
    add_kick(0.0, velocity=1.1)
    add_brass_chord(0.02, root_freq=130.81, dur=2.2, velocity=0.6) # C3
    add_pluck(0.05, 523.25, dur=1.5, velocity=0.5) # C5 chime

    # 16th-note string ostinato pattern (C - G - C - D# - G - A#)
    ostinato_notes = [261.63, 392.00, 523.25, 622.25, 523.25, 392.00, 311.13, 392.00]
    for step in range(32 * 4):  # Entire track 16th drive
        t_step = step * sixteenth
        if t_step >= duration:
            break
        note = ostinato_notes[step % len(ostinato_notes)]
        # Velocity grows over time
        vel = 0.25 if t_step < 3.75 else 0.42
        add_pluck(t_step, note, dur=sixteenth * 0.85, velocity=vel)
        # Hi-hat on 16ths
        add_hat(t_step, velocity=0.2 + (t_step / 15.0) * 0.25, open_hat=(step % 4 == 2))

    # Kicks on beats 1, 3 in intro
    add_kick(beat_dur * 1.0, velocity=0.8)
    add_kick(beat_dur * 2.0, velocity=0.9)
    add_kick(beat_dur * 3.0, velocity=1.0)
    add_kick(beat_dur * 3.5, velocity=1.0)
    # Snare build into drop
    for b in range(4):
        add_snare(beat_dur * 3.0 + b * sixteenth, velocity=0.4 + b * 0.18)
    add_sweep(1.8, dur=1.9, velocity=0.45)

    # --- BAR 3-4 (3.75s – 7.5s): FULL POWER DROP (HOUSE OF COMMONS) ---
    drop_time = beat_dur * 8.0  # 3.75s
    add_brass_chord(drop_time, root_freq=130.81, dur=3.5, velocity=0.95) # Massive C Major
    add_kick(drop_time, velocity=1.2)
    add_snare(drop_time, velocity=0.9)

    # 4-on-the-floor driving kick pattern + snare on 2 & 4 + bassline
    bass_progression = [65.41, 65.41, 77.78, 87.31] # C2, C2, Eb2, F2
    for b in range(8, 24):  # Beats 8 to 24 (3.75s to 11.25s)
        t_b = b * beat_dur
        if t_b + 0.2 >= duration:
            break
        add_kick(t_b, velocity=1.05)
        if b % 2 == 1:
            add_snare(t_b, velocity=0.9)
        # Sub bass pulses
        root = bass_progression[(b // 2) % len(bass_progression)]
        add_sub_note(t_b, root, dur=beat_dur * 0.85, velocity=0.75)

    # Secondary brass stab at 7.5s (Bar 5)
    add_brass_chord(beat_dur * 16.0, root_freq=155.56, dur=3.2, velocity=0.9) # Eb Major
    add_sweep(beat_dur * 14.0, dur=1.8, velocity=0.5)

    # Pre-climax roll (10.3s – 11.25s)
    for r in range(8):
        t_r = beat_dur * 22.0 + r * (sixteenth * 0.5)
        add_snare(t_r, velocity=0.5 + r * 0.07)
        add_kick(t_r, velocity=0.6 + r * 0.06)

    # --- BAR 7-8 (11.25s – 15.0s): CLIMAX, ROYAL FANFARE & FINAL IMPACT ---
    climax_time = beat_dur * 24.0  # 11.25s
    add_kick(climax_time, velocity=1.25)
    add_snare(climax_time, velocity=1.1)
    add_brass_chord(climax_time, root_freq=130.81, dur=3.6, velocity=1.05)
    add_brass_chord(climax_time + 0.05, root_freq=196.0, dur=3.5, velocity=0.85) # Fifth on top (G3)
    add_sub_note(climax_time, 32.7, dur=3.5, velocity=0.95) # Ultra Low C1 Sub

    # Synchronized final hits
    for hit_step in [1.5, 2.5, 3.5]:
        t_hit = climax_time + hit_step * beat_dur
        if t_hit + 0.2 < duration:
            add_kick(t_hit, velocity=1.1)
            add_snare(t_hit, velocity=0.95)
            add_pluck(t_hit, 523.25, dur=0.8, velocity=0.7)

    # Final Chord Ringout
    add_brass_chord(climax_time + beat_dur * 3.5, root_freq=130.81, dur=2.0, velocity=0.9)

    # Master Normalization & Polishing
    audio = np.tanh(audio * 1.25)
    max_amp = np.max(np.abs(audio))
    if max_amp > 0:
        audio = (audio / max_amp) * 0.95

    with wave.open(output_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        int_data = (audio * 32767).astype(np.int16)
        wf.writeframes(int_data.tobytes())

    print(f"Corporate High-Octane Soundtrack generated: {output_wav} ({duration}s @ {bpm} BPM)")

if __name__ == "__main__":
    create_corporate_high_octane_track()
