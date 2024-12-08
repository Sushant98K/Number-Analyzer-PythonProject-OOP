# Number Analyzer

```python
import time
import sys

def typing_animation(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

typing_animation("Welcome to the Number Analyzer!", 0.1)