import re
import json


class DataExtractor:
    
    def __init__(self):
        self.patterns = {
            'email': re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'),
            'url': re.compile(r'https?://(?:[-\w.])+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'),
            'phone': re.compile(r'(?:\(\d{3}\)\s*\d{3}[-.\s]*\d{4}|\b\d{3}[-.\s]*\d{3}[-.\s]*\d{4}\b)'),
            'credit_card': re.compile(r'\b(?:\d{4}[\s-]?){3}\d{4}\b'),
            'time': re.compile(r'(?:\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)\b|\b(?:[01]?\d|2[0-3]):[0-5]\d(?!\s?(?:AM|PM|am|pm))\b)'),
            'html_tag': re.compile(r'</?[a-zA-Z][^<>]*/?>'),
            'hashtag': re.compile(r'#[a-zA-Z][a-zA-Z0-9_]*'),
            'currency': re.compile(r'\$(?:\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)\b')
        }
    
    def get_emails(self, text):
        return self.patterns['email'].findall(text)
    
    def get_urls(self, text):
        return self.patterns['url'].findall(text)
    
    def get_phones(self, text):
        return self.patterns['phone'].findall(text)
    
    def get_credit_cards(self, text):
        return self.patterns['credit_card'].findall(text)
    
    def get_times(self, text):
        return self.patterns['time'].findall(text)
    
    def get_html_tags(self, text):
        return self.patterns['html_tag'].findall(text)
    
    def get_hashtags(self, text):
        return self.patterns['hashtag'].findall(text)
    
    def get_currency(self, text):
        return self.patterns['currency'].findall(text)
    
    def extract_all(self, text):
        results = {}
        methods = {
            'emails': self.get_emails,
            'urls': self.get_urls,
            'phones': self.get_phones,
            'credit_cards': self.get_credit_cards,
            'times': self.get_times,
            'html_tags': self.get_html_tags,
            'hashtags': self.get_hashtags,
            'currency': self.get_currency
        }
        
        for name, func in methods.items():
            results[name] = func(text)
        
        return results
    
    def check_results(self, text, expected):
        actual = self.extract_all(text)
        checks = {}
        
        for key in expected:
            if key in actual:
                checks[key] = set(actual[key]) == set(expected[key])
            else:
                checks[key] = False
        
        return checks


def run_demo():
    extractor = DataExtractor()
    
    sample = """
    Contact us at support@company.com or sales@subdomain.example.org
    Visit our website: https://www.example.com or https://subdomain.example.org/page
    Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
    Payment options: 1234 5678 9012 3456 or 1234-5678-9012-3456
    Meeting times: 14:30 today or 2:30 PM tomorrow
    HTML content: <div class="container"><p>Hello World</p></div>
    Follow us: #TechTips #WebDevelopment #CodingLife
    Prices start at $19.99 and go up to $1,234.56
    """
    
    print("Data Extraction Results:")
    print("-" * 30)
    
    results = extractor.extract_all(sample)
    
    for data_type, matches in results.items():
        print(f"\n{data_type}:")
        if matches:
            for match in matches:
                print(f"  {match}")
        else:
            print("  None found")


if __name__ == "__main__":
    run_demo()