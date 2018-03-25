# Project 2
# Linked List

# an AnyList is one of 
# - None, or
# a Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first    # any data type
        self.rest = rest      # an AnyList
   
    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return "Pair({!r}, {!r})".format(self.first, self.rest)    

# A Song represents a track and its info
class Song:
    def __init__(self, title, artist, album, num):
        self.title = title    # a String
        self.artist = artist  # a String 
        self.album = album    # a String
        self.num = num        # a String or an Int

    def __eq__(self, other):
        return (type(other) == Song
                and self.title == other.title
                and self.artist == other.artist
                and self.album == other.album
                and self.num == other.num)    

    def __repr__(self):
        return "Song({!r}, {!r}, {!r}, {!r})".format(self.title, self.artist, self.album, self.num)

# empty_list
# -> AnyList
# returns an empty list
def empty_list():
    return None

# add
# AnyList Int Value -> AnyList
# returns an AnyList with the value (any type) placed at the integer index
def add(lst, index, val):
    if lst is None:
        if index == 0:
            return Pair(val, None)
        else:
            raise IndexError()
    elif index > 0:
        return Pair(lst.first, add(lst.rest, index - 1, val))
    elif index == 0:
        return Pair(val, Pair(lst.first, lst.rest))
    else:
        raise IndexError()

# length
# AnyList -> Int
# returns the number of elements in the list
def length(lst):
    if lst is None:
        return 0
    else:
        return 1 + length(lst.rest)

# get
# AnyList Int -> Value
# returns the value (any type) at the index (int) position 
def get(lst, index):
    if lst is None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return lst.first
        else:
            return get(lst.rest, index - 1)

# set
# AnyList Int Value -> AnyList
# returns a new AnyList with the new Value at the integer index
def set(lst, index, val):
    if lst is None or index < 0:
        raise IndexError()
    else:
        if index == 0:
            return Pair(val, lst.rest)
        elif index > 0:
            return Pair(lst.first, set(lst.rest, index - 1, val))

# remove helper
# AnyList Int -> AnyList
def remove_helper(lst, index):
    global rem
    if index < 0 or lst is None:
        raise IndexError()
    else:
        if index > 0:
            return Pair(lst.first, remove_helper(lst.rest, index - 1))
        else:
            rem = lst.first
            return lst.rest

# remove
# AnyList Int -> Tuple
# removes element at the index from the list and returns the removed element and the resulting list in a tuple
def remove(lst, index):
    global rem
    if index < 0 or lst is None:
        raise IndexError()
    elif index == 0 and lst.rest is None:
        return None
    elif index == 0:
        rem = lst.first
        new_pair = lst.rest
    else: # lst.rest is not None:
        new_pair = Pair(lst.first, remove_helper(lst.rest, index - 1))
    return (rem, new_pair)

# search
# List val -> Song
# Returns the Song with the correct num attribute | Assumes correct song exists
def search(lst, no):
    if int(lst.first.num) == int(no):
        return lst.first
    else:
        return search(lst.rest, no) 

# foreach
# List function -> None
# applies provided function to each value in list
def foreach(lst, f):
    if lst is None:
        return None    
    else: 
        f(lst.first)
        foreach(lst.rest, f) 

# Insertion sort
# List function -> List
# returns a sorted list based on the function | Assumes list is not empty 
def sort(song_l_list, f):
    res_lst = Pair(song_l_list.first, None)
    while song_l_list.rest is not None:
        new_lst = song_l_list.rest
        res_lst = insert(res_lst, new_lst.first, f)
        song_l_list = song_l_list.rest
    return res_lst

# sort helper (insert)
# List val func -> List
# returns a new sorted list including the new number (sorted by func)
def insert(lst, val, f):
    if lst is None:
        return Pair(val, None)
    else:
        if f(lst.first, val) is True:
            return Pair(lst.first, insert(lst.rest, val, f))
        else:
            return Pair(val, lst)

