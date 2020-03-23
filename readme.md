# Python program that parse ad from site 'olx.ua' by search link
`Use for run:`

    - python v.3.8.1
    - scrapy v.2.0.1
    - fake-useragent v.0.1.11
    - twisted v.20.3.0
 
 `Description:`
 
 1. Create new directory to this project and nev virtual environment on it:
 
    _python -m venv env_
  
 2. Run virtual environment:
  
    _env\Scripts\activate_
  
 3. Download Twisted library for Scrapy:
 
    _https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted_
    
    in this project used Twisted‑20.3.0‑cp38‑cp38‑win32.whl

 4. Install Twisted‑20.3.0‑cp38‑cp38‑win32.whl library:
 
    _pip install twisted‑20.3.0‑cp38‑cp38‑win32.whl_
 
 5. Get project files from 'GitHub.com':
    
    _git clone https://github.com/rybaprm/OlxScrapy_ 
 
 6. Install all requirements:
 
    _pip install -r requirements.txt_

 6. For parse ad from site 'olx.ua' by search link run in terminal with
  activated virtual environment 'env' spider 'olx_scrapy_spider':
    
    _scrapy crawl olx_scrapy_spider -o olx.csv_

 7. After successful execution of the program we get file 'olx.csv' with
 parsing result.