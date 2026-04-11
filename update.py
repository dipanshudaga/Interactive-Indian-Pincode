import csv
import struct
import base64
import json

CSV_PATH = "clean_pincodes.csv"
DATA_PATH = "data.js"

LAT_MIN, LAT_MAX = 6.0, 37.0
LON_MIN, LON_MAX = 68.0, 98.0

def process_data():
    pin_dict = {}
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pin = row['pincode']
            if not pin or len(pin) != 6: continue
            lat = float(row['lat'])
            lon = float(row['long'])
            office = row['officename'].replace('"', '\\"').replace("'", "\\'")
            if pin not in pin_dict: pin_dict[pin] = []
            pin_dict[pin].append((lat, lon, office))
    pincode_list = sorted(pin_dict.keys(), key=int)
    hubs = []
    pin_offices = {}
    for pin in pincode_list:
        children = pin_dict[pin]
        avg_lat = round(sum(c[0] for c in children) / len(children), 5)
        avg_lon = round(sum(c[1] for c in children) / len(children), 5)
        hubs.append({'pin': pin, 'lat': avg_lat, 'lon': avg_lon})
        pin_offices[pin] = children
    return hubs, pin_offices

def pack_data(points):
    N = len(points)
    pin_str = ''.join(p['pin'] for p in points)
    buf = bytearray(N * 4)  
    for i, p in enumerate(points):
        lat_norm = int((p['lat'] - LAT_MIN) / (LAT_MAX - LAT_MIN) * 65535)
        lon_norm = int((p['lon'] - LON_MIN) / (LON_MAX - LON_MIN) * 65535)
        lat_norm = max(0, min(65535, lat_norm))
        lon_norm = max(0, min(65535, lon_norm))
        struct.pack_into('<HH', buf, i * 4, lat_norm, lon_norm)
    coord_b64 = base64.b64encode(bytes(buf)).decode('ascii')
    return pin_str, coord_b64, N

def write_data_js(pin_str, coord_b64, N, pin_offices):
    data = {
        "COORD_B64": coord_b64,
        "ZIP_STR": pin_str,
        "N": N,
        "BOUNDS": {"LAT_MIN": LAT_MIN, "LAT_MAX": LAT_MAX, "LON_MIN": LON_MIN, "LON_MAX": LON_MAX},
        "PIN_OFFICES": pin_offices
    }
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        f.write(f"const MAP_DATA = {json.dumps(data)};")

def main():
    locations, pin_offices = process_data()
    pin_str, coord_b64, N = pack_data(locations)
    write_data_js(pin_str, coord_b64, N, pin_offices)
    print(f"✅ Data updated from {CSV_PATH} to {DATA_PATH}")

if __name__ == '__main__':
    main()
