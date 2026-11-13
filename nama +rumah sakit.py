daftar_pasien = [
    {"nama": "Budi Santoso", "kasus": "Demam Berdarah (DBD)", "suhu": 39.2, "lama_inap": 5, "jaminan": "BPJS"},
    {"nama": "Siti Aminah", "kasus": "Pasca Operasi Caesar", "suhu": 36.8, "lama_inap": 3, "jaminan": "Asuransi Swasta"},
    {"nama": "Andi Wijaya", "kasus": "Tifus (Tipes)", "suhu": 38.5, "lama_inap": 6, "jaminan": "BPJS"},
    {"nama": "Rina Marlina", "kasus": "Pneumonia", "suhu": 37.8, "lama_inap": 9, "jaminan": "BPJS"},
    {"nama": "Dedi Kurniawan", "kasus": "Patah Tulang (Ortopedi)", "suhu": 36.5, "lama_inap": 10, "jaminan": "Mandiri"},
    {"nama": "Maya Sari", "kasus": "Usus Buntu", "suhu": 37.0, "lama_inap": 4, "jaminan": "BPJS"},
    {"nama": "Joko Susilo", "kasus": "Stroke Ringan", "suhu": 36.7, "lama_inap": 12, "jaminan": "BPJS"},
    {"nama": "Lestari Putri", "kasus": "Diare Akut & Dehidrasi", "suhu": 37.5, "lama_inap": 2, "jaminan": "Mandiri"},
    {"nama": "Hendra Gunawan", "kasus": "Serangan Jantung (ICCU)", "suhu": 35.8, "lama_inap": 8, "jaminan": "Asuransi Swasta"},
    {"nama": "Nadia Safitri", "kasus": "Asma Akut", "suhu": 36.9, "lama_inap": 3, "jaminan": "BPJS"}
]

print("=== SISTEM MONITORING PASIEN RAWAT INAP (OPNAME) ===\n")

for pasien in daftar_pasien:
    nama = pasien["nama"]
    kasus = pasien["kasus"]
    suhu = pasien["suhu"]
    hari = pasien["lama_inap"]
    jaminan = pasien["jaminan"]

    if suhu >= 38.0:
        kondisi_suhu = "Demam Tinggi (Waspada)"
    elif suhu > 37.2:
        kondisi_suhu = "Demam Ringan"
    elif suhu < 36.0:
        kondisi_suhu = "Hipotermia (Suhu Rendah)"
    else:
        kondisi_suhu = "Normal"

    if hari > 7:
        ket_inap = "Perawatan Jangka Panjang (> 1 Minggu)"
    else:
        ket_inap = "Perawatan Standar"

    if jaminan != "BPJS":
        info_biaya = f"Non-BPJS ({jaminan}) - Verifikasi Administrasi"
    else:
        info_biaya = "Ditanggung BPJS Kesehatan"

    print(f"Pasien     : {nama} | Kasus: {kasus}")
    print(f"Suhu Tubuh : {suhu}°C -> Kondisi: {kondisi_suhu}")
    print(f"Lama Inap  : {hari} hari -> {ket_inap}")
    print(f"Pembiayaan : {info_biaya}")
    print("-" * 55)
