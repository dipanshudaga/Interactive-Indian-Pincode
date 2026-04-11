# Interactive Indian Pincode Map

A high-performance, interactive visualization of India's postal network, mapping over 165,000 pincode locations with fluid responsiveness and detailed site-level data.

## Data Source

The data used in this project is sourced from the **All India Pincode Directory** provided by the Government of India.
- **Source URL:** [data.gov.in - All India Pincode Directory](https://www.data.gov.in/catalog/all-india-pincode-directory-through-webservice)

## Data Processing & Cleanup

To ensure high performance and smooth rendering of large datasets in the browser, a custom processing pipeline was implemented (`update.py`):

1.  **Filtering & Validation**: The raw dataset was filtered to ensure only valid 6-digit pincodes with associated coordinates were included.
2.  **Aggregation**: Multiple post offices sharing the same pincode were aggregated into a single "pincode hub." The central coordinate for each hub is calculated as the average latitude and longitude of its constituent offices.
3.  **Coordinate Compression**: To minimize file size, coordinates were normalized to a specific bounding box (Lat: 6.0–37.0, Lon: 68.0–98.0) and packed into 16-bit integers.
4.  **Binary Serialization**: The processed coordinate data is stored as a Base64-encoded string (`data.js`), which is decoded on the fly by the client. This significantly reduces the payload size compared to standard JSON.
5.  **Sanitization**: Office names and associated metadata were sanitized to handle special characters and escape sequence issues during JSON serialization.

## Key Features

- **Fluid Performance**: Leverages Canvas rendering to handle 165k+ points without UI lag.
- **Dynamic Search**: Real-time filtering by pincode or office name.
- **Postal Zone Visualization**: Color-coded visualization based on India's postal zones.
- **Lightweight**: Zero dependencies; built with vanilla HTML, CSS, and JavaScript.

## Setup

1.  Clone the repository.
2.  Open `index.html` in a modern web browser.
3.  To update the data, place a new `pincodes.csv` in the root and run `python3 update.py`.

## License

This project is open-source. Please attribute the data source to data.gov.in as per their usage policy.
