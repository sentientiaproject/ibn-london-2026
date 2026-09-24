import numpy as np
import wave

def create_high_energy_trailer_track(output_wav="soundtrack_high_energy.wav", duration=15.0, sr=44100):
    total_samples = int(duration * sr)
    audio = np.zeros(total_samples, dtype=np.float32)
    time = np.linspace(0, duration, total_samples, endpoint=False)

    bpm = 126.0
    beat_dur = 60.0 / bpm  # ~0.476 sec
    total_beats = int(duration / beat_dur)

    # 1. PUNCHY 808 KICK DRUM
    def add_kick(start_sec, punch=1.0):
        idx = int(start_sec * sr)
        dur = 0.35
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        # Fast pitch drop from 180Hz down to 42Hz
        f = 42 + 138 * np.exp(-t * 28.0)
        phase = 2 * np.pi * np.cumsum(f) / sr
        env = np.exp(-t * 12.0)
        # Click transient at start
        click = np.random.uniform(-1, 1, int(0.005 * sr)) * np.linspace(1, 0, int(0.005 * sr))
        kick = np.sin(phase) * env
        kick[:len(click)] += click * 0.4
        audio[idx : idx + n] += kick * punch * 0.85

    # 2. SHARP CRACKING SNARE / CLAP
    def add_snare(start_sec, volume=0.8):
        idx = int(start_sec * sr)
        dur = 0.28
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        # Noise burst
        noise = np.random.uniform(-1, 1, n) * np.exp(-t * 18.0)
        # Body tone
        tone = np.sin(2 * np.pi * 195.0 * t) * np.exp(-t * 22.0)
        snare = (noise * 0.75 + tone * 0.5) * volume
        audio[idx : idx + n] += snare

    # 3. FAST HI-HAT TICK
    def add_hihat(start_sec, open_hat=False, volume=0.35):
        idx = int(start_sec * sr)
        dur = 0.12 if open_hat else 0.04
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        decay = 18.0 if open_hat else 70.0
        hat = np.random.uniform(-1, 1, n) * np.exp(-t * decay)
        # High pass filter
        hat = hat - np.roll(hat, 1)
        audio[idx : idx + n] += hat * volume

    # 4. EPIC BRASS / SYNTH STAB (HYBRID TRAILER BRAAM)
    def add_braam(start_sec, freq=55.0, dur=1.8, volume=0.9):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        env = (1.0 - np.exp(-t * 40.0)) * np.exp(-t * 1.8)
        # Sawtooth + sub harmonics + distortion
        braam = (
            np.sin(2 * np.pi * freq * t) * 0.6 +
            np.sin(2 * np.pi * freq * 2.0 * t) * 0.4 +
            np.sin(2 * np.pi * freq * 3.0 * t) * 0.3 +
            np.sin(2 * np.pi * (freq * 0.5) * t) * 0.7
        )
        # Saturate
        braam = np.tanh(braam * 2.2) * env * volume
        audio[idx : idx + n] += braam

    # 5. RISER SWEEP
    def add_riser(start_sec, dur=2.5, volume=0.45):
        idx = int(start_sec * sr)
        n = int(dur * sr)
        if idx + n > total_samples:
            return
        t = np.linspace(0, dur, n, endpoint=False)
        f = np.linspace(150, 2400, n)
        phase = 2 * np.pi * np.cumsum(f) / sr
        env = (t / dur) ** 2.2
        noise = np.random.uniform(-0.5, 0.5, n) * env * 0.3
        sweep = (np.sin(phase) * 0.7 + noise) * env * volume
        audio[idx : idx + n] += sweep

    # 6. DRIVING BASSLINE ARPEGGIO (16th notes)
    def add_bass_arp(start_sec, dur_beats, root=55.0):
        sixteenth = beat_dur / 4.0
        n_steps = int(dur_beats * 4)
        notes = [root, root, root * 1.5, root, root * 1.33, root * 1.2, root, root * 2.0]
        for s in range(n_steps):
            t_start = start_sec + s * sixteenth
            idx = int(t_start * sr)
            note_dur = sixteenth * 0.8
            n = int(note_dur * sr)
            if idx + n > total_samples:
                break
            t = np.linspace(0, note_dur, n, endpoint=False)
            freq = notes[s % len(notes)]
            # Pluck envelope
            env = np.exp(-t * 22.0)
            tone = (np.sin(2 * np.pi * freq * t) + 0.4 * np.sin(4 * np.pi * freq * t)) * env
            audio[idx : idx + n] += tone * 0.45

    # ==========================================
    # ARRANGE 15-SECOND HIGH-ENERGY TIMELINE
    # ==========================================

    # --- BAR 1-2 (0.0s - 3.8s): RAPID INTRO & BUILDUP ---
    add_braam(0.02, freq=65.0, dur=1.8, volume=0.95)
    # Hi-hat 16th pattern driving from beat 1
    for s in range(16):
        add_hihat(s * (beat_dur / 2.0), open_hat=(s % 4 == 2), volume=0.3 + (s / 16.0) * 0.2)
    # 808 kicks on beat 1 and 3
    add_kick(0.0, punch=1.0)
    add_kick(beat_dur * 2.0, punch=0.9)
    add_kick(beat_dur * 3.0, punch=0.95)
    add_kick(beat_dur * 3.5, punch=0.95)
    # Fast snare roll into drop
    for b in range(4):
        add_snare(beat_dur * 3.0 + b * (beat_dur / 4.0), volume=0.4 + b * 0.2)
    add_riser(1.8, dur=2.0, volume=0.5)

    # --- BAR 3-6 (3.8s - 11.4s): MASSIVE FULL-ENERGY DROP & DRIVING BEATS ---
    drop_start = beat_dur * 4.0 # ~3.81s
    add_braam(drop_start, freq=55.0, dur=2.2, volume=1.0)
    
    # 4-on-the-floor heavy kicks + snares on 2 & 4
    for b in range(16):
        t_beat = drop_start + b * beat_dur
        if t_beat + 0.3 >= duration:
            break
        # Kick on every beat
        add_kick(t_beat, punch=1.1)
        # Snare on beats 2 and 4
        if b % 2 == 1:
            add_snare(t_beat, volume=1.0)
        # 16th hats
        for h in range(4):
            add_hihat(t_beat + h * (beat_dur / 4.0), open_hat=(h == 2), volume=0.35)

    # Driving Bassline Arpeggio
    add_bass_arp(drop_start, dur_beats=16, root=55.0)

    # Secondary impact braam at 7.6s (Bar 5)
    add_braam(drop_start + 8 * beat_dur, freq=73.42, dur=2.0, volume=0.95)
    add_riser(drop_start + 6 * beat_dur, dur=3.8, volume=0.55)

    # Pre-climax stutter roll (10.5s - 11.4s)
    for r in range(8):
        add_snare(drop_start + 14 * beat_dur + r * (beat_dur / 4.0), volume=0.5 + r * 0.08)
        add_kick(drop_start + 14 * beat_dur + r * (beat_dur / 4.0), punch=0.7 + r * 0.05)

    # --- BAR 7-8 (11.4s - 15.0s): MAXIMUM FINAL CLIMAX & SLAM ---
    climax_start = drop_start + 16 * beat_dur # ~11.43s
    add_braam(climax_start, freq=43.65, dur=3.4, volume=1.2) # Massive F1 Sub Drop
    add_kick(climax_start, punch=1.3)
    add_snare(climax_start, volume=1.1)

    # Final synchronized hits
    add_kick(climax_start + beat_dur * 1.5, punch=1.1)
    add_snare(climax_start + beat_dur * 1.5, volume=0.95)
    add_kick(climax_start + beat_dur * 2.5, punch=1.1)
    add_snare(climax_start + beat_dur * 2.5, volume=0.95)
    add_kick(climax_start + beat_dur * 3.5, punch=1.2)
    add_braam(climax_start + beat_dur * 3.5, freq=55.0, dur=2.0, volume=1.1)

    # Master Limiting & Aggressive Compression
    audio = np.tanh(audio * 1.35)
    max_amp = np.max(np.abs(audio))
    if max_amp > 0:
        audio = (audio / max_amp) * 0.96

    with wave.open(output_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        int_data = (audio * 32767).astype(np.int16)
        wf.writeframes(int_data.tobytes())

    print(f"High-Energy Soundtrack generated: {output_wav} ({duration}s @ {bpm} BPM)")

if __name__ == "__main__":
    create_high_energy_trailer_track()
