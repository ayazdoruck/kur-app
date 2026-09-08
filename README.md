# kur-app

Türkiye döviz ve altın kurlarını JSON olarak sunan küçük bir Flask servisi.
[truncgil Finans API](https://finans.truncgil.com/) verisini çekip tek bir uç
noktadan yeniden yayınlar — böylece ESP8266/ESP32 gibi TLS ve karmaşık başlık
yönetiminde zorlanan cihazlar da veriye erişebilir.

## Neden

Mikrodenetleyiciler üzerinde doğrudan üçüncü parti API çağırmak; sertifika
doğrulama, `User-Agent` zorunluluğu ve hata yönetimi yüzünden sorunlu. Bu
servis o işi üstlenip cihaza sade bir JSON döner.

## Uç noktalar

| Metot | Yol | Açıklama |
| --- | --- | --- |
| `GET` | `/kur` | Güncel kur verisini JSON olarak döner. Hata durumunda `{"error": "..."}` ve `500`. |

## Kurulum

```bash
git clone https://github.com/ayazdoruck/kur-app.git
cd kur-app
pip install -r requirements.txt
python server.py
```

Servis varsayılan olarak `http://0.0.0.0:10000` üzerinde çalışır. Port,
`PORT` ortam değişkeniyle değiştirilebilir — bu sayede Render, Railway gibi
platformlara ek yapılandırma olmadan dağıtılabilir.

## Örnek

```bash
curl http://localhost:10000/kur
```

## Teknolojiler

Python · Flask · requests

## Lisans

[MIT](LICENSE)
