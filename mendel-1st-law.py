# k = homozygous dominant (AA)
# m = heterozygous (Aa)
# n = homozygous recessive (aa)

def mendel_prob(k, m, n):
    k = float(k)
    m = float(m)
    n = float(n)
    pop = k + m + n
    
    k_equation = ((k/pop) * ((k-1)/(pop-1))) + ((k/pop) * (m/(pop-1))) + ((k/pop) * (n/(pop-1)))
    m_equation = ((m/pop) * (k/(pop-1))) + ((m/pop) * ((m-1)/(pop-1))*0.75) + ((m/pop) * (n/(pop-1))*0.5)
    n_equation = ((n/pop) * (k/(pop-1))) + ((n/pop) * (m/(pop-1))*0.5) + ((n/pop) * ((n-1)/(pop-1))*0)
    equation = k_equation + m_equation + n_equation
    return equation

print(mendel_prob(23, 23, 24))