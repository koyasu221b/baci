def reverse_string(astring):

    if len(astring) == 1 or len(astring) == 0:
        return astring

    head = astring[0]
    tail = astring[1:]
    reverse_tail = reverse_string(tail)
    return reverse_tail + head


astring = "ABC123"
actual = reverse_string(astring)
expected = "321CBA"

if actual == expected:
    print "pass"
