import os
from PIL import Image, ImageDraw, ImageFont

def make_icon_badges():
    os.makedirs('presentation_assets/badges', exist_ok=True)
    size = 256
    
    badges = {
        'shield_security': ('SECURITY', 'PARLIAMENT PROTOCOL', '#D4AF37'),
        'mobile_wallet': ('WALLET', 'DIGITAL PASS', '#F3E5AB'),
        'coach_transit': ('TRANSIT', 'OXFORD & CAMBRIDGE', '#D4AF37'),
        'payment_card': ('BILLING', 'MULTI-CURRENCY B2B', '#F3E5AB'),
        'match_meeting': ('NETWORK', '1-ON-1 BILATERAL', '#D4AF37'),
        'ai_camera': ('AI PHOTO', 'FACIAL RECOGNITION', '#F3E5AB'),
        'scanner_gate': ('SCANNER', '<2S GATE CHECK-IN', '#D4AF37'),
        'visa_vault': ('VAULT', 'UK VISA & HOTELS', '#F3E5AB'),
        'executive_vip': ('C-SUITE', '100 GLOBAL LEADERS', '#D4AF37'),
        'architecture_hub': ('SYSTEM', '4-TIER ARCHITECTURE', '#F3E5AB')
    }

    for name, (top_text, bottom_text, accent_color) in badges.items():
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Outer ring
        draw.ellipse([8, 8, size-8, size-8], fill='#0C1C36', outline=accent_color, width=4)
        # Inner ring
        draw.ellipse([20, 20, size-20, size-20], outline='#1E3A5F', width=2)

        # Center emblem: star/diamond polygon
        cx, cy = size // 2, size // 2
        r = 32
        poly = [(cx, cy - r), (cx + r*0.7, cy), (cx, cy + r), (cx - r*0.7, cy)]
        draw.polygon(poly, fill=accent_color)
        
        # Center inner dot
        draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill='#061226')

        img.save(f'presentation_assets/badges/{name}.png')

    print('Icon badges generated successfully.')

if __name__ == '__main__':
    make_icon_badges()
