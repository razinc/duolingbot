import random
from syllabus import syllabus

# print(list(syllabus.keys()))

topic = random.choice(list(syllabus.keys()))
# print(topic)

phrase = random.choice(syllabus[topic])
# print(phrase)

print(f"Topic: {topic}")
print(f"\tEnglish: {phrase['english']}")
print(f"\tChinese: {phrase['chinese']}")
print(f"\tPinyin : {phrase['pinyin']}")
