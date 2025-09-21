# Data Extraction Tool

A Python tool that extracts different types of data from text using regex patterns. Built for the ALU regex assignment.

## What it does

Extracts 8 different data types:
- Email addresses
- URLs  
- Phone numbers
- Credit card numbers
- Time (12/24 hour)
- HTML tags
- Hashtags
- Currency amounts

## Setup

Clone and run:
```bash
git clone https://github.com/mugishamoses/alu_regex-data-extraction-mugishamoses.git
cd alu_regex-data-extraction-mugishamoses
python data_extractor.py
```

Requires Python 3.7+

## Usage

```python
from data_extractor import DataExtractor

extractor = DataExtractor()

text = """
Email me at john@example.com or visit https://example.com
Call (555) 123-4567 for help
Card: 1234 5678 9012 3456
Meeting at 2:30 PM or 14:30
#Python costs $29.99
"""

# Get everything
results = extractor.extract_all(text)

# Or get specific types
emails = extractor.get_emails(text)
urls = extractor.get_urls(text)
```

Output:
```python
{
    'emails': ['john@example.com'],
    'urls': ['https://example.com'], 
    'phones': ['(555) 123-4567'],
    'credit_cards': ['1234 5678 9012 3456'],
    'times': ['2:30 PM', '14:30'],
    'hashtags': ['#Python'],
    'currency': ['$29.99']
}
```

## Testing

Run tests with:
```bash
python test_extractor.py
```

## Files

- `data_extractor.py` - main code
- `test_extractor.py` - tests
- `README.md` - this file

## Regex Patterns

The tool handles various formats for each data type. For example:
- Emails: basic@domain.com, user.name@sub.domain.org
- Phones: (123) 456-7890, 123-456-7890, 123.456.7890  
- Times: 14:30, 2:30 PM, 11:45 am

## Notes

This handles most common formats but might miss some edge cases. The patterns work well for typical use cases.

Author: mugishamoses