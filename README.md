# NASA API Client

A simple terminal-based NASA API client built with Python.

Fetches data like the Astronomy Picture of the Day (APOD) and displays it cleanly. This project is designed to make it easy to interact with NASA's public APIs.

> **NASA Open APIs** provide a huge range of data about planets, Earth, Mars rovers, satellites, asteroids, and more.  
> You can explore all available APIs here: [https://api.nasa.gov](https://api.nasa.gov)

---

## Requirements

- Python 3.8 or higher

### Python packages needed:
- `requests`
- `python-dotenv`

Install them using:
```
pip install requests python-dotenv
```

---

## Installation

Clone the repository:

```
git clone https://github.com/y-nabeelxd/NASA-API
```

Navigate into the project folder:

```
cd NASA-API
```

---

## How to Run

Simply run the `api.py` script:

```
python api.py
```

On the first run, the script will ask for your NASA API Key.  
You can obtain a free API key from [https://api.nasa.gov](https://api.nasa.gov).

The API key will be saved automatically for future runs inside a `.env` file.

---

## Note

This project is currently set up to fetch data from the **Astronomy Picture of the Day (APOD)** API.  
You can modify `api.py` to use different endpoints by checking NASA's official documentation.

More APIs can be found at: [https://api.nasa.gov](https://api.nasa.gov)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

[**y-nabeelxd**](https://github.com/y-nabeelxd)  
Repository: [NASA-API](https://github.com/y-nabeelxd/NASA-API)
