# Access Not Found: Anomaly Detection Project

# Project Description

This repo contains a group project identifying anomalies in user access logs for the CodeUp Curriculm sites. Using analysis and data aggregating techniques we were able to answer the questions listed below per an email sent requesting our help. The deliverables are a professional response email, a single google summary slide, final noteboook, wrangle and explory .py modules, and this repository.

# Project Goal

* Answer 5 questions sent through e-mail.

# Initial Thoughts

There are going to be some anomalies that we can identify to help the requestor with their presentation.

# The Plan

* Acquire
    * Data acquired from MySql Server using env.py credentials
    * Joined logs and cohorts tables then pulled into jupyter lab environment and created a CSV
    * 73739 Rows x 15 Columns *before* cleaning
    * 73739 Rows x 12 Columns *after* cleaning

  
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
    * cohort_id had 1,334 nulls
        * Bash, Darden, Florence, Hyperion, and Jupiter all had no cohort_id's assigned
            * mapped cohort_id's here that were not taken
            * there did not seem to be any logical ranking order to the cohort_id's
            * 2-6, inclusive, respective to name listing

* Explore
    * Questions
        1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
            * fundamentals for data science
            * mysql for web dev
        2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
        3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
        4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
        5. Which lessons are least accessed?
        6. Anything else of note...

# Data Dictionary  

| Feature | Definition|
|:--------|:-----------|
|| |   
|| |
|| |   
|| |            
|| |   
|| |
|| |   
|| |
|| |
|| |
|| |

# Steps to Reproduce
1. Clone this repo
2. Run notebook

---

# Takeaways

Explore takeaways pointed at some interesting variations presenting when the profits got higher:

1. 

2. 

3. 

4. 

5. 

6. 

***Overall Takeaways:***


    
- Of note: 

# Recommendation
    
* For the data scientists: 
    
* For the business: 
    
# Next Steps:
    
* 