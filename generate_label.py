from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter
import os

# === INPUT DARI USER ===
nama_barang = input("Masukkan Nama Barang: ").strip().upper()
kode_barang = input("Masukkan Kode Barang: ").strip().upper()
bin_location = input("Masukkan Bin Location (boleh kosong): ").strip().upper()

# Ukuran gambar (10x6 cm @ 300dpi)
dpi = 300
width_px = int(10 * dpi / 2.54)
height_px = int(6 * dpi / 2.54)

# Buat canvas putih
img = Image.new("RGB", (width_px, height_px), "white")
draw = ImageDraw.Draw(img)

# Load font
try:
    font_bold = ImageFont.truetype("arialbd.ttf", 36)
    font_regular = ImageFont.truetype("arial.ttf", 30)
except:
    font_bold = font_regular = ImageFont.load_default()

# === HEADER BIRU DENGAN NAMA BARANG ===
margin = 10
header_height = 100
draw.rectangle([(margin, margin), (width_px - margin, header_height)], fill="royalblue")
draw.text(((width_px) // 2, (margin + header_height) // 2), nama_barang, font=font_bold, fill="white", anchor="mm")

# === KODE ITEM DENGAN BACKGROUND ORANGE ===
kode_text = f"Kode: {kode_barang}"
text_size = draw.textbbox((0, 0), kode_text, font=font_bold)
text_width = text_size[2] - text_size[0]
text_height = text_size[3] - text_size[1]

kode_x = margin + 60
kode_y = header_height + 40
padding = 20

# Kotak oranye belakang teks kode
draw.rectangle(
    [(kode_x - padding, kode_y - padding),
     (kode_x + text_width + padding, kode_y + text_height + padding)],
    fill="orange"
)
draw.text((kode_x, kode_y), kode_text, font=font_bold, fill="black")

# === BIN LOCATION DENGAN BACKGROUND ORANGE ===
if bin_location:
    box_x1 = width_px - 250
    box_x2 = width_px - 50
    box_y1 = header_height + 20
    box_y2 = box_y1 + 60
    draw.rectangle([(box_x1, box_y1), (box_x2, box_y2)], fill="orange")
    draw.text(((box_x1 + box_x2) // 2, box_y1 + 30), bin_location, font=font_bold, fill="black", anchor="mm")

# === BARCODE TANPA TEKS BAWAH ===
EAN = barcode.get_barcode_class("code128")
ean = EAN(kode_barang, writer=ImageWriter())
barcode_path = ean.save("temp_barcode", options={"write_text": False})

# Tempel barcode, resize lebih tinggi
barcode_img = Image.open("temp_barcode.png").resize((width_px - 100, 380))
img.paste(barcode_img, (60, header_height + 160))

# === BORDER HITAM ===
border_margin = 5
draw.rectangle(
    [(border_margin, border_margin), (width_px - border_margin, height_px - border_margin)],
    outline="black", width=3
)

# Simpan hasil
output_filename = f"{kode_barang}.jpg"
img.save(output_filename, dpi=(dpi, dpi))
print(f"\n✅ Label berhasil dibuat: {output_filename}")

# Bersihin file barcode sementara
os.remove("temp_barcode.png")
