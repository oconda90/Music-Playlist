from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # Creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #  Create a new song
    new_song = Song(title)

    # Set new song's next pointer to where the __first_song is pointing
    new_song.set_next_song(self.__first_song)

    # Set __first_song pointer to point at the new song
    self.__first_song = new_song

    


  # Searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    index = 0
    current_node = self.__first_song
    while current_node != None:
      if current_node.get_title() == title:
        # print(index)
        return index
      current_node = current_node.get_next_song()
      index += 1
    return None



  # Removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    prev_node = None
    current_node = self.__first_song
    while current_node != None:
      if current_node.get_title() == title:
        if prev_node != None:
          prev_node.set_next_song(current_node.get_next_song())
          break
        else:
          current_node.set_next_song(self.__first_song)
          break
      prev_node = current_node
      current_node = current_node.get_next_song()
    



  # Returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_node = self.__first_song

    while current_node != None:
      counter += 1
      current_node = current_node.get_next_song()

    return counter


  # Prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    count= 1
    current_node = self.__first_song
    while current_node != None:
      print(f'{count}. {current_node} {count}')
      current_node = current_node.get_next_song()
      count += 1

# Insert song any where in the play list
def insert(title, index):
  pass

# Shuffle songs
def shuffle():
  pass

# Reverse songs
def reverse():
  pass

  