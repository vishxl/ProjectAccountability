class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sent in sentences:
            word_count = len(sent.split())
            
            if word_count > max_words:
                max_words = word_count
            
        return max_words   