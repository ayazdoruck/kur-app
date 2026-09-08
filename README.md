# kur-app

A small Flask service that exposes live Turkish exchange and gold rates as JSON.
It fetches data from the [truncgil Finans API](https://finans.truncgil.com/) and
re-publishes it through a single endpoint, so devices like the ESP8266/ESP32 —
which struggle with TLS and header requirements — can consume it easily.

## Why

Calling a third-party API directly from a microcontroller is painful:
certificate validation, a mandatory `User-Agent`, and error handling all get in
the way. This service takes care of that and returns plain JSON to the device.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/kur` | Returns the current rates as JSON. On failure, responds with `{"error": "..."}` and status `500`. |

## Getting started

```bash
git clone https://github.com/ayazdoruck/kur-app.git
cd kur-app
pip install -r requirements.txt
python server.py
```

The service listens on `http://0.0.0.0:10000` by default. The port can be
overridden with the `PORT` environment variable, which makes it deployable to
Render, Railway and similar platforms without extra configuration.

## Example

```bash
curl http://localhost:10000/kur
```

## Built with

Python · Flask · requests

## License

[MIT](LICENSE)
