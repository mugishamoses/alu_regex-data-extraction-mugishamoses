import re
import json
from typing import Dict, List


class DataExtractor:
    """
    A comprehensive data extraction tool using regular expressions.
    Extracts emails, URLs, phone numbers, credit cards, times, HTML tags, hashtags, and currency.
    """
    
    def __init__(self):
        """Initialize regex patterns for different data types."""
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
    
    def get_emails(self, text: str) -> List[str]:
        """Extract email addresses from text."""
        return self.patterns['email'].findall(text)
    
    def get_urls(self, text: str) -> List[str]:
        """Extract URLs from text."""
        return self.patterns['url'].findall(text)
    
    def get_phones(self, text: str) -> List[str]:
        """Extract phone numbers from text."""
        return self.patterns['phone'].findall(text)
    
    def get_credit_cards(self, text: str) -> List[str]:
        """Extract credit card numbers from text."""
        return self.patterns['credit_card'].findall(text)
    
    def get_times(self, text: str) -> List[str]:
        """Extract time formats from text."""
        return self.patterns['time'].findall(text)
    
    def get_html_tags(self, text: str) -> List[str]:
        """Extract HTML tags from text."""
        return self.patterns['html_tag'].findall(text)
    
    def get_hashtags(self, text: str) -> List[str]:
        """Extract hashtags from text."""
        return self.patterns['hashtag'].findall(text)
    
    def get_currency(self, text: str) -> List[str]:
        """Extract currency amounts from text."""
        return self.patterns['currency'].findall(text)
    
    def extract_all(self, text: str) -> Dict[str, List[str]]:
        """Extract all supported data types from text."""
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
    
    def save_results_to_file(self, results: Dict, filename: str = "extraction_results.json"):
        """Save extraction results to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {filename}")


def test_edge_cases():
    """Test regex patterns with edge cases and malformed data."""
    extractor = DataExtractor()
    
    test_cases = {
        "Valid Data": """
        Contact: user@example.com, firstname.lastname@company.co.uk
        Sites: https://www.example.com, https://subdomain.example.org/page
        Phones: (123) 456-7890, 123-456-7890, 123.456.7890
        Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
        Times: 14:30, 2:30 PM, 11:59 PM
        HTML: <p>, <div class="example">, <img src="image.jpg" alt="description">
        Tags: #example, #ThisIsAHashtag
        Money: $19.99, $1,234.56
        """,
        
        "Edge Cases": """
        Invalid emails: @example.com, user@, incomplete@domain
        Malformed phones: 123-45-6789, (12) 456-7890
        Wrong cards: 1234 5678 901, 1234-5678-9012-345
        Bad times: 25:30, 13:60 PM, 24:00 PM
        Invalid tags: #123StartWithNumber, #
        Wrong currency: $, $1,23.456
        """,
        
        "Mixed Content": """
        Real email: support@company.com mixed with fake: user@
        Good URL: https://test.com with incomplete: http://
        Valid phone: (555) 123-4567 and invalid: 555-12-3456
        """
    }
    
    print("EDGE CASE TESTING")
    print("=" * 50)
    
    for test_name, test_data in test_cases.items():
        print(f"\n{test_name.upper()}:")
        print("-" * 30)
        results = extractor.extract_all(test_data)
        
        for data_type, matches in results.items():
            if matches:
                print(f"{data_type}: {len(matches)} found - {matches}")
            else:
                print(f"{data_type}: None found")


def run_comprehensive_demo():
    """Run comprehensive demonstration with multiple test scenarios."""
    extractor = DataExtractor()
    
    # Sample data for demonstration
    sample_data = """
    Welcome to TechCorp! Contact us at support@company.com or sales@subdomain.example.org
    Visit our website: https://www.example.com or check our blog at https://subdomain.example.org/page
    
    Customer Service Numbers:
    - Main Office: (123) 456-7890
    - Support Line: 123-456-7890  
    - Emergency: 123.456.7890
    
    Payment Information:
    - Visa: 1234 5678 9012 3456
    - MasterCard: 1234-5678-9012-3456
    
    Office Hours:
    - Weekdays: 9:00 AM to 17:30
    - Weekend Support: Available 14:30 to 2:30 PM
    
    Website Content:
    <div class="container">
        <p>Welcome to our site!</p>
        <img src="logo.jpg" alt="Company Logo">
    </div>
    
    Social Media:
    Follow us on Twitter: #TechTips #WebDevelopment #CodingLife #Innovation2024
    
    Pricing:
    - Basic Plan: $19.99/month
    - Premium Plan: $99.99/month  
    - Enterprise: $1,234.56/month
    """
    
    print("COMPREHENSIVE DATA EXTRACTION DEMO")
    print("=" * 50)
    print("Sample text being analyzed...")
    print("\nExtraction Results:")
    print("-" * 30)
    
    results = extractor.extract_all(sample_data)
    
    # Display results with counts
    for data_type, matches in results.items():
        print(f"\n{data_type.upper()} ({len(matches)} found):")
        if matches:
            for i, match in enumerate(matches, 1):
                print(f"  {i}. {match}")
        else:
            print("  No matches found")
    
    # Save results to file
    extractor.save_results_to_file(results)
    
    return results


def main():
    """Main function to run all demonstrations."""
    print("REGEX DATA EXTRACTION TOOL")
    print("=" * 50)
    print("This tool extracts 8 types of data using regular expressions:")
    print("1. Email addresses")
    print("2. URLs") 
    print("3. Phone numbers")
    print("4. Credit card numbers")
    print("5. Time formats")
    print("6. HTML tags")
    print("7. Hashtags")
    print("8. Currency amounts")
    print("\n")
    
    # Run comprehensive demo
    results = run_comprehensive_demo()
    
    print("\n" + "=" * 50)
    
    # Run edge case testing
    test_edge_cases()
    
    print("\n" + "=" * 50)
    print("Demo completed! Check 'extraction_results.json' for saved results.")


if __name__ == "__main__":
    main()