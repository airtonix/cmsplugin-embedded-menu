import re

def deslugify(value):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.
    """
    reverse_map = {
      "_" : " ",
      "-" : " : ",
    }

    for _from, _to in reverse_map.iteritems():
        value = re.sub(_from, _to, value)
    return value
