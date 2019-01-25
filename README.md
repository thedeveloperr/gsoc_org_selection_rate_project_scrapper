Scrapped the gsoc website and counted the projects/students accepted by organisation yearwise.

### **To replicate follow the steps below:**

- Install the requirements from req.txt using
  ```
  pip install -r req.txt
  ```
- Run collect.py to scrape data from year 2016 to 2018
  ```
  python3 collect.py 2016 2018
  ```
  or if your default python points to python 3 you can run
  ```
  python collect.py 2016 2018
  ```
  You can run from 2017 to 2018 or 2016 to 2017 too.
- You will have a json file called data.json after this. Now run workon.py to convert that json to csv. 
  ```
  python3 workon.py
  ```
  or if your default python points to python 3 you can run
  ```
  python workon.py
  ```
- The workon.py just takes the raw json and sums the number of projects from given start year to end year and outputs it in csv. If you will open the file you can notice that it just use pandas to do it. I planned to use pandas to plot data but data was too large to fit in figure. So just used it to output csv, you are more than welcomed to play with the data.
- Accuracy have not been extensively tested. Few Random tests. Some of organisation worked on same project but changed their org name like mit app inventor, there might be more such cases.
- Based on projects listed on gsoc website, so accuracy subject to accuracy of the list.
