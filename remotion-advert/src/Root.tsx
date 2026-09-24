import React from 'react';
import { Composition } from 'remotion';
import { MainAdvert } from './Composition';

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* 16:9 Widescreen Cinema Commercial (1920x1080, 15 Seconds @ 30 FPS) */}
      <Composition
        id="IBNCommercialWidescreen"
        component={MainAdvert}
        durationInFrames={450} // 15 Seconds * 30 FPS
        fps={30}
        width={1920}
        height={1080}
      />

      {/* 9:16 Social Reel / Vertical Commercial (1080x1920, 15 Seconds @ 30 FPS) */}
      <Composition
        id="IBNCommercialReel"
        component={MainAdvert}
        durationInFrames={450}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
