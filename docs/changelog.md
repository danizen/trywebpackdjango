- 11/02/16 gehrigdg -- updated `moviedb\data\moviedb.json` timestamps to work with `USE_TZ=False` in sqlite3
- 10/27/16 gehrigdg -- changed `USE_TZ` to `False` in `base.py`. This means that all dates stored in Oracle will be interpreted as being in the Eastern time zone. When `USE_TZ == True`, Django converts times to `UTC` before storing them and translates them back to our time zone on retrieval.  
- 10/13/16 gehrigdg -- added  `CSRF_COOKIE_HTTPONLY` and `CSRF_COOKIE_SECURE` settings to `dev_oracle.py` and `dev_sqlite3.py`. This addresses an issue with forms submissions failing on the desktop, which is served through `HTTP`, rather  than the  servers, which run `HTTPS`.

