#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # find Ticket with source NONE
    # linked list! 
    
    cache = []
    results = []

    if length == 0:
        return

    if ticket

    return route


'''
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]

Your function should output an array of strings with the entire route of
your trip. For the above example, it should look like this:

["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
'''