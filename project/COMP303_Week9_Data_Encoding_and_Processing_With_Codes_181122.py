#!/usr/bin/env python
# coding: utf-8

# In this lecture, we try to process data presented in different kinds of common encodings, such as `CSV` files, `JSON`, `XML` using Python. Unlike the lectures on data structures, this chapter is not focused on specific algorithms, but instead on the problem of getting data in and out of a program.

# ## Reading and Writing `CSV` Data
# 
# You want to read or write data encoded as a `CSV` file. For most kinds of `CSV` data, use the csv library. For example, suppose you have some stock market data in a file named `data.csv`.

# In[1]:


import csv
with open('data.csv') as f:
    f_csv = csv.reader(f)
    print(f_csv)
    print(type(f_csv))
    headers = next(f_csv)
    print(headers)
    print(headers[1])
    for row in f_csv:
        # print(row)
        # print(type(row))
        print(row[1])
        print(type(row[1]))


# If you do not want use indexes to reach specific column in given `CSV` file, you have an alternative way:

# In[2]:


from collections import namedtuple
with open('data.csv') as f:
    f_csv = csv.reader(f)
    # headings is columns names
    headings = next(f_csv)
    print(headings)
    Row = namedtuple('Row', headings)
    print(Row)
    for r in f_csv:
        # print(r)
        # print(type(r))
        row = Row(*r)
        print(row)
        print("--->", row[1])
        print("--->", type(row[1]))


# Another alternative to read the data as a sequence of dictionaries. To do that, we have another object inside `csv` module >> __DictReader()__.

# In[3]:


with open('data.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'], "\t", row['Change'], "\t", row['Volume'])


# ### How to write data into `CSV` file

# In[4]:


headers


# In[5]:


rows=[('AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'),
('AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500'),
('AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000'),
('BA', '98.31', '6/11/2007', '9:36am', '+0.12', '104800'),
('C', '53.08', '6/11/2007', '9:36am', '-0.25', '360900'),
('CAT', '78.29', '6/11/2007', '9:36am', '-0.23', '225400')]


# In[6]:


with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)


# If you have the data as a sequence of dictionaries, do this:

# In[7]:


headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']


# In[8]:


rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        {'Symbol': 'BA', 'Price': 98.31, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': +0.12, 'Volume': 104800},
        {'Symbol': 'C', 'Price': 53.08, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': -0.25, 'Volume': 360900},
        {'Symbol': 'CAT', 'Price': 78.29, 'Date': '6/11/2007',
          'Time': '9:36am', 'Change': -0.23, 'Volume': 225400}]


# In[9]:


with open('stocks_dict.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)


# In[10]:


with open('stocks.csv') as f:
    for line in f:
        row = line.split(',')
        print(row)


# In[11]:


with open('stocks_dict.csv') as f:
    for line in f:
        row = line.split(',')
        print(row)


# ## If we have a headers which are not valid identifiers(example Header name: \_Date-Values), how we process the `CSV` file:

# In[12]:


import re
with open('data_regex.csv') as f:
    f_csv = csv.reader(f)
    headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    print("AFTER:", headers)
    Row = namedtuple('Row',headers)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol_for_stocks)


# # How we convert to string data to other types?

# It is also important to emphasize that `csv`does not try to interpret the data or convert it to a type other than a **string**. If such conversions are important, there is something need to do yourself. Here is one example of performing extra type conversions on `CSV`data:

# In[13]:


# 1st way
# Write each data type for columns in list
col_types = [str, float, str, str, float, int]

with open('data.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    total, counter_rows = 0, 0
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(converted_type(value) 
                    for converted_type, value in zip(col_types, row))
        print(row)
        print(type(row[1]), type(row[4]), type(row[5]))
        total += row[1]
        counter_rows += 1
    average = total / counter_rows
    print("\n=============\n")
    print(f"Average Price Values --> {average:.3f}")


# ## Converting selected fields (columns) type of `csv` file

# Alternatively, here is an example of converted selected fields of dictionaries:

# In[14]:


print('Reading as dicts with type conversion')
field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]

with open('data.csv') as f:
    total, counter_rows = 0, 0
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)
        print(type(row['Price']), type(row['Change']), type(row['Volume']))
        total += row['Price']
        counter_rows += 1
    average = total / counter_rows
    print("\n=============\n")
    print(f"Average Price Values --> {average:.3f}")


# ## Reading and Writing `JSON` Data
# 
# JSON is stands for _JavaScript Object Notation_. In Python, there exist a module with a name of __json__. With this module we can read JSON data.

# In[15]:


# Let us convert Python dictionary into JSON data
import json

data = {'Name':'COMP',
        'Code': 303,
        'Section': 1
       }

# Convert this dictionary into json string
json_str = json.dumps(data)
print(json_str)


# Here is how you turn `JSON`-encoded string back into a Python data structure:

# In[16]:


data = json.loads(json_str)
print(data)


# In[17]:


# let us write this json string into json file
with open('data.json', 'w') as f:
    json.dump(data, f)


