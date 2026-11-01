def count_words(text):
    d= {}
    words = text.split()
    words = [word.strip('.,!?;:()[]{}"\'') for word in words]  # Remove punctuation
    words = [word.lower() for word in words]  # Convert to lowercase
    for index, word in enumerate(words):
        key= words[index]
        value = words.count(key)
        d[key] = value
    return d

        

print(count_words("AI is the future. The future is now."))  