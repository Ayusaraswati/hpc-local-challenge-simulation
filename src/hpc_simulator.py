import time
import multiprocessing
from multiprocessing import Pool
import numpy as np

def simulate_evacuation_zone(zone_data):
    """
    Fungsi simulasi untuk satu zona wilayah (dijalankan secara paralel).
    Menghitung estimasi beban/waktu evakuasi berdasarkan populasi dan variabel hambatan.
    """
    zone_id, population, obstacle_factor = zone_data
    
    start_time = time.time()
    np.random.seed(zone_id)
    
    # Matriks komputasi matematis intensif (meniru kalkulasi beban HPC)
    sim_matrix = np.random.rand(1000, 1000) * obstacle_factor
    processed_val = np.sum(np.sin(sim_matrix) * population)
    
    execution_time = time.time() - start_time
    
    return {
        "zone_id": zone_id,
        "population": population,
        "processed_score": float(processed_val),
        "computation_time_sec": round(execution_time, 4)
    }

def main():
    print("=== HPC Local Challenge Simulation: Evacuation Model ===")
    
    # Data sampel zona (ID Zona, Jumlah Populasi, Faktor Hambatan Jalan)
    zones = [
        (1, 4500, 1.2),
        (2, 3200, 0.9),
        (3, 7800, 1.5),
        (4, 5100, 1.1),
        (5, 6200, 1.3),
        (6, 2900, 0.8)
    ]
    
    print(f"[*] Memulai pemrosesan paralel untuk {len(zones)} zona menggunakan {multiprocessing.cpu_count()} Core CPU...")
    
    start_total = time.time()
    # Pemrosesan paralel menggunakan multiprocessing Pool
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(simulate_evacuation_zone, zones)
    total_time = time.time() - start_total
    
    print("\n--- Hasil Simulasi ---")
    for res in results:
        print(f"Zona {res['zone_id']} | Populasi: {res['population']} | Skor Risiko: {res['processed_score']:.2f} | Waktu: {res['computation_time_sec']}s")
    
    print(f"\n[✓] Total Waktu Eksekusi Paralel: {total_time:.4f} detik")

if __name__ == "__main__":
    main()
