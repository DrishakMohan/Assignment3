"""
Name:Drishak Mohan
University:University Of Toronto
"""


from typing import List, Dict, Tuple

def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    f=open(file_name,"r")
    data=f.readlines()
    d={}

    for i in range(0,len(data),5):
        
        if data[i+2]=="\n" and data[i+3]=="\n":
            a={int(data[i].replace(" ","").strip("\n")):(data[i+1].replace(" ","").strip("\n"),[],[])}
            d.update(a)  
        
        elif data[i+2]=="\n":
            a={int(data[i].replace(" ","").strip("\n")):(data[i+1].replace(" ","").strip("\n"),[],[int(x.strip()) for x in data[i+3].replace(" ","").strip("\n").split(",")])}
            d.update(a)
        
        elif data[i+3]=="\n":
            a={int(data[i].replace(" ","").strip("\n")):(data[i+1].replace(" ","").strip("\n"),[int(x.strip()) for x in (data[i+2].replace(" ","").strip("\n").split(","))],[])}
            d.update(a)           
        
        else:
            a={int(data[i].replace(" ","").strip("\n")):(data[i+1].replace(" ","").strip("\n"),[int(x.strip()) for x in (data[i+2].replace(" ","").strip("\n").split(","))],[int(x.strip()) for x in data[i+3].replace(" ","").strip("\n").split(",")])}
            d.update(a)
    return d
mghn.

def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.
    
    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400, 
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'], 
        [100, 200, 300], 
        [400, 500]), 
    100001: (
        200, 
        'Make the ocean great again.', 
        [''], 
        [], 
        [400]), 
    100002: (
        500, 
        "Help I'm being held captive by a beast!  %OhNoes", 
        ['OhNoes'], 
        [400], 
        [100, 200, 300]), 
    100003: (
        500, 
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome", 
        ['StockholmeSyndrome'], 
        [400, 100], 
        []), 
    100004: (
        300, 
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
        ['ShowYouTheWorld', 'JustSayNo'], 
        [500, 200], 
        [400]), 
    100005: (
        400, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    """
    f=open(file_name,"r")
    D=f.readlines()
    d={}
    
    for i in range(0,len(D),7):
        
        if D[i+5]=="\n" and D[i+4]=="\n" and D[i+3]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),[''],[],[])}
            d.update(a)        
        
        elif D[i+5]=="\n" and D[i+4]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),D[i+3].replace(" ","").strip("\n").split(","),[],[])}
            d.update(a)
        
        elif D[i+4]=="\n" and D[i+3]==["\n"]:
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),[''],[],[int(x.strip()) for x in (D[i+5].replace(" ","").strip("\n").split(","))])}
            d.update(a)
        
        elif D[i+5]=="\n" and D[i+3]==["\n"]:
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),[''],[int(x.strip()) for x in (D[i+4].replace(" ","").strip("\n").split(","))],[])}
            d.update(a)
        
        elif D[i+4]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),D[i+3].replace(" ","").strip("\n").split(","),[],[int(x.strip()) for x in (D[i+5].replace(" ","").strip("\n").split(","))])}
            d.update(a)
        
        elif D[i+5]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),D[i+3].replace(" ","").strip("\n").split(","),[int(x.strip()) for x in (D[i+4].replace(" ","").strip("\n").split(","))],[])}
            d.update(a)
        
        elif D[i+3]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),[''],[int(x.strip()) for x in (D[i+4].replace(" ","").strip("\n").split(","))],[])}
            d.update(a)            

        elif D[i+5]=="\n" and D[i+4]=="\n":
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),D[i+3].replace(" ","").strip("\n").split(","),[],[])}
            d.update(a)
        
        else:
            a={int(D[i].replace(" ","").strip()):(int(D[i+1].replace(" ","").strip("\n")),D[i+2].strip("\n"),D[i+3].replace(" ","").strip("\n").split(","),[int(x.strip()) for x in (D[i+4].replace(" ","").strip("\n").split(","))],[int(x.strip()) for x in (D[i+5].replace(" ","").strip("\n").split(","))])}
            d.update(a)   
    
    return d

def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of th .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(create_profile_dictionary("profiles.txt"), create_chirp_dictionary("chirps.txt"))
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profiles, chirps, 500 )
    ['Make the ocean great again.', 
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
    'Does not want to build a %SnowMan %StopAsking']
    """
    f= []
    e=[]
    ifo=[]
    l=[]
    c=[]
    g=[]
    a=chirp_dictionary.keys()
    for i in  profile_dictionary[user_id][2]:
        ifo.append(i)
    for j in ifo:
        for i in a:
            if j==chirp_dictionary[i][0]:
                c+=[i]
                g.append(len(chirp_dictionary[i][3]))
    l.append(chirp_dictionary[c[g.index(max(g))]][1])
    return l
    
def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.
    
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(create_chirp_dictionary("chirps.txt"))
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']}, 
    '': {
        200: ['Make the ocean great again.']}, 
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]}, 
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"], 
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}, 
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    ans_dict = dict()
    l=[]
    a=chirp_dictionary.keys()
    for i in a:
        for j in chirp_dictionary[i][2]:
            l.append(j)

    for i in range(len(l)):
        item = l[i].strip()
        l[i] = item
    for number in chirp_dictionary:
        for tag in l:
            h = dict()
            for x in chirp_dictionary.keys():
                if tag in chirp_dictionary[x][1]:
                    if h.get(chirp_dictionary[x][0],True) != True:
                        h[chirp_dictionary[x][0]].append(chirp_dictionary[x][1])
                    else:
                        h[chirp_dictionary[x][0]] = [chirp_dictionary[x][1]]
            ans_dict[tag] = h
    return ans_dict

def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking', 
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    l=[]
    a=chirp_dictionary.keys()
    for i in a:
        if tag in chirp_dictionary[i][2]:
            l.append(chirp_dictionary[i][1])
    return l




    
