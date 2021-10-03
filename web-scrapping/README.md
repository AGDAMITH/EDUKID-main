## Web Scrapping

#### Sources
    YouTube
    KhanAcademy
  
#### Technologies Used
    Firestore
    Firestire Admin
    BeautifulSoup 4.0
    Requests 2.22.0
    selenium
    wxPython
    
#### How to set up ?
##### Create Python Virtual environment
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    
##### Install Required libraries
    pip install -r requirements.txt
    pip install --upgrade firebase-admin
    

##### Setup Selenium on PC

First go to - [About Chrome](chrome://settings/help) and check your version  -  chrome://settings/help
Download [Selenium driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that is matched with your chrome version

###### Windows
    1. Unzip the donwloaded file
    2. include the ChromeDriver location in your PATH environment variable
    3. include the path to ChromeDriver in config file
    4. Set OS as WINDOWS in config file
    
###### Mac or Linux
    1. Unzip the donwloaded file
    2. move the ChromeDriver to /usr/local/bin
    3. Set OS as WINDOWS in config file


##### If you are facing any security issue to run chromedriver execute following command
    xattr -d com.apple.quarantine /usr/local/bin/chromedriver
    
    
##### To Run
    pythonw main.py | python main.py | python3.py
