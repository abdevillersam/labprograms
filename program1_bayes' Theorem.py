def bayes_theorem(p_f,p_f_and_a):
  p_a_given_f = (p_f_and_a / p_f)
  return p_a_given_f

p_f = float(input('Enter value of P(F): '))
p_f_and_a = float(input('Enter value of P(F^A): '))
result = bayes_theorem(p_f,p_f_and_a)
print('Result P(A|F) = %.3f%%' % (result*100))