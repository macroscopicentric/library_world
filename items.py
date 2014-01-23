import rooms

class Item(object):
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location

    def examine(self):
        print self.description

    def take(self):
        player.inventory.append(self.name)
        self.location = 'player'
        player.location.inventory.remove(self.name)
        print "You take the %s." % (self.name)

    def drop(self):
        player.inventory.remove(self.name)
        self.location = player.location
        player.location.inventory.append(self.name)
        print "You drop the %s." % (self.name)

#Items
ledger = Item('ledger', '''It's a large leather ledger. It's incredibly heavy, and when you open it you feel as though it
contains every piece of equipment checked out by every librarian in the history of the Clayr. It's that big. You probably don't want
to carry it around.''', rooms.librarian_alcove)

pan_pipes = Item('pipes', '''It's a set of pan pipes. There are seven total. They're plain wood,
bound together with leather, and inscribed with Charter marks.''')
bells = Item('bells', '''A set of seven bells hang on a bandolier, meant to be worn across the chest. Their leather pouches are
etched with Charter marks and the bells' mahogany handles stick out of the top of the pouches.''')

item_list = {'ledger': ledger, 'pipes': pan_pipes, 'bells': bells} #is there a way I can 'predefine' these items so I can put them up with the other lists?