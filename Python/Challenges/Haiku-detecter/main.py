class Poem():
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
    
    def syllable_count(self, words):
        counts = []
        counter = 0
        for word in words:
            word = word.lower()
            count = 0
            vowels = "aeiouy"
            if word[0] in vowels:
                count += 1
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    count += 1
            if word.endswith("e"):
                count -= 1
            if count == 0:
                count += 1
            counts.append(count)
            counter += 1
        return counts

    def split(self, poem):
        words = poem.split(" ")
        return words

    def is_haiku(self, line1, line2, line3):
        words1 = self.split(line1)
        words2 = self.split(line2)
        words3 = self.split(line3)
        count1 = self.syllable_count(words1)
        count2 = self.syllable_count(words2)
        count3 = self.syllable_count(words3)
        total1 = 0
        total2 = 0
        total3 = 0
        for i in count1:
            total1 = total1 + i
        for j in count2:
            total2 = total2 + j
        for k in count3:
            total3 = total3 + k
        if total1 == 5 and total2 == 7 and total3 == 5:
            return True
        return False
        
        

poem = Poem("Harry was a good boy.", "Harry was a very good.", "Harry was a good.")
print(poem.is_haiku(poem.line1, poem.line2, poem.line3))