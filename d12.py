text = input("Make a Sentence: ")
news = []
word = ""
for char in text:
    if char != " ":
        word += char
    else:
        news.append(word)
        word = ""
if word:
    news.append(word)   
print (news)

# #word tokenization
# def tokenize(text):
#     tokens = []
#     current_token = []
    
#     for char in text.title():
#         if char.isalnum():
#             current_token.append(char)
#         elif current_token:
#             tokens.append(''.join(current_token))
#             current_token = []
    
#     if current_token:
#         tokens.append(''.join(current_token))
    
#     return tokens

# text = input("Enter a Sentence: ")
# tokens = tokenize(text)
# print(tokens)

        