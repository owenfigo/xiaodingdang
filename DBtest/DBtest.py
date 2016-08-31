from CodernityDB.database import Database
from CodernityDB.hash_index import HashIndex


class WithXIndex(HashIndex):

    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = 'I'
        super(WithXIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        a_val = data.get("x")
        if a_val is not None:
            return a_val, None
        return None

    def make_key(self, key):
        return key


def main():
    db = Database('tmp/tut2')
    db.create()
    x_ind = WithXIndex(db.path, 'x')
    db.add_index(x_ind)

    for x in xrange(100):
        db.insert(dict(x=x))

    for y in xrange(100):
        db.insert(dict(y=y))

    for curr in db.all('id'):
        print curr
    print '*************************************'
    print db.get('x', 77, with_doc=True)
    print '*************************************'
    print db.count(db.all, 'id')
    print '*************************************'
    print db.count(db.all, 'x')


if __name__ == '__main__':
    main()
