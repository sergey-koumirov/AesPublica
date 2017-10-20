import yaml

from app import db
from app.eve_models import EveType, EveMarketGroup, EveGroup, EveCategory


def parse_categories(file):
    print(".... loading categories")
    data = yaml.load(file, Loader=yaml.CLoader)
    for key in data:
        print(key, data[key]['name'].get('en','N/A'))
        item = EveCategory.query.get(key)
        if not item:
            item = EveCategory(id=key)
        item.icon_id = data[key].get('iconID',None)
        item.published = data[key]['published']
        item.name = data[key]['name']['en']
        db.session.add(item)
        db.session.commit()

def parse_groups(file):
    print(".... loadinggroups")
    data = yaml.load(file, Loader=yaml.CLoader)
    for key in data:
        print(key, data[key]['name'].get('en','N/A'))
        item = EveGroup.query.get(key)
        if not item:
            item = EveGroup(id=key)
        item.category_id = data[key]['categoryID']
        item.icon_id = data[key].get('iconID',None)
        item.published = data[key]['published']
        item.name = data[key]['name']['en']
        db.session.add(item)
        db.session.commit()


def parse_market_groups(file):
    print(".... loading market groups")
    data = yaml.load(file, Loader=yaml.CLoader)
    for record in data:
        key = record['marketGroupID']
        # print(key, record['marketGroupName'])
        item = EveMarketGroup.query.get(key)
        if not item:
            item = EveMarketGroup(id=key)
        item.name = record['marketGroupName']
        item.description = record.get('description','N/A')
        item.has_types = record['hasTypes']
        item.icon_id = record.get('iconID',None)
        item.parent_id = record.get('parentGroupID',None)
        db.session.add(item)
        db.session.commit()


def parse_type_ids(file):
    print(".... loading type IDs")
    data = yaml.load(file, Loader=yaml.CLoader)
    for key in data:
        print(key, data[key]['name'].get('en','N/A'))
        item = EveType.query.get(key)
        if not item:
            item = EveType(id=key)
        item.group_id = data[key].get('groupID',None)
        item.market_group_id = data[key].get('marketGroupID',None)
        item.volume = data[key].get('volume',None)
        item.name = data[key]['name'].get('en','N/A')
        item.portion_size = data[key]['portionSize']
        item.published = data[key]['published']
        db.session.add(item)
        db.session.commit()