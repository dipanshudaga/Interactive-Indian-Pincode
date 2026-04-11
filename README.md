<div align="center">
  <h1 align="center">Interactive Indian Pincode Map</h1>
  <p align="center">
    A fluid visualization of India's postal network mapping 165,000+ pincodes.
    <br />
    <a href="https://dipanshudaga.github.io/Interactive-Indian-Pincode/"><strong>Check out the live map »</strong></a>
  </p>
</div>

<br />

This is an interactive visualization of India's postal network. It maps over 165,000 pincodes across the country, letting you explore the density and distribution of post offices in a fluid, responsive interface.

## What you can do
- **Explore the map**: Zoom and pan smoothly across the entire country to see post office clusters.
- **Search anything**: Quickly find a specific pincode or search for a post office by name to see its exact location.
- **Toggle details**: Click on points to see the specific names of the post offices associated with that pincode.
- **See postal zones**: The map is color-coded by India's postal zones, making it easy to see how the network is structured.

## The Data
The data comes from the [All India Pincode Directory](https://www.data.gov.in/catalog/all-india-pincode-directory-through-webservice).

To keep things running fast in the browser, I did some basic cleanup:
- Grouped post offices by pincode and averaged their coordinates for a cleaner map.
- Compressed the coordinate data into a small binary format so the page loads quickly.
- Cleaned up names and removed any broken entries.

## Running it locally
1. Just clone the repo and open `index.html` in your browser. No server or dependencies needed.
2. If you want to update the data, just put a new `pincodes.csv` in the folder and run `python3 update.py`.

---
Built with vanilla JS, HTML, and CSS. Hosted on GitHub Pages.
