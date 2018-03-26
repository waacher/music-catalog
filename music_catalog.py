# Music Catalog

# Using array lists

import sys
sys.setrecursionlimit(99999)
from array_list import *
#from linked_list import *

# A Song represents a track and its info
class Song:
    def __init__(self, title, artist, album, num):
        self.title = title      # a String
        self.artist = artist    # a String
        self.album = album      # a String
        self.num = num          # an Int

    def __eq__(self, other):
        return (type(other) == Song
                and self.title == other.title
                and self.artist == other.artist
                and self.album == other.album
                and self.num == other.num)

    def __repr__(self):
        return "Song({!r}, {!r}, {!r}, {!r})".format(self.title, self.artist, self.album, self.num)

# Display main menu
def menu():
    print("Song Catalog")
    print("   1) Print Catalog\n   2) Song Information\n   3) Sort\n   4) Add Songs\n   0) Quit")
    choice = input("Enter selection: ")
    return choice

# Display sort menu
def sort_menu():
    print("\nSort songs")
    print("   0) By Number\n   1) By Title\n   2) By Artist\n   3) By Album")
    choice = input("Sort by: ")
    print()
    return choice

# print_song
# Song -> Song
# prints a formatted Song
def print_song(song):
    if song is not None:
        print("{!r}--{}--{}--{}".format(song.num, song.title, song.artist, song.album))
    else:
        pass

# Str -> List
# Returns song information from text file as a list of Song obejcts | Process invalid inputs
def read_songs_from_file(infile):
    song_list = empty_list()
    global error_lines
    error_lines = []
    line_count = 1
    list_index = 0
    global song_num
    song_num = 0
    for line in infile:
        line = line.strip()
        if line == '':
            pass 
        else:    
            lst0 = line.split('--')
            if len(lst0) == 3:
                new_song = Song(lst0[0], lst0[1], lst0[2], song_num)
                song_list = add(song_list, list_index, new_song)
                list_index += 1
                song_num += 1
            else:
                error_lines.append(line_count)
        line_count += 1
    return song_list

def main():
    try:
        infile = open(sys.argv[1], 'r')
        song_list = read_songs_from_file(infile)
    except IndexError:
        print("Usage: python3 music_catalog.py <file>")
        sys.exit(1)
    except FileNotFoundError:
        print("'{}': No such file or directory".format(sys.argv[1]))
        sys.exit(1)

    if len(error_lines) > 0:
        print("Catalog input errors:")
        for line in error_lines:
            print("line", line, ": malformed song information")
        print()   
    
    choice = menu()
    global sort_choice
    sort_choice = None 
    
    while choice != '0':
        if choice == '1': # Print Catalog
            foreach(song_list, print_song) 
            print()

        elif choice == '2': # Song info 
            song_no = input("Enter song number: ")  
            if int(song_no) >= length(song_list) or int(song_no) < 0:
                print("\n... Invalid song number")
                print()
            else:
                right_song = search(song_list, song_no)
                print("\nSong information ...")
                print("   Number:", right_song.num)
                print("   Title:", right_song.title)
                print("   Artist:", right_song.artist)
                print("   Album:", right_song.album) 
                print()       

        elif choice == '3': # Sort
            menu_choice = sort_menu()
            song_list = catalog_sort(song_list, menu_choice)
            
        elif choice == '4': # Add Songs (file)
            file_to_load = input("Enter name of file to load: ")
            try:
                addfile = open(file_to_load, 'r')
                global song_num
                line_count = 1
                index = length(song_list)
                error_lines_1 = []
                for line in addfile:
                    line = line.strip()
                    if line == '':
                        pass
                    else:
                        line_lst = line.split('--')
                        if len(line_lst) == 3:
                            new_song = Song(line_lst[0], line_lst[1], line_lst[2], song_num)
                            song_list = add(song_list, index, new_song)
                            song_num += 1
                            index += 1
                        else:
                            error_lines_1.append(line_count)
                        line_count += 1
                if sort_choice is not None:
                    song_list = catalog_sort(song_list, sort_choice)
                if len(error_lines_1) > 0:
                    print("\nCatalog input errors:")
                    for line in error_lines_1:
                        print("line", line, ": malformed song information\n")
                     
            except IndexError:
                print("\nUsage: python3 music_catalog.py <file>\n")
            except FileNotFoundError:
                print("\n'{}': No such file or directory\n".format(file_to_load))    
        else:
            print("\nInvalid Option\n")     

        choice = menu()

# less-than-artist
# Song Song -> bool
# returns true if the first Song's artist is 'less-than' the second
def less_than_artist(s1, s2):
    if s1.artist < s2.artist:
        return True
    elif s1.artist == s2.artist:
        if s1.album < s2.album:
            return True
        elif s1.album == s2.album:
            if s1.title < s2.title:
                return True
            elif s1.title == s2.title:
                return less_than_number(s1, s2)
    return False

# less-than-album
# Song Song -> bool
# return true if the first Song's album is 'less-than' the second
def less_than_album(s1, s2):
    if s1.album < s2.album:
        return True
    elif s1.album == s2.album:
        if s1.artist < s2.artist:
            return True
        elif s1.artist == s1.artist:
            if s1.title < s2.title:
                return True
            elif s1.title == s2.title:
                return less_than_number(s1, s2)
    return False

# less-than-title
# Song Song -> bool
# return true if the first Song's title is 'less-than' the second
def less_than_title(s1, s2):
    if s1.title < s2.title:
        return True
    elif s1.title == s2.title:
        if s1.artist < s2.artist:
            return True
        elif s1.artist == s2.artist:
            if s1.album < s2.album:
                return True
            elif s1.album == s2.album:
                return less_than_number(s1, s2)
    return False

# less-than-number
# Song Song -> bool
# return True if the first Song's number is 'less-than' the second
def less_than_number(s1, s2):
    if int(s1.num) < int(s2.num):
        return True
    else:
        return False

# other sort
# List Str -> List
# sorts the List based on the choice | Retains last valid choice
def catalog_sort(lst, choice):
    if choice != '0' and choice != '1' and choice != '2' and choice != '3':
        print("... Invalid sort option\n")
    else:
        if choice == '0':
            lst = sort(lst, less_than_number)
        elif choice == '1':
            lst = sort(lst, less_than_title)
        elif choice == '2':
            lst = sort(lst, less_than_artist)
        elif choice == '3':
            lst = sort(lst, less_than_album)
        global sort_choice
        sort_choice = choice     
    return lst

if __name__ == '__main__':
    main()
