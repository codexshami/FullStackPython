# Problem 17: The Word Ladder (Word Ladder)

## Problem Statement
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words such that:
1. The first word is `beginWord`.
2. The last word is `endWord`.
3. Every adjacent pair of words differs by a single letter.
4. Every word in the sequence is in `wordList`.

Return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.

## Input Format
- Strings `beginWord` and `endWord`.
- A list of strings `wordList`.

## Example
**Input:** beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]  
**Output:** 5  
**Explanation:** "hit" → "hot" → "dot" → "dog" → "cog"
