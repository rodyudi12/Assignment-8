class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
     
    def __str__(self): #fixed
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size): #I took out the data=None, because I was not using in this
        self.size = size
        self.data = [None] * size
    #hash function    
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    #insert function
    def insert(self, key, value):
        new_contact = Contact(key, value) #I created this so the contact could be stored in a correct way, before was printing just the number without the name when I tried to 
        index = self.hash_function(key)
        current = self.data[index]
        if self.data[index] is None:
            self.data[index] = Node(key, new_contact) #added this so the contact will be added to the index
            return
        
        while current:
            if current.key == key:
                current.value = new_contact #update to new contact
                return
            
            if current.next is None:
                break
            current = current.next
        current.next = Node(key, new_contact) #I also changed this Node to new_contact, so there are no issues

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value #I forgot to put .value
            current = current.next

        return None
    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}: ")
            current = self.data[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"{current.value}") #it doesn't need the key anymore, when it had it duplicated the name, so I can just remove the current.key
                    current = current.next
    
    

# Test your hash table implementation here.  
table = HashTable(10)

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
#Edge 1: Hash Collisions
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")
#Edge 2: Duplicate Keys
table.insert("Rebecca", "999-444-9999") 
table.print_table()


#search names plus edge 3
search_names = ["John", "Chris"]
i = 0
while i <len(search_names):
    name = search_names[i]
    contact = table.search(name)
    if contact is not None:
        print(f"Search result:", contact)
    else:
        print("Search result: None")
    i += 1

'''
Why is hash table the right structure for fast lookups? Especially for long lists, a list looping becomes expensive. So a hash takes a string and converts into a number
This is good because it makes it faster for the program to search and insert new names. It's fine to use a list if you have just 3 names with contacts, but if we have a whole
phonebook hash makes it efficient so search for each contact.
How did you handle colisions? I handle colisions by adding to the same index in example edge 1, and another example is edge 2 that it substitutes the contact number for the last number added
for example what happened to Rebecca, the number showing in the output is the last one added. For edge 3 when the contact doesn't exist, I decided to create a loop through the names to print if the contact exists or not.
The problem that I was thinking when I decided to do this loop is that if I had like 100 names to search, I don't think it would work well.
When might an enginner choose a hash table over a list or tree? Hash table is better when you don't need to care about order, and you have a big number of insertion(data) in the table. So the most important thing of hash table
is that you can navigate through all the insertions, especially when it is a large number in a faster way
'''