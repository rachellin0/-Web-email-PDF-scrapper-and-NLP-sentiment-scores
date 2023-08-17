I've developed modules in data_import.py, common.py, sentiment_engine.py, and the main.py driver script. I've implemented basic text mining to clean the text and split it into sentences. I've utilized sentiment analysis for each of these sentences using both **VADER** Compound scores within the range of [-1, 1] and **TextBlob**'s Polarity within the range of [-1, 1], along with Subjectivity in the range of [0, 1]. An example of the results is shown below.

#### In order to execute the main.py, kindly replace it with your actual email address and generate a temporary password as below: 
* Enable the IMAP Access at: Gmail Settings> Forwarding and POP / IMAP> IMAP Acess
* Enable 2-factor authentication for the google account
* generate an app-specific password (https://myaccount.google.com/apppasswords)
* Use this newly generated password for imap login
#### Download the following libraries for this task:
* vaderSentiment
* PyMuPDF
* requests
* beautifulsoup4
#### To support text mining, I used the following resources:
* nltk.download('punkt')
* nltk.download('stopwords')

#### Sentiment score results example  
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



#### Scraped text example 
(a) real property held for at least 12 months
the term “real property” means land and 
includes the following:
1) qualified conservation easements 
transferred to a qualified organization as 
described in sections 2031(c)(8)(b) and 
170(h) of the internal revenue code
2) grazing permits or grazing leases 
issued by the u.s. forest service, the 
bureau of land management, or the 
idaho department of lands, but only if 
the grazing permit or grazing lease was 
transferred at the same time as the “base 
property”
3) depreciable real property as described in 
section 1250(c) of the internal revenue 
code, but only if that property was 
transferred in perpetuity and the transfer 
was required to be in writing according to 
idaho code section 9-503.
(b) tangible personal property used in a 
revenue-producing enterprise and held for at 
least 12 months
