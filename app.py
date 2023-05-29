import docx

docx.Document.__format__ = lambda x, _: x.paragraphs[0].text
# import random_information

# print(random_information.roll_dice(10))
