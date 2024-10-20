class Polynomial1:
    def __init__(self,coefs): 
        self.coefficients = coefs 

        # the __init__ method is used to initialise 
        # object attributes (e.g. coefficients) with values 
        # passed as arguments (in this case coefs) 

        # By convention, the first parameter to any instance method
        # is self. 

    def degree(self):
        return len(self.coefficents)-1
    
    def __str__(self):
        coefs = self.coefficients
        terms = []
        # degree 0 and 1 terms conventionally have different representations
        if coefs[0]:
            terms.append(str[coefs[0]])
        if self.degree() and coefs[1]:
            terms.append(f'{'' if coefs[1]==1 else coefs[1]}x')
        terms += [f"{'' if c == 1 else c}x^{d}" for d,c in enumerate(coefs[2:], start = 2)]
        
        return '+'.join(reversed(terms)) or "0"
    
    # object equality

    def __eq__(self,other):
        return self.coefficents == other.coefficients
    
    # polynomial addition

    def __add__(self,other):
        if isinstance(other,Polynomial1):
            common = min(self.degree(),other.degree)+1
            coefs = tuple(a+b for a,b in zip(self.coefficients,other.coefficients))
            coefs+= self.coefficients[common:]+other.coefficients[common:]
            return Polynomial1(coefs)
        elif isinstance(other,Number):
            return Polynomial1((self.coefficients[0]+other,)+self.coefficients[1:])
        else:
            return NotImplemented
    def __radd__(self,other):
        return self+other
