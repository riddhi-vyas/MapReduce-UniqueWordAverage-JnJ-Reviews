# MapReduce-UniqueWordAverage-JnJ-Reviews
This repository contains Python code for a MapReduce program aimed at calculating the average count of unique words in product reviews, specifically tailored for Johnson &amp; Johnson products. The primary code file is designed to be executed on a Hadoop cluster. The repository includes a sample input file named 'reviews.csv' for testing. I have also attached the output file named as logs.txt that I got after running this mapreduce job on hadoop cluster.

Project topic: Analyzing Average Unique Word Counts in Johnson & Johnson Product Reviews using MapReduce

Motivation:
Online shopping plays a crucial role in this digital era. We as consumers heavily depend on product reviews to find insights whether selecting a new dress, renting a car, or booking a hotel. Businesses use sentimental reviews to improve their product performances.

We will analyze review texts for each product by calculating the count of unique words used in the review text. Then using these scores, we will calculate the average count for each product to review the unique content from the reviews. This analysis will provide valuable insights into the unique content within the reviews. By understanding customer sentiments, businesses can make improvements to their products and it helps customers in making better-informed choices.

To achieve this, we are implementing a map reduce program in python that takes user reviews as input and performs analysis using MapReduce. This will enable us to efficiently process large volumes of data, making the analysis scalable and impactful for both businesses and consumers using Hadoop.

Data Acquisition: 
We are using Johnson & Johnson OGX Product Reviews dataset from kaggle - https://www.kaggle.com/datasets/winston56/johnson-johnson-ogx-product-reviews/data.
The dataset contains product reviews for two categories: MakeupAlley and Ulta.
We have used MakeupAlley which contains features: date(review timestamp), rating(rating values from 1 to 5), review(customer review text), and product(product name).
