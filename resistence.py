"""
Resistor Colour Codes
"""
def colour(r,c,p):
    color_map = {
        0: "BLK", 1: "BWN", 2: "RED", 3: "ONG",
        4: "YLW", 5: "GRN", 6: "BLU", 7: "VLT",
        8: "GRY", 9: "WHT"
    }
    if c<=0 or p<=0 or c>p:
        return "invalid"
        
    
    re=str(r)
    if len(re)<=2:
        return "invalid"
    first=int(re[0])
    second=int(re[1])
    last=len(re)-2
    return f"{color_map[first]}{color_map[second]}{color_map[last]}"
p=int(input())
c=int(input())
r=p//(c*c)
h=colour(r,c,p)
print(h)