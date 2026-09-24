import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Sequence
} from 'remotion';

export const MainAdvert: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();

  // Background slow zoom
  const bgScale = interpolate(frame, [0, 450], [1.0, 1.15], {
    extrapolateRight: 'clamp'
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#020713',
        fontFamily: "'Cinzel', Georgia, serif",
        overflow: 'hidden',
        color: '#ffffff'
      }}
    >
      {/* Background Atmosphere */}
      <AbsoluteFill
        style={{
          transform: `scale(${bgScale})`,
          background: 'radial-gradient(circle at 60% 30%, #163668 0%, #061226 70%, #020713 100%)',
          opacity: 0.85
        }}
      />

      {/* Cinematic Vignette */}
      <AbsoluteFill
        style={{
          background: 'radial-gradient(circle at 50% 50%, transparent 40%, rgba(2,7,19,0.8) 85%, #020713 100%)',
          pointerEvents: 'none'
        }}
      />

      {/* ========================================================= */}
      {/* SCENE 1: 0.0s - 3.8s (Frames 0 - 114) — LOGO & OPENING */}
      {/* ========================================================= */}
      <Sequence from={0} durationInFrames={114}>
        <Scene1Opening frame={frame} fps={fps} />
      </Sequence>

      {/* ========================================================= */}
      {/* SCENE 2: 3.8s - 7.5s (Frames 114 - 225) — VENUE & TITLES */}
      {/* ========================================================= */}
      <Sequence from={114} durationInFrames={111}>
        <Scene2VenueTitle frame={frame - 114} fps={fps} />
      </Sequence>

      {/* ========================================================= */}
      {/* SCENE 3: 7.5s - 11.5s (Frames 225 - 345) — 5-DAY PACKAGES */}
      {/* ========================================================= */}
      <Sequence from={225} durationInFrames={120}>
        <Scene3Packages frame={frame - 225} fps={fps} />
      </Sequence>

      {/* ========================================================= */}
      {/* SCENE 4: 11.5s - 15.0s (Frames 345 - 450) — CLIMAX & CTA */}
      {/* ========================================================= */}
      <Sequence from={345} durationInFrames={105}>
        <Scene4CTA frame={frame - 345} fps={fps} />
      </Sequence>
    </AbsoluteFill>
  );
};

// -------------------------------------------------------------
// Scene 1: Opening & Animated Lotus Blossom
// -------------------------------------------------------------
const Scene1Opening: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const opacity = interpolate(frame, [0, 15], [0, 1]) * interpolate(frame, [95, 114], [1, 0]);
  const logoScale = spring({
    frame: frame - 5,
    fps,
    config: { damping: 12, stiffness: 100 }
  });

  const kickerOpacity = interpolate(frame, [25, 45], [0, 1]);
  const textY = interpolate(frame, [30, 60], [30, 0]);

  return (
    <AbsoluteFill
      style={{
        opacity,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: '60px'
      }}
    >
      <div style={{ transform: `scale(${logoScale})`, marginBottom: 30 }}>
        {/* Animated Lotus Graphic */}
        <svg viewBox="0 0 200 160" width="180" height="140">
          <ellipse cx="100" cy="120" rx="35" ry="6" fill="#d4af37" />
          <path d="M100 15 C85 55, 85 95, 100 115 C115 95, 115 55, 100 15 Z" fill="#2563eb" />
          <path d="M100 115 C80 90, 60 70, 50 45 C75 55, 95 85, 100 115 Z" fill="#dc2626" />
          <path d="M100 115 C75 105, 45 90, 25 75 C55 85, 85 105, 100 115 Z" fill="#e11d48" />
          <path d="M100 115 C120 90, 140 70, 150 45 C125 55, 105 85, 100 115 Z" fill="#0284c7" />
          <path d="M100 115 C125 105, 155 90, 175 75 C145 85, 115 105, 100 115 Z" fill="#0d9488" />
        </svg>
      </div>

      <div
        style={{
          opacity: kickerOpacity,
          color: '#d4af37',
          fontSize: '1.4rem',
          letterSpacing: 6,
          fontWeight: 700,
          marginBottom: 16
        }}
      >
        INDIAN BUSINESS NETWORK PRESENTS
      </div>

      <h1
        style={{
          transform: `translateY(${textY}px)`,
          fontSize: '3.8rem',
          fontWeight: 900,
          background: 'linear-gradient(135deg, #fff 30%, #f5e6b3 70%, #d4af37 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          lineHeight: 1.15
        }}
      >
        AN UNPRECEDENTED<br />GLOBAL GATHERING
      </h1>
    </AbsoluteFill>
  );
};

// -------------------------------------------------------------
// Scene 2: Venue Prestige & Titles
// -------------------------------------------------------------
const Scene2VenueTitle: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const opacity = interpolate(frame, [0, 15], [0, 1]) * interpolate(frame, [95, 111], [1, 0]);
  const scale = interpolate(frame, [0, 111], [0.95, 1.05]);

  return (
    <AbsoluteFill
      style={{
        opacity,
        transform: `scale(${scale})`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: '60px'
      }}
    >
      <div
        style={{
          background: 'rgba(12, 28, 54, 0.9)',
          border: '1px solid #d4af37',
          padding: '12px 36px',
          borderRadius: 50,
          color: '#f3e5ab',
          fontSize: '1.2rem',
          fontWeight: 700,
          marginBottom: 25,
          letterSpacing: 2
        }}
      >
        🔒 INVITATION ONLY • STRICTLY 100 DISTINGUISHED GUESTS
      </div>

      <h1
        style={{
          fontSize: '4.5rem',
          fontWeight: 900,
          background: 'linear-gradient(135deg, #fff 30%, #f5e6b3 70%, #d4af37 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent',
          lineHeight: 1.1,
          marginBottom: 25
        }}
      >
        GLOBAL INDIAN<br />BUSINESS EXCELLENCE<br />AWARDS 2026
      </h1>

      <div style={{ display: 'flex', gap: 30, fontSize: '1.8rem', color: '#f3e5ab', fontWeight: 700 }}>
        <span>🏛️ HOUSE OF COMMONS, BRITISH PARLIAMENT</span>
        <span>•</span>
        <span>📅 5 – 9 NOVEMBER 2026</span>
      </div>
    </AbsoluteFill>
  );
};

