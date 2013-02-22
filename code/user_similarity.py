from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
from itertools import permutations

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    #Map 1
    def extract_users_with_businesses(self, _, record):
        """Take in a record, filter by review and yield <user_id, business_id>
        """
        if record['type'] == 'review':
            yield (record['user_id'], record['business_id'])
    #Red 1
    def count_businesses_per_user(self, user, businesses):
        businesses = set(businesses)
        businesses = list(businesses)
        count = len(businesses)
        #yield [user, [businesses, count]]
        yield (user, (businesses, count))
        
    #Map 2
    def group_by_business(self, user, businesses_count):
        businesses, count = businesses_count[0], businesses_count[1]
        businesses = list(businesses)
        count = len(businesses)
        for business in businesses:
            yield (business, (user, count))
    #Red 2
    def generic_reducer(self, business, users_c):
        users_c = list(users_c)
        users_c = [tuple(u) for u in users_c]
        yield (business, users_c)

    #Map 3
    def create_userpairs(self, business, users_c):

        users_c_tuple = [tuple(user_c) for user_c in users_c]
        users_c_pairs = [frozenset(perm) for perm in permutations(users_c_tuple, 2)]
        users_c_pairs_unique = set(users_c_pairs)


        for pair in users_c_pairs_unique:
            u1, u2 = pair
            u_id1, c1 = u1[0], u2[1]
            u_id2, c2 = u2[0], u2[1]
            yield ((u_id1, u_id2), c1+c2)
    #Red 3
    def calculate_jaccard (self, user_pair, c):
        c = list(c)
        jaccard = float(len(c))/float((c[0]-len(c)))
        if jaccard >= 0.5:
            yield (user_pair, jaccard)

    
    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <user_id, business_id>
        reducer1: <user_id, [business_id]> => <user_id, ([business_id], count)>

        mapper2: <user_id, ([business_id], count)> => <business_id, (user_id, count)>
        reducer2: no reducer: <b_id, [(u_id, count)]> => <b_id, [(u_id, count)]>

        group by b_id and output user_id pairs for earch combination of users who reviewd a business, add counts:  C = count1+count2 
        mapper3: <b_id, [(u_id, count)]> => <(u_id1, u_id2), C>

        len([C]) = |user_1 intersec user2|, C - len([C])  = |user_1 union user_2|
        reducer3: <(u_id1, u_id2), [C]> => <(u_id1, u_id2), len([C])/(C - len([C])>

      
        ##NOT ASKED BY ASSINGMENT
        mapper4: <(u_id1, u_id2), jaccard> => <"MAX", ((u_id1, u_id2), jaccard)> 
        reduce4: <"MAX", [((u_id1, u_id2), jaccard)] => <(u_id1, u_id2), jaccard>
        
        """
        # return [self.mr(mapper=self.extract_users_with_businesses, 
        #                 reducer=self.count_businesses_per_user),
        #         self.mr(mapper=self.group_by_business),
    

        return [self.mr(mapper=self.extract_users_with_businesses,                           reducer=self.count_businesses_per_user),
                self.mr(mapper=self.group_by_business,
                        reducer=self.generic_reducer),
                self.mr(mapper=self.create_userpairs,
                        reducer=self.calculate_jaccard)]

if __name__ == '__main__':
    UserSimilarity.run()
