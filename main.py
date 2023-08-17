

from data_import import WebScraper, EmailFilter, PDFTextProcessor
from sentiment_engine import SentimentAnalyzer
from common import TextObject

def main():
    # Replace with actual values
    WEB_URL = "http://www.assafelovic.com/blog/2020/12/28/how-to-build-a-url-text-summarizer-with-simplenbspnlp"
    EMAIL_ADDRESS = "your_email@gmail.com"# Replace with actual email
    PASSWORD = "qxxymqhuqhyhmkbo"  #newly generated password for imap login
    IMAP_SERVER = "imap.gmail.com" 
    PDF_URLS = ["https://tax.idaho.gov/wp-content/uploads/forms/EFO00093/EFO00093_05-19-2022.pdf"]

    # Process data from different sources
    processed_text = process_data_sources(web_url=WEB_URL,
                                          email_address=EMAIL_ADDRESS,
                                          password=PASSWORD,
                                          imap_server=IMAP_SERVER,
                                          pdf_urls=PDF_URLS)

    # Print the unified processed text
    #print(processed_text.text)

    analyzer = SentimentAnalyzer()
    sentiment_df = analyzer.analyze_text(processed_text)
    # Print the first 10 rows of the sentiment DataFrame
    for index, row in sentiment_df.head(10).iterrows():
        print("Sentence:", row['Sentence'])
        for column in sentiment_df.columns:
            if column != 'Sentence':
                print(f"{column}:", row[column])
        print("-----")

if __name__ == "__main__":
    main()



