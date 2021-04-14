def reverse(s, ind):
    if len(s) == ind:
        return
    
    reverse(s, ind+1)
    print(s[ind])

reverse("suresh", 0)