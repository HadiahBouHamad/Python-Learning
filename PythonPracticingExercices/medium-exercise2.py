def count_words(text):
    d= {}
    words = text.split()
    words = [word.strip('.,!?;:()[]{}"\'') for word in words]  # Remove punctuation
    words = [word.lower() for word in words]  # Convert to lowercase
    for word in words:
        d[word] = d.get(word,0) +1 
    return d

print(count_words("AI is the future. The future is now."))  