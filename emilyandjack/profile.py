import json, os

static_dir = 'emilyandjack/static/'

class Profile:
    """
    Attributes for this class:
        fname:  First Name
        lname:  Last Name
        nname:  Nickname
        loc:    Location
        desc:   Description
    """
    def __init__(self, d):
        self.__dict__.update(d)

    def __repr__(self):
        return ('<Profile %r, %r, %r, %r, %r>') % (self.fname, self.lname, \
            self.nname, self.loc, self.desc)

def load_from_json(json_data):
    pdict = {}
    profiles_list = []
    profiles_list = json_data['profiles']

    for item in profiles_list:
        p = Profile(item)
        pdict[p.fname.lower()] = p
    
    return pdict