// -------------------------------------------------------------
// Scene 3: Packages & Academic Powerhouses
// -------------------------------------------------------------
const Scene3Packages: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const opacity = interpolate(frame, [0, 15], [0, 1]) * interpolate(frame, [100, 120], [1, 0]);

  return (
    <AbsoluteFill
      style={{
        opacity,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: '60px'
      }}
    >
      <div style={{ color: '#d4af37', fontSize: '1.3rem', letterSpacing: 5, fontWeight: 700, marginBottom: 12 }}>
        CHOOSE YOUR EXPERIENCE
      </div>

      <h2 style={{ fontSize: '3rem', fontWeight: 800, color: '#fff', marginBottom: 35 }}>
        WESTMINSTER • OXFORD • CAMBRIDGE
      </h2>

      <div style={{ display: 'flex', gap: 24, width: '100%', maxWidth: 1200, justifyContent: 'center' }}>
        <div style={{ flex: 1, background: 'rgba(12, 28, 54, 0.9)', border: '1px solid #1e3a5f', borderRadius: 12, padding: 30 }}>
          <div style={{ fontSize: '1.4rem', color: '#fff', fontWeight: 800, marginBottom: 8 }}>DINNER PASS</div>
          <div style={{ fontSize: '2.5rem', color: '#d4af37', fontWeight: 900 }}>£750</div>
          <p style={{ color: '#94a3b8', fontSize: '1rem', marginTop: 10 }}>Black Tie Gala Dinner (6 Nov) & Networking</p>
        </div>

        <div style={{ flex: 1, background: 'rgba(12, 28, 54, 0.9)', border: '1px solid #1e3a5f', borderRadius: 12, padding: 30 }}>
          <div style={{ fontSize: '1.4rem', color: '#fff', fontWeight: 800, marginBottom: 8 }}>OXFORD & DINNER</div>
          <div style={{ fontSize: '2.5rem', color: '#d4af37', fontWeight: 900 }}>£1,000</div>
          <p style={{ color: '#94a3b8', fontSize: '1rem', marginTop: 10 }}>Gala Dinner + Oxford Leadership Forum</p>
        </div>

        <div style={{ flex: 1.15, background: 'rgba(12, 28, 54, 0.95)', border: '2px solid #d4af37', borderRadius: 12, padding: 30, boxShadow: '0 0 35px rgba(212,175,55,0.3)' }}>
          <div style={{ color: '#d4af37', fontSize: '0.9rem', fontWeight: 800, letterSpacing: 2, marginBottom: 6 }}>★ BEST VALUE</div>
          <div style={{ fontSize: '1.4rem', color: '#f3e5ab', fontWeight: 800, marginBottom: 8 }}>5-DAY MASTER PASS</div>
          <div style={{ fontSize: '2.8rem', color: '#d4af37', fontWeight: 900 }}>£1,500</div>
          <p style={{ color: '#cbd5e1', fontSize: '1rem', marginTop: 10 }}>Gala + Oxford + Cambridge + Imperial College</p>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// -------------------------------------------------------------
// Scene 4: Climax & Call to Action
// -------------------------------------------------------------
const Scene4CTA: React.FC<{ frame: number; fps: number }> = ({ frame, fps }) => {
  const opacity = interpolate(frame, [0, 15], [0, 1]);

  return (
    <AbsoluteFill
      style={{
        opacity,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        textAlign: 'center',
        padding: '60px'
      }}
    >
      <div style={{ background: 'rgba(220, 38, 38, 0.2)', border: '1px solid #ef4444', color: '#fca5a5', padding: '10px 30px', borderRadius: 50, fontSize: '1.1rem', fontWeight: 700, marginBottom: 20 }}>
        ⚠️ STRICTLY 100 SEATS — INVITATION ONLY
      </div>

      <h1 style={{ fontSize: '4.2rem', fontWeight: 900, color: '#fff', marginBottom: 25 }}>
        RESERVE YOUR PRESENCE
      </h1>

      <div style={{ background: 'rgba(12, 28, 54, 0.95)', border: '2px solid #d4af37', borderRadius: 16, padding: '24px 60px', boxShadow: '0 0 45px rgba(212, 175, 55, 0.4)', marginBottom: 25 }}>
        <div style={{ color: '#94a3b8', fontSize: '1.1rem', marginBottom: 6 }}>Official Delegate Registration:</div>
        <div style={{ fontSize: '2.2rem', color: '#d4af37', fontWeight: 900, letterSpacing: 2 }}>
          https://tally.so/r/NpzrWj
        </div>
      </div>

      <div style={{ fontSize: '1.3rem', color: '#cbd5e1' }}>
        Enquiries: Subha Austalekshmi (+44 7587 260254) | events@ibnonline.co.uk
      </div>

      <div style={{ color: '#d4af37', letterSpacing: 4, marginTop: 30, fontSize: '1rem', fontWeight: 700 }}>
        INDIAN BUSINESS NETWORK | CONNECT • COLLABORATE • INSPIRE
      </div>
    </AbsoluteFill>
  );
};
