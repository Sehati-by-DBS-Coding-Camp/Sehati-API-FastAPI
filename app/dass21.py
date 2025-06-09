
def hitung_skala_dass21(depresi, kecemasan, stress):
    dass21_scale = {
    "Depresi": [(0, 9, "Normal"), (10, 13, "Ringan"), (14, 20, "Sedang"), (21, 27, "Berat"), (28, 100, "Sangat berat")],
    "Kecemasan": [(0, 7, "Normal"), (8, 9, "Ringan"), (10, 14, "Sedang"), (15, 19, "Berat"), (20, 100, "Sangat berat")],
    "Stres": [(0, 14, "Normal"), (15, 18, "Ringan"), (19, 25, "Sedang"), (26, 33, "Berat"), (34, 100, "Sangat berat")]
    }

    hasil_depresi = ""
    for min_val, max_val, kategori in dass21_scale["Depresi"]:
        if min_val <= depresi <= max_val:
            hasil_depresi = kategori
            break

    hasil_kecemasan = ""
    for min_val, max_val, kategori in dass21_scale["Kecemasan"]:
        if min_val <= kecemasan <= max_val:
            hasil_kecemasan = kategori
            break

    hasil_stres = ""
    for min_val, max_val, kategori in dass21_scale["Stres"]:
        if min_val <= stress <= max_val:
            hasil_stres = kategori
            break

    return {
        "Depresi": hasil_depresi,
        "Kecemasan": hasil_kecemasan,
        "Stres": hasil_stres
    }
    
def hitung_rata_rata_dass21(depresi, kecemasan, stress):
        total = depresi + kecemasan + stress
        rata_rata = total / 3  
        if rata_rata < 10:
            kategori = "Normal"
        elif rata_rata < 14:
            kategori = "Ringan"
        elif rata_rata < 20:
            kategori = "Sedang"
        elif rata_rata < 27:
            kategori = "Berat"
        else:
            kategori = "Sangat Berat"
    
        return kategori