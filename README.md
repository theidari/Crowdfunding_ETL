<p align="center">
<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/asset/header.png" width="900px">
</p>

<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/asset/space_label.png" width="30px"> Crowdfunding platforms like [Kickstarter](https://www.kickstarter.com) and [Indiegogo](https://www.indiegogo.com/) have been growing in success and popularity since the late 2000s. From independent content creators to famous celebrities, more and more people are using crowdfunding to launch new products and generate buzz, but not every project has found success.
To receive funding, the project must meet or exceed an initial goal, so many organizations dedicate considerable resources looking through old projects in an attempt to discover “the trick” to finding success.

<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/asset/space_label.png" width="30px"> <b>Project Overview</b></br>
- <b>Objective:</b>The instructions for this project are divided into the following subsections:
  - [x] Create the Category and Subcategory DataFrames
  - [x] Create the Campaign DataFrame
  - [x] Create the Contacts DataFrame
  - [x] Create the Crowdfunding Database
  
- <b>Methods, Software and Attribution:</b>
  - following programming languages, software, and libraries were used in this project:</br>
    * <img src="https://img.shields.io/badge/python-inactive.svg?style=flat&logo=Python&logoColor=yellow" width="80px">&nbsp;<img src="https://img.shields.io/badge/postgres-inactive.svg?style=flat&logo=postgresql&logoColor=blue" width="89px">
    * <img src="https://img.shields.io/badge/Jupyter Notebook-inactive.svg?style=flat&logo=Jupyter&logoColor=orange" width="150px">&nbsp;<img src="https://img.shields.io/badge/Visual Studio Code-inactive.svg?style=flat&logo=Visual Studio Code&logoColor=blue" width="158px">&nbsp;<img src="https://img.shields.io/badge/Microsoft PowerPoint-inactive.svg?style=flat&logo=Microsoft PowerPoint&logoColor=orange" width="172px">
    * <img src="https://img.shields.io/badge/pandas-inactive.svg?style=flat&logo=pandas&logoColor=blueviolet" width="80px">&nbsp;<img src="https://img.shields.io/badge/NumPy-inactive.svg?style=flat&logo=NumPy&logoColor=blue" width="80px">&nbsp;<img src="https://img.shields.io/badge/RegExr-inactive.svg?style=flat&logo=data:image/png;base64,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&logoColor=blue" width="80px">&nbsp;<img src="https://img.shields.io/badge/JSON-inactive.svg?style=flat&logo=JSON&logoColor=black" width="68px">

       
  - The project header GIF has been designed by powerpoint and <a href="https://photopea.com">photopea.com</a> using assets from <a href="https://Freepik.com">Freepik.com</a>.
 
  

<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/asset/space_label.png" width="30px"> <b>ETL Results</b></br>
- <b>Create the Category and Subcategory DataFrames</b>
<h6 align="center">Fig[1]: Category and Subcategory DataFrames</h6>
<p align="center">
<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/output/category_df.png" width="160px">&nbsp;<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/output/subcategory_df.png" width="220px">
</p>

- <b>Create the Campaign DataFrame</b>
<h6 align="center">Fig[2]: Campaign DataFrame</h6>
<p align="center">
<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/output/campaign.png" width="900px">
</p>

- <b>Create the Contacts DataFrame</b>
<h6 align="center">Fig[3]: Contacts DataFrame</h6>
<p align="center">
<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/output/contacts.png" width="450px">
</p>

- <b>Create the Crowdfunding Database</b></br>
  - In this project, [Entity-Relationship Diagrams (ERDs)](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) were utilized as the primary modeling method, implemented using the [QUICK DBD](https://www.quickdatabasediagrams.com/) application. The ERD revealed four entities in the crowdfunding database, namely categories, subcategories, campaigns, and contacts. The modeling results were depicted in Figure 4. Additionally, the [Crowdfunding ERD Documentation](https://github.com/theidari/Crowdfunding_ETL/blob/main/output/Crowdfunding_ERD.pdf) offers a comprehensive overview of the diagram.
  - [<b>Create a Table and Import Data</b>](https://github.com/theidari/Crowdfunding_ETL/blob/main/code/crowdfunding_db.sql)
<h6 align="center">Fig[4]: Crowdfunding ERD</h6>
<p align="center">
<img src="https://raw.githubusercontent.com/theidari/Crowdfunding_ETL/591ec41cf96da62ebed837b35537da4880705a33/output/crowdfunding_ERD_basic_color.svg" width="600px" height="700px">
</p>


<img src="https://github.com/theidari/Crowdfunding_ETL/blob/main/asset/space_label.png" width="30px"> <b>References</b></br>
<sup>[1]</sup> Trilogy Education Services, a <a href="https://2u.com/">2U, Inc.</a> brand.</br>
