import cv2
import numpy as np

# Load image
img = cv2.imread("low_image_quality.png")
if img is None:
    raise ValueError("Image not found")

# Convert to LAB (L = luminance)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

# Normalize luminance to avoid banding
l = cv2.normalize(l, None, 0, 255, cv2.NORM_MINMAX)

# Gamma correction (lift midtones only)
gamma = 0.85  # < 1.0 brightens midtones
lut = np.array([((i / 255.0) ** gamma) * 255
                for i in range(256)]).astype("uint8")
l_gamma = cv2.LUT(l, lut)

# CLAHE (very conservative)
clahe = cv2.createCLAHE(
    clipLimit=1.7,
    tileGridSize=(8, 8)
)
l_clahe = clahe.apply(l_gamma)

# Optional: slight edge-preserving smoothing
l_smooth = cv2.bilateralFilter(
    l_clahe,
    d=5,
    sigmaColor=25,
    sigmaSpace=25
)

# Recombine channels
lab_enhanced = cv2.merge((l_smooth, a, b))
enhanced = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)

# Save result
cv2.imwrite("enhanced_output.png", enhanced)
