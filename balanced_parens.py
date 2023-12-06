def balanced_parens(n):
    ret = []

    def generate(parans, openings, closings):
        if openings == 0 and closings == 0:
            ret.append(parans)
            return
        elif openings == 0:
            ret.append(parans + ")" * closings)
            return
        if openings < closings:
            generate(parans + ")", openings, closings-1)
        generate(parans +"(", openings-1, closings)
    
    generate("", n, n)
    return ret
