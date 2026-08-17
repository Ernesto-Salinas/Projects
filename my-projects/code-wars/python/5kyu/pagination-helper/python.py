"""
Instructions:
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0) # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

Given Code:
# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        pass
    
    # returns the number of items within the entire collection
    def item_count(self):
        pass
    
    # returns the number of pages
    def page_count(self):
        pass
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        pass
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass

"""

# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        itemcount=0
        pagecount=0
        for i in self.collection:
            itemcount+=1
            if (itemcount-1)%self.items_per_page==0:
                pagecount+=1
        return pagecount
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        items_on_page=0
        itemsleft = self.item_count()
        if page_index < 0:
            return -1
        for i in range(page_index+1):
            items_on_page = 0
            if itemsleft <= 0:
                return -1
            elif itemsleft < self.items_per_page:
                items_on_page = itemsleft
                itemsleft -= self.items_per_page
            elif itemsleft >= self.items_per_page:
                items_on_page = self.items_per_page
                itemsleft -= self.items_per_page
        return items_on_page

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        itemcount=0
        pagecount=0
        if item_index > (self.item_count()-1) or item_index < 0:
            return -1
        else:
            for i in range(item_index+1):
                itemcount+=1
                if (itemcount-1)%self.items_per_page==0:
                    pagecount+=1
            return pagecount-1

helper = PaginationHelper(['a','b','c','d','e','f'], 4)

print("The number of pages is ", helper.page_count())
print("The number of items is ", helper.item_count())
print("The number of items on page 0 is ",helper.page_item_count(-1))
print("The number of items on page 1 is ",helper.page_item_count(0))
print("The number of items on page 2 is ", helper.page_item_count(1))
print("The number of items on page 3 is ", helper.page_item_count(2))
print("Item 6 is on page index ", helper.page_index(5))
print("Item 3 is on page index ", helper.page_index(2))
print("Item 21 is on page index ", helper.page_index(20))
print("Item index -10 is on page index ", helper.page_index(-10))
print("Item 1 is on page index ", helper.page_index(0))