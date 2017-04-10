import json

def clean_json(json):
    unusable = json.dumps(json)
    usable = json.loads(unusable)
    return usable

class user_info:
    def __init__(self, usablejson):
        self.name = usablejson['name']
        self.brawlhalla_id = usablejson['brawlhalla_id']
        self.level = usablejson['level']
