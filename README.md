PulsePlot: Overview

In this project I have gathered my listening history from my spotify account. Then performed data analysis on it to get a better understanding of my listening history, music taste, and choice of artist.

Moreover, performed a cluster analysis on the dataset.
Codes and Resources used

    Editor used: VS code
    Python version: 3.11
    Packages used: pandas, matplotlib, seaborn, calplot, sklearn, spotipy, requests
    
About the Dataset

The data is scraped from Spotify using it's API.
Data Cleaning

The data is then preprocessed and transformed as required to avoid any abberations that might later skew the results.

The data cleaning steps that are performed are:

    Dropping duplicate columns
    Dropping duplicate rows
    Null check
    Data Format check
    Value check

Exploratory Data Analysis - using seaborn, calplot, matplotlib

Cluster Analysis
Various cluster analysis are performed to group and define the cluster profiles of the songs.

Different cluster algorithms performed are:

    KMeans clustering
    Agglomerative clustering
    DBSCAN
