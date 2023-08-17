I've developed modules in data_import.py, common.py, sentiment_engine.py, and the main.py driver script. I've implemented basic text mining to clean the text and split it into sentences. I've utilized sentiment analysis for each of these sentences using both **VADER** Compound scores within the range of [-1, 1] and **TextBlob**'s Polarity within the range of [-1, 1], along with Subjectivity in the range of [0, 1]. An example of the results is shown below.
#### I used the following libraries for this task:
* vaderSentiment
* PyMuPDF
* requests
* beautifulsoup4
#### To support text mining, I used the following resources:
* nltk.download('punkt')
* nltk.download('stopwords')

#### In order to execute the main.py, kindly replace it with your actual email address and generate a temporary password as below: 
* Enable the IMAP Access at: Gmail Settings> Forwarding and POP / IMAP> IMAP Acess
* Enable 2-factor authentication for the google account
* generate an app-specific password (https://myaccount.google.com/apppasswords)
* Use this newly generated password for imap login


#### Sentiment score results 
                    Sentence  Vader_Sentiment  \
0  Assaf Elovic   December 28, 2020     How to bu...           0.0000    
1  To view the source code, please visit my GitHu...           0.3182   
2  Wouldn’t it be great if you could automaticall...           0.6249   
3  Rather you’re too busy, or have too many artic...           0.1513  
4  That’s why TL;DR (too long didn’t read) is so ...           0.0000  
5  While this internet acronym can criticize a pi...           0.0516  
6  While my last piece focused on how to estimate...           0.3818  
7  Getting startedFor this tutorial, we’ll be usi...           0.5994     
8  Beautiful Soup is a Python library for pulling...           0.5994    
9  It works with your favorite parser to provide ...           0.4588    

   TextBlob_Polarity  TextBlob_Subjectivity  
0           0.000000               0.357143  
1           0.000000               0.000000  
2           0.800000               0.750000  
3           0.200000               0.325000  
4          -0.175000               0.450000  
5          -0.116667               0.533333  
6           0.000000               0.066667  
7           0.850000               1.000000  
8           0.850000               1.000000  
9           0.500000               1.000000  