# In[18]:


# Read the json file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


# In[19]:


yes = True # in type true
no = False # in type false
variable = None # in json type null

data = {'a': True,
     'b': 'Hello',
     'c': None,
     'd': False
    }

json.dumps(data)


# In[20]:


from urllib.request import urlopen
from pprint import pprint

url = urlopen('https://glin.github.io/reactable/articles/popular-movies/tmdb_movies.json')
response = json.loads(url.read().decode('utf-8'))
pprint(response)


# In[21]:


type(response)


# In[22]:


len(response)


# In[23]:


response[1000].keys()


# In[24]:


print(response[110]['title'])


# In[25]:


actual_data = response[110]['similar']
print(actual_data)
print("\n=================\n")
print(type(actual_data), type(actual_data[7]))


# In[26]:


actual_data[7].keys()


# In[27]:


for k,v in actual_data[7].items():
    print(k, ': ',v)


# In[28]:


movie_data = actual_data[7]['title']


# In[29]:


print(movie_data)


# # How we can convert  a `Json` data into Python object rather dict or list

# In[30]:


json_data = '{"name": "COMP", "code": 303, "section": 1}'

# First define a class to declare a template to generate object
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d
        
data = json.loads(json_data, object_hook = JSONObject)


# In[31]:


data.name


# In[32]:


data.code


# In[33]:


data.section


# In[34]:


type(data)


# In[35]:


data = {'Name':'COMP',
        'Code': 303,
        'Section': 1
       }

print(json.dumps(data))


# In[36]:


print(json.dumps(data, indent = 4))


# # Parsing Simple XML Data

# Module name to process the XLM documents is xml.etree.ElementTree

# In[37]:


from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Dowload the RSS feed and Parse it.
url = urlopen('https://planetpython.org/rss20.xml')

# Then parse this feed
document=parse(url)


# In[38]:


# Extracting and output tags of interest from the document
for item in document.iterfind('channel/item'):
    title = item.findtext('title')
    pubDate = item.findtext('pubDate')
    link = item.findtext('link')
    
    print(title)
    print(pubDate)
    print(link)


# In[39]:


# Use of find() method over document object
e = document.find('channel/title')
e


# In[40]:


e.tag


# In[41]:


e.text


# In[42]:


e.get('some_attribute')


# For parsing `XML` Files _ElementTree_ module is not the only option for you. You might consider to use __lxml__ module. You only need to change previous import statement to following.

# In[43]:


# Instead of following import
# from xml.etree.ElementTree import parse
# Use this version
from lxml.etree import parse
from xml.etree.ElementTree import iterparse
get_ipython().run_line_magic('pinfo', 'iterparse')


# In[44]:


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    document = iterparse(filename, events = ('start','end'))
    # Skip the document element
    next(document)
    
    tags = []
    elements = []
    for event, element in document:
        if event == 'start':
            tags.append(element.tag)
            elements.append(element)
            # print(tags)
            # print(elements)
        elif event == 'end':
            if tags == path_parts:
                yield element
                # elements[-2].remove[element]
            try:
                tags.pop()
                elements.pop()
            except IndexError:
                pass


# In[45]:


# Suppose you want to write a script that ranks employees by the id numbers.
# let us do it together
from collections import Counter
employees_by_id = Counter()

data = parse_and_remove('employee.xml', 'employee/projects/project')
for employee in data:
    print(employee.findtext('id'))
    employees_by_id[employee.findtext('id')] += 1
    
print(employees_by_id)
    
for eid, num in employees_by_id.most_common():
    print(eid, num)


# In[46]:


data = iterparse('employee.xml', events = ('start','end'))


# In[47]:


next(data)


# In[48]:


next(data)


# In[49]:


next(data)


# In[50]:


next(data)


# In[51]:


next(data)


# In[52]:


next(data)


# In[53]:


next(data)


# In[54]:


next(data)


# In[55]:


next(data)


# In[56]:


next(data)


# In[57]:


next(data)


# In[58]:


next(data)


# In[59]:


next(data)


# In[60]:


next(data)


# In[61]:


next(data)


# In[62]:


next(data)


# # Turning Dictionary into XML File

# In[63]:


from xml.etree.ElementTree import Element
# Write a function that convert given python dictionary to xml file
def dict_to_xml(tag, dictionary):
    elem = Element(tag)
    for key, value in dictionary.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem


# In[64]:


employee = {'First Name': 'Ali', 'Second Name': 'Cihan',
            'Last Name':'Keles','age':35}
e = dict_to_xml('record', employee)


# In[65]:


e


# In[66]:


from xml.etree.ElementTree import tostring


# In[67]:


tostring(e)


# In[68]:


def dict_to_xml_str(tag, dictionary):
    parts = ['<{}>'.format(tag)]
    for key,value in dictionary.items():
        parts.append('<{0}>{1}</{0}>'.format(key,value))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)

e_str = dict_to_xml_str('record', employee)
print(e_str)

