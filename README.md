# web-scraping-challenge
This project does web scraping of Mars related data from different websites and puts them together in a webpage.
It scrapes data using Splinter, BeautifulSoup, Pandas and Jupyter Notebook. A Python flask application is used to render the scraped data which is stored in MongoDB.<br><br>

Follwoing data are scraped from the respective sites.<br>
NASA Mars News - https://redplanetscience.com/<br>
JPL Mars Space Images - Featured Image - https://spaceimages-mars.com/<br>
Mars Facts - https://galaxyfacts-mars.com/<br>
Mars Hemispheres - https://marshemispheres.com/<br><br>

A flask application with a root route / will query the Mongo database and pass the mars data into an HTML template to display the data.<br>
The template HTML file called index.html will take the mars data dictionary and display all of the data in the appropriate HTML elements.<br>
A route called /scrape imports the scrape_mars.py script and calls scrape function. The scrape function does all the scraping from different sites and returns one Python dictionary containing all of the scraped data. 
The return value is stored in Mongo as a Python dictionary.<br>
/scrape route is redirected to the root route / and the page is updated with the scraped data.<br>

The html page looks as following.<br>
![Mars Image 1](Screenshots\Mission2Mars_1.png "Webpage screenshot")
![Mars Image 2](Screenshots\Mission2Mars_2.png "Webpage screenshot")