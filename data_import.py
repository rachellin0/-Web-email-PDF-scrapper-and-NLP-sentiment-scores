
# !pip install PyMuPDF
# !pip install requests
# !pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import email
import imaplib
import os
import fitz
# from common import TextObject  # Import the TextObject class from your common module

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find and extract the main article content
            main_article = soup.find('main')  # Adjust the tag based on the site's structure
            if main_article:
                article_text = main_article.get_text()
            else:
                article_text = "Main article content not found."

            # Create a TextObject instance and return it
            article_object = TextObject(article_text)
            return article_object

        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

class EmailFilter:
    def __init__(self, email_address, password, imap_server):
        self.email_address = email_address
        self.password = password
        self.imap_server = imap_server

    def fetch_email_bodies(self):
        try:
            mail = imaplib.IMAP4_SSL(self.imap_server)
            mail.login(self.email_address, self.password)
            mail.select('inbox')

            result, data = mail.search(None, 'ALL')
            email_ids = data[0].split()

            email_bodies = []

            for email_id in email_ids:
                result, msg_data = mail.fetch(email_id, '(RFC822)')
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            try:
                                email_bodies.append(part.get_payload(decode=True).decode('utf-8'))
                            except UnicodeDecodeError:
                                email_bodies.append(part.get_payload(decode=True).decode('ISO-8859-1'))
                else:
                    content_type = msg.get_content_type()
                    if content_type == "text/plain":
                        try:
                            email_bodies.append(msg.get_payload(decode=True).decode('utf-8'))
                        except UnicodeDecodeError:
                            email_bodies.append(msg.get_payload(decode=True).decode('ISO-8859-1'))

            return email_bodies

        except Exception as e:
            print("Error:", e)
            return []
        return TextObject("\n".join(email_bodies))


class PDFTextProcessor:
    def __init__(self, pdf_urls):
        self.pdf_urls = pdf_urls

    def process_pdf_files(self):
        processed_texts = []

        for pdf_url in self.pdf_urls:
            processed_text = self.process_pdf_url(pdf_url)
            processed_texts.append(processed_text)

        combined_text = "\n".join(processed_texts)
        return TextObject(combined_text)

    def process_pdf_url(self, pdf_url):
        try:
            response = requests.get(pdf_url)
            pdf_bytes = response.content

            pdf_document = fitz.open("pdf", pdf_bytes)
            text = ""

            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()

            processed_text = self.process_text(text)
            return processed_text
        except Exception as e:
            print(f"Error processing {pdf_url}: {e}")
            return ""

    def process_text(self, raw_text):
        # Perform your processing steps here (e.g., remove articles, reduce to word roots)
        # For demonstration, let's assume we're just lowercasing the text
        processed_text = raw_text.lower()
        return processed_text

def process_data_sources(web_url=None, email_address=None, password=None, imap_server=None, pdf_urls=None):
    processed_texts = []

    if web_url:
        scraper = WebScraper(web_url)
        scraped_text = scraper.scrape()
        processed_texts.append(scraped_text.text)  # Extract the text attribute

    if email_address and password and imap_server:
        email_filter = EmailFilter(email_address, password, imap_server)
        email_bodies = email_filter.fetch_email_bodies()
        processed_texts.extend(email_bodies)

    if pdf_urls:
        pdf_processor = PDFTextProcessor(pdf_urls)
        pdf_processed_text = pdf_processor.process_pdf_files()
        processed_texts.append(pdf_processed_text.text)  # Extract the text attribute

    combined_text = "\n".join(processed_texts)
    return TextObject(combined_text)

