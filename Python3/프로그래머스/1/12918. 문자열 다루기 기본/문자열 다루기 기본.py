def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    try:
        int(s)
    except:
        return False
    
    return True