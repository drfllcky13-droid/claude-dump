"""Turn an unsuppressed gunshot into a suppressed one.

What a real suppressor does (CDC/NIOSH measurements, sound-design practice):
  - traps and slows the muzzle gas: the sharp, boomy blast becomes a rounder, quieter "thup"
  - less energy reaches the surroundings, so the echo/tail is much shorter
  - leaves the gun's action untouched, so slide/bolt clacks become audible
  - adds a short gas "pfft" as the gas leaves the baffles
  - does nothing to a supersonic bullet's crack (N-wave)
Usage: python3 suppress.py <in_dir> <out_dir>   (in_dir: <freesound id>.wav, mono 44.1 kHz; needs numpy + scipy)
"""
import sys, pathlib, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt, sosfiltfilt

SR = 44100

# Classes. att: dB taken off the blast transient. crack: N-wave length in ms (0 = subsonic).
# mech: (slide-back ms, slide-forward ms) after the shot, None for manual actions.
# level: dB relative to the unsuppressed shot. ponytail: hand-tuned by numbers, not by ear; tune here.
CLS = {
    "22":     dict(hold_ms=8, tau_ms=14, att=16, crack=0,    mech=(2, 28),  mech_db=-6,  hiss_ms=18, hiss_db=-20, level=-22),
    "pistol": dict(hold_ms=10, tau_ms=18, att=13, crack=0,    mech=(3, 38),  mech_db=-6,  hiss_ms=30, hiss_db=-17, level=-17),
    "45":     dict(hold_ms=10, tau_ms=18, att=14, crack=0,    mech=(3, 42),  mech_db=-6,  hiss_ms=34, hiss_db=-17, level=-18),
    "smg":    dict(hold_ms=10, tau_ms=16, att=13, crack=0,    mech=(2, 30),  mech_db=-4,  hiss_ms=28, hiss_db=-17, level=-15),
    "rifle":  dict(hold_ms=12, tau_ms=22, att=11, crack=0.25, mech=(3, 30),  mech_db=-9, hiss_ms=45, hiss_db=-16, level=-9),
    "762":    dict(hold_ms=12, tau_ms=24, att=11, crack=0.35, mech=(3, 34),  mech_db=-9, hiss_ms=50, hiss_db=-16, level=-8),
    "bolt":   dict(hold_ms=12, tau_ms=24, att=11, crack=0.3,  mech=None,     mech_db=0,   hiss_ms=50, hiss_db=-16, level=-8),
    "50":     dict(hold_ms=18, tau_ms=35, att=10, crack=0.6,  mech=None,     mech_db=0,   hiss_ms=70, hiss_db=-15, level=-6),
    "pump":   dict(hold_ms=14, tau_ms=28, att=8,  crack=0,    mech=None,     mech_db=0,   hiss_ms=55, hiss_db=-15, level=-9),
    "semi12": dict(hold_ms=14, tau_ms=28, att=8,  crack=0,    mech=(4, 45),  mech_db=-7,  hiss_ms=55, hiss_db=-15, level=-9),
}

# gun -> (source id, class, (trim start s, trim length s) or None)
GUNS = {
    "9mm":      (427592, "pistol", None),
    "police":   (828786, "pistol", None),
    "45":       (734062, "45", None),
    "22":       (865989, "22", None),
    "viper":    (865987, "pistol", None),
    "oldsmg":   (258198, "45", None),
    "compact":  (390663, "smg", None),
    "policesmg": (865993, "smg", None),
    "service":  (145206, "762", None),
    "tr15":     (427596, "rifle", None),
    "ak105":    (402791, "rifle", "auto4"),
    "carbine":  (865985, "rifle", None),
    "mk14":     (452154, "762", None),
    "military": (854507, "rifle", None),
    "tactical": (773873, "pump", None),
    "herrington": (773873, "semi12", None),
    "oryx":     (569309, "semi12", None),
    "hunting":  (452154, "bolt", None),
    "bolt":     (410442, "bolt", None),
    "light":    (855608, "bolt", None),
    "milsniper": (563015, "bolt", None),
    "heavy50":  (668071, "50", None),
}


def sos(kind, f, order=2):
    return butter(order, f, kind, fs=SR, output="sos")


def follow(x, att_ms, rel_ms):
    """Peak envelope follower with separate attack/release."""
    a, r = np.exp(-1 / (SR * att_ms / 1000)), np.exp(-1 / (SR * rel_ms / 1000))
    e, out, ax = 0.0, np.empty_like(x), np.abs(x)
    for i, v in enumerate(ax):
        c = a if v > e else r
        e = c * e + (1 - c) * v
        out[i] = e
    return out


def onsets(x, min_gap_ms=45, rel=0.3):
    """Shot starts: envelope crosses rel*max, at least min_gap apart."""
    e = follow(x, 0.2, 15)
    th, gap, out, last = rel * e.max(), int(SR * min_gap_ms / 1000), [], -10**9
    above = e > th
    for i in np.flatnonzero(above[1:] & ~above[:-1]) + 1:
        if i - last >= gap:
            out.append(i); last = i
    return out or [int(np.argmax(e))]


def shelf(x, f, db, kind):
    """Shelf as a crossover: split at f, scale one side."""
    lo = sosfiltfilt(sos("lowpass", f), x)
    hi = x - lo
    g = 10 ** (db / 20)
    return lo * g + hi if kind == "low" else lo + hi * g


def peak_eq(x, f, db, q=1.0):
    bw = f / q
    band = sosfiltfilt(sos("bandpass", [max(20, f - bw / 2), f + bw / 2]), x)
    return x + band * (10 ** (db / 20) - 1)


