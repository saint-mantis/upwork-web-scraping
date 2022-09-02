Scraping Data from Upwork 

 
 

Github Link - https://github.com/saint-mantis/upwork-web-scraping 

In the above Repository you can find 4 Files  

 	 

	1) chrome driver 

	2) requirements.txt 

	3) sample_output.csv 

	4) main.py 

 

 1.  Chrome Driver - Selenium requires chrome driver to scrap data.The Repository contains chrome 	 driver which works with Mac OS.You can download chrome driver according to your operating 	system from this link- https://chromedriver.chromium.org/downloads 

 

 2. Requirements.txt - which contains python packages.you can install packages in a virtual 		environment To Install follow below steps 

	A)  To Install virtualenv – pip install virtualenv 

	B)  virtualenv env 

	C)  Mac – source/env/bin/active 

	    Windows – env/Scripts/activate 

  D) After activating virtual environment run – “pip install –r requirements.txt” 

 

 3.  sample_output.csv - you can view sample output from the main.py in sample_output.csv. 

Outputs will be saved to this file by default. 

	 

 4. main.py - It contains the code to scrap data. you can find some variables below, change it       	a	accordingly 

	A) LINK – Link of the website 

	B) PATH_TO_OUTPUT_CSV_FILE – Path of the output csv file 

	C) EMAIL – Email for the login 

	D) PASSWORD – Password for the login 

	E) SECURITY_QUESTION – Security Question for the login 

	F) PATH_TO_CHROMEDRIVER – Path to the Chrome Driver 

 

   Run Script by – “python main.py” 

          Tip – RANDOMLY CHANGE MOUSE POINTER DURING THE LOGIN PROCESS OVER CHROMEDRIVE, SO THE PROGRAM WILL NOT BE RECOGNISED AS A BOT 
