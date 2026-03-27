# Solution 12: Syntactic Address Validation (Valid IP Address)

## Approach Explanation
We split the IP based on the delimiter (`.` for IPv4, `:` for IPv6) and check every component against the specific rules of each protocol.

## Step-by-Step Logic
1. If `.` is in `queryIP`, check for IPv4:
   - Split by `.`. Must have 4 parts.
   - For each part:
     - Must be 1-3 digits.
     - Must not have leading zeros (unless it's just "0").
     - Must be between 0 and 255.
2. If `:` is in `queryIP`, check for IPv6:
   - Split by `:`. Must have 8 parts.
   - For each part:
     - Must be 1-4 characters.
     - Each character must be hex (0-9, a-f, A-F).
3. Return results accordingly.

## Complexity
- **Time Complexity:** O(N).
- **Space Complexity:** O(N).

## Code
```python
def valid_ip_address(queryIP):
    def isIPv4(s):
        parts = s.split(".")
        if len(parts) != 4: return False
        for p in parts:
            if not p.isdigit(): return False
            if p[0] == '0' and len(p) > 1: return False
            if not 0 <= int(p) <= 255: return False
        return True
        
    def isIPv6(s):
        parts = s.split(":")
        if len(parts) != 8: return False
        hexdigits = "0123456789abcdefABCDEF"
        for p in parts:
            if not 1 <= len(p) <= 4: return False
            if not all(c in hexdigits for c in p): return False
        return True
        
    if "." in queryIP and isIPv4(queryIP): return "IPv4"
    if ":" in queryIP and isIPv6(queryIP): return "IPv6"
    return "Neither"
```
