import re
from collections import deque

# Define helper classes and methods.


class cacheLRU:
    def __init__(self, size):
        self.size = size
        self.itemHash = {}
        self.itemQueue = deque()

    def Set(self, key, value):

        # Add and Queue key:value.

        self.itemHash[key] = value
        self.QueueKey(key)

    def Get(self, key):

        # Key exist? If not return None

        if (key not in self.itemHash):
            return None

        # Queue and return key.

        self.QueueKey(key)
        return self.itemHash[key]

    def QueueKey(self, key):

        # Attempt to remove key (We have to find it anyways).
        # PS: Not the best solution but restricted by library I picked,
        # welcome to ask why.

        try:
            self.itemQueue.remove(key)
        except:
            pass

        # Append key.

        self.itemQueue.appendleft(key)

        # Pop and remove unwanted tailing item (least recently used item).

        if (len(self.itemQueue) > self.size):
            removedItem = self.itemQueue.pop()
            self.itemHash.pop(removedItem)


class App:
    def __init__(self):
        self.cacheLRU = None

    def SizeHandler(self, args):

        # Check if we called sized already.

        if (self.cacheLRU is not None):
            return False

        # Should only be one argument.

        if (len(args) != 1):
            return False

        # Arg should be a number.

        if not re.match('\d+', args[0]):
            return False
        size = int(args[0])

        # Number should be greater than zero.

        if (size < 1):
            return False

        # Create cache object

        self.cacheLRU = cacheLRU(int(args[0]))
        print 'SIZE OK'
        return True

    def GetHandler(self, args):

        # We call SIZE yet?

        if (self.cacheLRU is None):
            return False

        # Should only be one arg.

        if (len(args) != 1):
            return False

        # No spaces in the arg.

        if not re.match('\S+', args[0]):
            return False

        # Attempt to get value from cache.

        value = self.cacheLRU.Get(args[0])
        if (value is None):
            print 'NOTFOUND'
        else:
            print 'GOT {0}'.format(value)
        return True

    def SetHandler(self, args):

        # We call SIZE yet?

        if (self.cacheLRU is None):
            return False

        # Should only be two args.

        if (len(args) != 2):
            return False
        key = args[0]
        value = args[1]

        # No spaces in the args.

        if not re.match('\S+', key + value):
            return False

        # Set key:value.

        self.cacheLRU.Set(key, value)
        print 'SET OK'
        return True


# Script execution starts here.

# Create app and assign commands.

app = App()
Actions = {
            'SIZE': app.SizeHandler,
            'GET': app.GetHandler,
            'SET': app.SetHandler
          }

# Start loop input execution.

while True:

    # Get input from user.

    command = raw_input()

    # Split input, delimiter = white space.

    args = command.split()

    # Command should come with at least 2 arguments.

    if (len(args) < 2):
        print 'ERROR'
        continue

    # Check if first action is valid.

    if args[0] not in Actions:
        print 'ERROR'
        continue

    # Run command.

    if not Actions[args[0]](args[1:]):
        print 'ERROR'
