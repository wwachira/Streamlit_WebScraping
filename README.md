### Learning outcomes
### Author: W. Wachira, Liz
Request a web page using Python’s built-in urllib module
Parse HTML using Beautiful Soup
Using Streamlit: Streamlit is an open-source Python framework designed for creating and deploying interactive web applications for data analysis and machine learning projects. 
Repeatedly request data from a website to check for updates
https://realpython.com/python-web-scraping-practical-introduction/ 
https://realpython.com/what-is-pip/
http://learn-co-curriculum.github.io/site-for-scraping/courses
https://datacamp.pxf.io/pythonology 

## PLEASE NOTE: <BEWARE>
Important: Most websites publish a Terms of Use document. You can often find a link to it in the website’s footer.
Failure to comply with the Terms of Use could result in your IP being blocked, so be careful!
With techniques like this, you can scrape data from websites that periodically update their data. However, you should be aware that requesting a page multiple times in rapid succession can be seen as suspicious, or even malicious, use of a website.

### wiki.py -installing libraries
python3 -m venv .venv
source .venv/bin/activate 
pip install pandas
pip install lxml

### st.py - installing libraries
in venv: pip install streamlit
 pip install requests
 pip install beautifulsoup4  -scrapes
 pip install pandas          -turn to csv file
pip install streamlit


 streamlit run st.py - http://localhost:8501/

