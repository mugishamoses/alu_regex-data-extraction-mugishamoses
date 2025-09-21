"""
ALU Regex Data Extraction Tool
Author: mugishamoses
Description: A comprehensive tool for extracting various data types from text using regex patterns
"""

import re
from typing import List, Dict, Tuple
import json


class DataExtractor:
    """
    A comprehensive data extraction tool using regular expressions.
    Supports extraction of emails, URLs, phone numbers, credit cards, time, HTML tags, hashtags, and currency.
    """
    
    def __init__(self):
        """Initialize the DataExtractor with optimized regex patterns for all data types."""
        self.patterns = {
            'email': self._compile_email_pattern(),
            'url': self._compile_url_pattern(),
            'phone': self._compile_phone_pattern(),
            'credit_card': self._compile_credit_card_pattern(),
            'time': self._compile_time_pattern(),
            'html_tag': self._compile_html_tag_pattern(),
            'hashtag': self._compile_hashtag_pattern(),
            'currency': self._compile_currency_pattern()
        }
    
    def _compile_email_pattern(self) -> re.Pattern:
        """
        Email pattern that handles common formats including:
        - Basic emails: user@domain.com
        - Subdomain emails: user@subdomain.domain.com
        - Names with dots: first.last@domain.com
        - Plus addressing: user+tag@domain.com
        """
        pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.compile(pattern)
    
    def _compile_url_pattern(self) -> re.Pattern:
        """
        URL pattern that handles:
        - HTTP/HTTPS protocols
        - Subdomains
        - Paths and query parameters
        - Various TLDs
        """
        pattern = r'https?://(?:[-\w.])+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'
        return re.compile(pattern)
    
    def _compile_phone_pattern(self) -> re.Pattern:
        """
        Phone pattern that handles multiple formats:
        - (123) 456-7890
        - 123-456-7890
        - 123.456.7890
        - 123 456 7890
        """
        pattern = r'(?:\(\d{3}\)\s*\d{3}[-.\s]*\d{4}|\b\d{3}[-.\s]*\d{3}[-.\s]*\d{4}\b)'
        return re.compile(pattern)
    
    def _compile_credit_card_pattern(self) -> re.Pattern:
        """
        Credit card pattern that handles:
        - Space separated: 1234 5678 9012 3456
        - Dash separated: 1234-5678-9012-3456
        - No separators: 1234567890123456
        """
        pattern = r'\b(?:\d{4}[\s-]?){3}\d{4}\b'
        return re.compile(pattern)
    
    def _compile_time_pattern(self) -> re.Pattern:
        """
        Time pattern that handles:
        - 24-hour format: 14:30, 09:15
        - 12-hour format: 2:30 PM, 11:45 AM
        """
        # Combined pattern: 24-hour OR 12-hour with AM/PM
        pattern = r'(?:\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)\b|\b(?:[01]?\d|2[0-3]):[0-5]\d(?!\s?(?:AM|PM|am|pm))\b)'
        return re.compile(pattern)
    
    def _compile_html_tag_pattern(self) -> re.Pattern:
        """
        HTML tag pattern that handles:
        - Opening tags: <div>, <p class="example">
        - Closing tags: </div>, </p>
        - Self-closing tags: <img src="..." />
        """
        pattern = r'</?[a-zA-Z][^<>]*/?>'
        return re.compile(pattern)
    
    def _compile_hashtag_pattern(self) -> re.Pattern:
        """
        Hashtag pattern that handles:
        - Simple hashtags: #example
        - CamelCase hashtags: #ThisIsAHashtag
        - Hashtags with numbers: #hashtag2024
        """
        pattern = r'#[a-zA-Z][a-zA-Z0-9_]*'
        return re.compile(pattern)
    
    def _compile_currency_pattern(self) -> re.Pattern:
        """
        Currency pattern that handles:
        - Dollar amounts: $19.99, $1,234.56
        - Various formats with commas and decimals
        """
        pattern = r'\$(?:\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)\b'
        return re.compile(pattern)
    
    def extract_emails(self, text: str) -> List[str]:
        """Extract all email addresses from the given text."""
        return self.patterns['email'].findall(text)
    
    def extract_urls(self, text: str) -> List[str]:
        """Extract all URLs from the given text."""
        return self.patterns['url'].findall(text)
    
    def extract_phones(self, text: str) -> List[str]:
        """Extract all phone numbers from the given text."""
        return self.patterns['phone'].findall(text)
    
    def extract_credit_cards(self, text: str) -> List[str]:
        """Extract all credit card numbers from the given text."""
        return self.patterns['credit_card'].findall(text)
    
    def extract_times(self, text: str) -> List[str]:
        """Extract all time expressions from the given text."""
        return self.patterns['time'].findall(text)
    
    def extract_html_tags(self, text: str) -> List[str]:
        """Extract all HTML tags from the given text."""
        return self.patterns['html_tag'].findall(text)
    
    def extract_hashtags(self, text: str) -> List[str]:
        """Extract all hashtags from the given text."""
        return self.patterns['hashtag'].findall(text)
    
    def extract_currency(self, text: str) -> List[str]:
        """Extract all currency amounts from the given text."""
        return self.patterns['currency'].findall(text)
    
    def extract_all(self, text: str) -> Dict[str, List[str]]:
        """
        Extract all supported data types from the given text.
        
        Args:
            text (str): The input text to extract data from
            
        Returns:
            Dict[str, List[str]]: Dictionary containing all extracted data types
        """
        results = {}
        extraction_methods = {
            'emails': self.extract_emails,
            'urls': self.extract_urls,
            'phones': self.extract_phones,
            'credit_cards': self.extract_credit_cards,
            'times': self.extract_times,
            'html_tags': self.extract_html_tags,
            'hashtags': self.extract_hashtags,
            'currency': self.extract_currency
        }
        
        for data_type, method in extraction_methods.items():
            try:
                results[data_type] = method(text)
            except Exception as e:
                # Handle edge cases gracefully
                results[data_type] = []
                print(f"Warning: Error extracting {data_type}: {str(e)}")
        
        return results
    
    def validate_extraction(self, text: str, expected: Dict[str, List[str]]) -> Dict[str, bool]:
        """
        Validate extraction results against expected outputs.
        Useful for testing and quality assurance.
        """
        actual = self.extract_all(text)
        validation_results = {}
        
        for data_type in expected:
            if data_type in actual:
                validation_results[data_type] = set(actual[data_type]) == set(expected[data_type])
            else:
                validation_results[data_type] = False
        
        return validation_results


def main():
    """
    Main function to demonstrate the data extraction capabilities.
    """
    extractor = DataExtractor()
    
    # Sample text containing various data types
    sample_text = """
    Contact us at support@company.com or sales@subdomain.example.org
    Visit our website: https://www.example.com or https://subdomain.example.org/page
    Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
    Payment options: 1234 5678 9012 3456 or 1234-5678-9012-3456
    Meeting times: 14:30 today or 2:30 PM tomorrow
    HTML content: <div class="container"><p>Hello World</p></div>
    Follow us: #TechTips #WebDevelopment #CodingLife
    Prices start at $19.99 and go up to $1,234.56
    """
    
    print("=== ALU Regex Data Extraction Tool ===\n")
    print("Sample text:")
    print(sample_text)
    print("\n" + "="*50 + "\n")
    
    # Extract all data types
    results = extractor.extract_all(sample_text)
    
    # Display results
    for data_type, matches in results.items():
        print(f"{data_type.upper()}:")
        if matches:
            for match in matches:
                print(f"  - {match}")
        else:
            print("  - No matches found")
        print()


if __name__ == "__main__":
    main()