# TDI Capstone Project

(Sep. to Nov. 2019 cohort) 

My capstone project is using Machine Learning Models to predict early childhood development outcomes in developing countries. 

I am currently still working on deploying my app to Heroku using Docker. Stay tuned to look at my website.

To help you understand the end project, I made a video and you can find it [here](https://youtu.be/D_Xf4k-dl6c).


## 1. Why early childhood development?
As the basis for overall human development, ECD plays a key role in enhancing the productivity and growth of a child. Failures to invest in ECD can, therefore, result in the delay of a child’s development as well as inhibit the optimal development and performance of children throughout their lives. In child development, early years play a crucial role as formative years for brain development, affecting learning, health and ultimately income. As such, investing in early years yields a high return in investment, through creating the human capital needed for economic growth, and reducing poverty and inequality, thus forming the basis for sustainable development. Yet there are a lot of studies about ECD in different countries, no study takes a holistic approach to look at ECD worldwide.


## 2. Dataset
The dataset for this project is from [UNICEF Multiple Indicator Cluster Survey](http://mics.unicef.org/) which has surveys from 1999 to 2018 from more than 100 countries. For this project, 6 years of data is used (from around 150,000 children under 5 years old, 41 countries).


## 3. Machine Learning Model   
Because it is a classification problem (e.g whether the child is able to identify 10 letters/alphabet or not?), I used Logistics Regression to predict this outcome based on a number of features I had (mother's education level, child age, child family wealth status, etc.). I used Random Forest (RF) Model too. Although RF model has slightly higher accuracy (83.5%) compared with Logistics Regression Model (83%), it takes longer to run, and also I am not able to check the coefficient to know which feature has a negative/postive effect towards the result. Thus, I chose logistics regression model for my capstone project. 

## 4. What else is used to prepare my project?
- Flask
- Heroku
- Folium: you can see two country-level overview that I prepared using Folium.
- HTML
- Stata (I used Stata to cleaned and combined my dataset from UNICEF before using Python to train the Machine Learning Model)

## 5. To Conclude:
The outcome of this project will be very useful for NGOs, International Organizations, governments, and policymakers to design and implement effective policies that are well-supported by evidence. Moreover, this project will also be valuable to foundations and education institutes when considering where and how to invest in early years education that can yield a high return in investment. All in all, the findings will be used as a basis for policy decisions and program interventions, and for the purpose of influencing public opinion on the situation of children around the world.

## Next Steps:
### 1: Improve my ML model
There are rooms to improve my current model. A few things that I could try: 
- add more features to my current model since I have a lot more features in my data (the reason why I did not add a lot of features is that it will be hard for me to prepare my flask app when users have to manually input all the features in order to predict the outcome);
- check some of the correlation of the features, and combined features together if needed;
- Use Gradient Boosting Machine model;


### 2: Build Child Development Outcome Index
I could use a number of outcomes from the survey to construct some sort of child development outcome index, and then use folium to present it to the audience

### 3: Extend to other studies
UNICEF Multiple Indicator Cluster Survey also has "Household Survey" and "Women Survey". More studies can be done to understand:
- Household Characteristics in different countries and worldwide;
- Women empowerment outcomes in different countries and worldwide;
- Merge household survey, and women survey together to study parenting impact on child behavior for child under 5 years old, and child between 5 to 17 years old;
- More study can be done using child survey:
    - Child Health
    - Child Mortality
    - Child Nutrition
    - Child Protection



## Feedback and Contact:
If you have any feedback on my project, or you would like to discuss potential work that we can do together, please feel free to reach out to me: alisa.hdzhao@gmail.com