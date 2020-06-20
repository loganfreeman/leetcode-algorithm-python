class UnionFind(object):
    """Disjoint Set data structure supporting union and find operations used
    for Kruskal's MST algorithm
    Methods -
        insert(a, b) -> inserts 2 items in the sets
        get_leader(a) -> returns the leader(representative) corresponding to item a
        make_union(leadera, leaderb) -> unions two sets with leadera and leaderb
        in O(nlogn) time where n the number of elements in the data structure
        count_keys() -> returns the number of groups in the data structure
    """

    def __init__(self):
        self.leader = {}
        self.group = {}
        self.__repr__ = self.__str__

    def __str__(self):
        return str(self.group)

    def get_sets(self):
        """return a list of all of the sets
        """
        return [i[1] for i in self.group.items()]

    def insert(self, a, b=None):
        leadera = self.get_leader(a)
        leaderb = self.get_leader(b)
        if not b:
            if a not in self.leader:
                self.leader[a] = a
                self.group[a] = set([a])
                return
        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return
                self.make_union(leadera, leaderb)
            else:
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])

    def get_leader(self, a):
        return self.leader.get(a)

    def count_groups(self):
        return len(self.group)
    def make_union(self, leadera, leaderb):
        if leadera not in self.group or leaderb not in self.group:
            raise Exception("Invalid leader specified leadera -%s, leaderb - %s" % (leadera, leaderb))
        groupa = self.group[leadera]
        groupb = self.group[leaderb]
        if len(groupa) < len(groupb):
            # swap a and b if a is smaller
            leadera, groupa, leaderb, groupb = leaderb, groupb, leadera, groupa
        groupa |= groupb
        del self.group[leaderb]
        for k in groupb:
            self.leader[k] = leadera