def burst_env(n, att_ms, tau_ms):
    t = np.arange(n) / SR * 1000
    return np.minimum(t / att_ms, 1) * np.exp(-t / tau_ms)


def click(rng, n_ms=30):
    """Metal-on-metal: noise tick plus a few short ringing modes."""
    n = int(SR * n_ms / 1000); t = np.arange(n) / SR
    tick = sosfilt(sos("highpass", 2500), rng.standard_normal(n)) * np.exp(-t / 0.0015)
    modes = sum(np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) * np.exp(-t / d)
                for f, d in zip(rng.uniform(1800, 6500, 4), rng.uniform(0.003, 0.012, 4)))
    c = tick / (np.abs(tick).max() + 1e-9) + 0.5 * modes / (np.abs(modes).max() + 1e-9)
    return c / np.abs(c).max()


def n_wave(ms):
    """Supersonic bullet crack: a straight pressure ramp from + to -, then a reflection off the ground."""
    n = max(4, int(SR * ms / 1000))
    w = np.zeros(int(SR * 0.012)); w[:n] = np.linspace(1, -1, n)
    w = sosfilt(sos("highpass", 700), w)
    refl = int(SR * 0.004)
    w[refl:] += 0.35 * sosfilt(sos("lowpass", 5000), w)[: len(w) - refl]
    return w / np.abs(w).max()


def place(dst, src, at, gain):
    end = min(len(dst), at + len(src))
    if at < end:
        dst[at:end] += src[: end - at] * gain


def suppress(x, p, seed):
    rng = np.random.default_rng(seed)
    peak0 = np.abs(x).max()
    ons = onsets(x)

    # 1. Blast: pull the fast transient down toward the slower envelope (rounder, softer attack).
    fast, slow = follow(x, 0.05, 6), follow(x, 6, 30)
    g = np.clip(slow / (fast + 1e-9), 10 ** (-p["att"] / 20), 1.0)
    y = x * g

    # 2. Tail: less gas reaches the air, so less echo. After each shot, hold briefly, then decay fast.
    #    (Real suppressed XM2010: -20 dB about 24 ms after the peak.)
    t = np.arange(len(y))
    last = np.maximum.accumulate(np.where(np.isin(t, ons), t, 0))
    since = (t - last) / SR * 1000
    gt = np.where(since < p["hold_ms"], 1.0, np.exp(-(since - p["hold_ms"]) / p["tau_ms"]))
    gt[: ons[0]] = 1.0
    y = y * np.maximum(gt, 10 ** (-45 / 20))

    # 3. Tone: the boom goes; the "thup" around 400 Hz stays. Real suppressed shots stay bright up top
    #    (gas, action, crack), so only a light high cut. The muffled movie sound is a myth.
    y = sosfiltfilt(sos("highpass", 110), y)
    y = shelf(y, 160, -10, "low")
    y = peak_eq(y, 420, 3.0, q=0.9)
    y = shelf(y, 4000, -3, "high")

    out = y / (np.abs(y).max() + 1e-9)
    hiss = None
    for i, o in enumerate(ons):
        lvl = 1.0 if i == 0 else 0.9
        # 4. Gas leaving the baffles: short band-limited hiss.
        n = int(SR * p["hiss_ms"] * 5 / 1000)
        hiss = sosfilt(sos("bandpass", [1500, 10000]), rng.standard_normal(n)) * burst_env(n, 0.6, p["hiss_ms"])
        place(out, hiss / np.abs(hiss).max(), o, lvl * 10 ** (p["hiss_db"] / 20))
        # 5. The action: slide/bolt back, then forward.
        if p["mech"]:
            back, fwd = p["mech"]
            place(out, click(rng), o + int(SR * back / 1000), lvl * 10 ** (p["mech_db"] / 20))
            place(out, click(rng), o + int(SR * fwd / 1000), lvl * 10 ** ((p["mech_db"] - 3) / 20))
        # 6. Supersonic crack is unaffected by the can: keep it sharp and loud.
        if p["crack"]:
            place(out, n_wave(p["crack"]), o, lvl * 0.9)

    out = out / (np.abs(out).max() + 1e-9) * peak0 * 10 ** (p["level"] / 20)
    return out


def load(path):
    sr, x = wavfile.read(path)
    assert sr == SR
    return x.astype(np.float64) / 32768.0


def main(in_dir, out_dir):
    in_dir, out_dir = pathlib.Path(in_dir), pathlib.Path(out_dir)
    out_dir.mkdir(exist_ok=True)
    for gun, (sid, cls, trim) in GUNS.items():
        x = load(in_dir / f"{sid}.wav")
        if trim == "auto4":  # long range recording: take 4 s from the first loud shot
            s = max(0, onsets(x, rel=0.5)[0] - int(0.05 * SR))
            x = x[s : s + 4 * SR]
        x = x / (np.abs(x).max() + 1e-9) * 0.89  # previews are normalized; keep a common reference
        y = suppress(x, CLS[cls], seed=sid)
        y = np.concatenate([y, np.zeros(int(0.05 * SR))])
        wavfile.write(out_dir / f"{gun}.wav", SR, (np.clip(y, -1, 1) * 32767).astype(np.int16))
        print(f"{gun:>11}  from {sid}  class {cls:<7} {len(y) / SR:5.2f}s  peak {20 * np.log10(np.abs(y).max()):6.1f} dBFS")


if __name__ == "__main__":
    main(*sys.argv[1:3])
