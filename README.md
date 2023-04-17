![img](https://github.com/msherrif04/harry_potter_network/blob/web_scraping/cover.gif)

# Analysis of networks in the harry potter universe

# Project Overview
The purpose of this project is to scrape data on the characters in the harry potter books and analyse the relationships and networks between the characters. 

## Methods Used
* Data scraping and colleciton
* Data cleaning
* Data Preparation
* Data visualisation
* Natural language processing

## Codes and Resources Used
- **Editor Used:**  Visual Studio Code
- **Python Version:** 3.11
- **Selenium:** 4.8.3

## Python Packages Used
This section contains all the necessary dependencies needed to reproduce this project

- **Data scraping:** `selenium, webdriver-manager`
- **Data Manipulation:** `pandas`
- **Data Visualization:** `matplotlib`
- **Natural Language processing:** `spacy.io`


# Data

## Source Data
- **Cover Image:** https://raw.githubusercontent.com/DLWAwesome/harry-potter-spells/master/2005874_200x130.gif
- **List of harry potter characters:** https://www.hp-lexicon.org/characters/
- **Harry Potter books:** https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter

## Data Preprocessing
Acquired data is not always squeaky clean, so preprocessing them are an integral part of any data analysis. In this section you can talk about the same.

# Code structure
Explain the code structure and how it is organized, including any significant files and their purposes. This will help others understand how to navigate your project and find specific components. 

Here is the basic suggested skeleton for your data science repo (you can structure your repository as needed ):

```bash
├── LICENSE
├── README.md        
├── data
│   ├── external       
│   ├── interim       
│   ├── processed      
│   └── raw                    
│
├── notebooks    
│
├── reports            
│   └── figures      
│
├── requirements.txt  
├── src                
│   ├── __init__.py    
│   │
│   ├── data           
│   │   └── make_dataset.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
```

# Results and evaluation
Provide an overview of the results of your project, including any relevant metrics and graphs. Include explanations of any evaluation methodologies and how they were used to assess the quality of the model. You can also make it appealing by including any pictures of your analysis or visualizations.

# Future work
Outline potential future work that can be done to extend the project or improve its functionality. This will help others understand the scope of your project and identify areas where they can contribute.

# Acknowledgments/References
* Idea by [Thu Vu](https://github.com/thu-vu92/the_witcher_network)


For instance, I am referencing the image that I used for my readme header - 
- Image by [rashadashurov](https://www.vectorstock.com/royalty-free-vector/data-science-cartoon-template-with-flat-elements-vector-27984292)

# License
Specify the license under which your code is released. Moreover, provide the licenses associated with the dataset you are using. This is important for others to know if they want to use or contribute to your project. 

For this github repository, the License used is [MIT License](https://opensource.org/license/mit/).