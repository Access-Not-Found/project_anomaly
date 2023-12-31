# Access Not Found: Anomaly Detection Project

# Project Description

This repo contains a group project identifying anomalies in user access logs for the CodeUp Curriculm sites. Using analysis and data aggregating techniques we were able to answer the questions listed below per an email sent requesting our help. The deliverables are a professional response email, a single google summary slide, final noteboook, wrangle and explory .py modules, and this repository.

# Project Goal

* Outliers on the curriculum logs, providing insights via email to the boss for the board meeting on Friday morning.
* This analysis aims to address the listed questions and uncover any additional important findings related to the observed counts data.
* Answer 5 questions sent through e-mail, provide one slide summary in Google slides.

# Initial Thoughts

There are going to be valuable insights that we can use to help the requestor with their presentation.

# The Plan

* Acquire
    * Data acquired from MySql Server using env.py credentials
    * Joined logs and cohorts tables then pulled into jupyter lab environment and created a CSV
    * 847330 rows × 15 columns *before* cleaning
    * 847330 rows × 14 columns *after* cleaning

* Prepare
    * dropped columns
        * id, slack, deleted_at, date, time
    * renamed columns
        * name to cohort
        * created_at to created
        * updated_at to updated
    * changed dates to datetime type
    * created new columns
        * program name by mapping program_id
            * 1 = data science
            * 2&3 = web dev
            * 4 = cloud
        * date and time combined into one column and renamed to access_dates
        * lesson column
        * endpoint column
    * no nulls

* Explore
    * Questions
        1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
        2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
        3. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
        4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
        5. Which lessons are least accessed?
        6. Anything else of note...

# Data Dictionary  

| Feature | Definition|
|:--------|:-----------|
|date| Access date of the user|
|time| Access time of the user|
|path| User pathway|   
|user_id| Specific user id per cohort|    
|cohort_id| Specific cohort id|   
|ip| IP address of the user|
|name| Cohort Name|   
|start_date| Start_date for the user|
|end_date| End_date for the user|
|created_at| Date and time of account creation|
|updated_at| Date and time of last update|
|program_id| Specific id for each program offered|

# Steps to Reproduce
1. Clone this repo
2. Run notebook

---

# Explore Takeaways

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    * Classification, javascript-i, and html-css are the top lessons per program offered.
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    * Cohorts Bayes and Curie, specialized in data science, exhibit higher access frequencies for lessons on anomaly detection, NLP, 3-SQL, and Python. Cohort Teddy shows a distinct preference for the mkdocs lesson, while Cohort Zion demonstrates a significantly higher frequency for accessing CSS-I.
    * The Apex cohort stands out by accessing the professional development lesson more frequently than other cohorts. Additionally, all cohorts show similar frequencies in accessing the extra features and CSS lessons.
3. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
    * There is evidence of students accessing different materials during 2018. It was difficult to determine, by program_id, which students belonged to which known Codeup program. Knowing that data science began in 2019 helped to determine the proper program names. From that knowledge we were able to correctly identify the programs based on dates and lessons pinged.
    * There are web dev students accessing data science materials into 2020, *after* access was restricted.
4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
    * The top lessons accessed after graduation in the Web Development program include fundamentals, MySQL, and JavaScript I, II, and III. In the Data Science program, frequently accessed post-graduation lessons are SQL, classification, fundamental, Python, and 3-SQL.
5. Which lessons are least accessed?
    * Lessons like using-files, intro-to-mysql, control-structures-ii, command-line, and PHP have relatively low student access rates. This suggests that these lessons cover familiar everyday practices and may not require frequent review, unlike more complex and less commonly used lessons.
6. Anything else of note...
    * not on this iteration
        
# Recommendations/Next Steps

* The cohorts that pinged the most may have had some circumstances with the curriculum not work in their favor. I recommend working with the instructors to identify and remedy the possible confusion.

* For the third question my next steps would be to identify the students specifically that are accessing restricted materials to try to figure out how they did it and close the loop.

* We recommend maintaining graduates' access to the curriculum and implementing a system to send them notifications regarding significant updates. This approach ensures their ongoing engagement and keeps them up-to-date with the latest advancements in the curriculum.