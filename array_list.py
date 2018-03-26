# Array List

# A List represents an array in python
class List:
    def __init__(self, data, length, cap):
        self.data = data        # a list
        self.length = length    # an Int
        self.cap = cap          # an Int

    def __eq__(self, other):
        return (type(other) == List
                and self.data == other.data
                and self.length == other.length
                and self.cap == other.cap)

    def __repr__(self):
        return "List({!r}, {!r}, {!r})".format(self.data, self.length, self.cap)

# a Song represents a song and its attributes
class Song:
    def __init__(self, title, artist, album, num):
        self.title = title
        self.artist = artist
        self.album = album
        self.num = num

    def __eq__(self, other):
        return (type(other) == Song
                and self.title == other.title
                and self.artist == other.artist
                and self.album == other.album
                and self.num == other.num)

    def __repr__(self):
        return "Song({!r}, {!r}, {!r}, {!r})".format(self.title, self.artist, self.album, self.num)

# empty_list
# -> List
# returns an empty list
def empty_list():
    return List([None], 0, 1)

# add
# List Int Value -> List
# returns a new List with the given value (any type) added into the list
def add(lst, index, val):
    if index < 0 or index > lst.length:
        raise IndexError()
    else:
        if lst.length >= lst.cap:
            new_cap = lst.cap * 2
            new_list = [None] * new_cap
            for i in range(0, index):
                new_list[i] = lst.data[i]
            for j in range(index, lst.length):
                new_list[j + 1] = lst.data[j]
            new_list[index] = val
            return List(new_list, lst.length + 1, new_cap)
        else:
            for i in range(lst.length - 1, index - 1, -1):
                lst.data[i + 1] = lst.data[i]
            lst.data[index] = val
            return List(lst.data, lst.length + 1, lst.cap)

# length
# List -> Int
# returns the number of elements in the List
def length(lst):
    return lst.length

# get
# List Int -> Value
# returns the value at the index in the list
def get(lst, index):
    if index < 0 or index >= lst.length:
        raise IndexError()
    else:
        return lst.data[index]

# set
# List Int Value -> List
# returns a new List with the given value (any type) at the index (Int) specified
def set(lst, index, val):
    if index < 0 or lst.data[0] is None and index >= 0 or index >= lst.length:
        raise IndexError()
    else:
        lst.data[index] = val

    return List(lst.data, lst.length, lst.cap)

# remove
# List Int -> List
# returns a new List without the element at the index
def remove(lst, index):
    if index < 0 or index >= lst.length:
        raise IndexError()
    else:
        length = lst.length - 1
        val = lst.data[index]
        for i in range(index, length):
            lst.data[i] = lst.data[i + 1]
        lst.data[length] = None
        return (val, List(lst.data, length, lst.cap))

# search
# List Int -> Song
# Returns the Song with the correct num attribute
def search(lst, no):
    for song in lst.data:
        if int(song.num) == int(no):
            return song

# foreach
# List function -> None
# applies provided function to each value in List
def foreach(lst, f):
    if lst.data[0] is None:
        return None
    else:
        for i in range(lst.length):
            f(lst.data[i])

# sort
# List func -> List
# returns a sorted list based on the function
def sort(song_a_list, f):
    lst = song_a_list.data
    global length
    length = song_a_list.length
    for index in range(length - 1):
        small_index = index_of_smallest(lst, index, f)
        swap(lst, index, small_index)        
    return song_a_list

# helper function for sort
# list Int func -> Int
# returns the index of the smallest value (defined by a function) in the list
def index_of_smallest(lst, start, f):
    index = start
    for i in range(start, length):
        if f(lst[i], lst[index]) is True:
            index = i
    return index

# helper function for sort
# list Int Int -> None
# swaps two values in a list
def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
            
