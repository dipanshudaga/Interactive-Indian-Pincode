# 🗺️ Interactive Indian Pincode Map

> **Live Exploration**: [dipanshudaga.github.io/Interactive-Indian-Pincode](https://dipanshudaga.github.io/Interactive-Indian-Pincode/)

An interactive visualization of India's postal network, mapping over **165,000 pincodes**. Discover the density and distribution of post offices across the country through a fluid, responsive interface.

---

### 🚀 What You Can Do

*   **Fluid Navigation** – Zoom and pan smoothly across the entire map of India, from the Himalayas to Kanyakumari.
*   **Smart Search** – Instantly find a specific pincode or search for a post office by name.
*   **Deep Dive** – Click on any data point to see the specific names of all post offices associated with that pincode.
*   **Zone Insights** – The map is color-coded by India's postal zones, making the network's structure intuitive at a glance.

---

### 📦 The Data

The data is sourced from the [All India Pincode Directory](https://www.data.gov.in/catalog/all-india-pincode-directory-through-webservice).

#### How it stays fast:
To ensure the map stays responsive even with 165k+ points, I've implemented a few optimizations:
1.  **Hub Aggregation**: Post offices sharing a pincode are grouped into a single "pincode hub" with an averaged coordinate.
2.  **Binary Packing**: Coordinates are compressed into a small binary format, significantly reducing file size compared to raw JSON.
3.  **Client-Side Rendering**: Uses hardware-accelerated Canvas for buttery-smooth interaction.

---

### 🛠️ Running Locally

1.  **Clone & Open**: No server needed. Just clone the repo and open `index.html` in your browser.
2.  **Update Data**: 
    - Drop a new `pincodes.csv` into the root folder.
    - Run `python3 update.py` to regenerate the optimized `data.js`.

---

**Built with**: Vanilla JS • HTML5 • CSS3  
**Hosting**: GitHub Pages
