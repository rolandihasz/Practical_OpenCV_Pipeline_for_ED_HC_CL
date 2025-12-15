<h1>Visibility Enhancer 1.0</h1>

A Practical, conservative OpenCV pipeline specifically tuned for (extremely dark, high-contrast, cinematic lighting) image types. 

The goal is visibility improvement without hallucination or noise explosion. It's not a filter, this is production-safe code. 

Sane(Specify‑And‑Edit) pipeline:
1. Convert to LAB or YCrCb
2. Work only on the luminance channel
3. Apply mild gamma correction (γ ≈ 0.85)
4. CLAHE with very conservative parameters
  clipLimit ≈ 1.5–2.0
  tileGridSize ≈ (8,8)
5. Optional bilateral filter (small radius)
6. Recombine channels

This improves visibility without lying about content.

Core principles behind the pipeline
  -Never touch RGB directly → work on luminance only
  -Lift midtones, not blacks
  -Local contrast, low clip limit
  -Very mild noise control
  -Preserve mood

Parameter guidance (important)

Gamma
  -0.80–0.90 → safe range
  -Lower than 0.8 → noise rises fast
  -Above 0.9 → barely visible change

CLAHE
  -clipLimit > 2.0 → halos + noise
  -tileGridSize < (8,8) → patchy contrast

Bilateral filter
  -Optional, but helps suppress shadow noise
  -Do not increase kernel size aggressively

Next: (Under Development)
An upgraded version with Automatic subject masking + new enhancement (Python / OpenCV)
