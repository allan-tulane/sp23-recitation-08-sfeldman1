
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookyb-ird'), ('-elephant', 'rele-vant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  if (T, S) in MED:
    return MED[(T, S)]
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else: 
    if (S[0] == T[0]):
      return (fast_MED(S[1:], T[1:], MED))
    else:   
      opt1 = fast_MED(S, T[1:], MED) + 1
      opt2 = fast_MED(S[1:], T, MED) + 1
      opt3 = fast_MED(S[1:], T[1:], MED) + 1
      med = min(opt1, opt2, opt3)

  MED[(S, T)] = med
  return med
  
def fast_align_MED(S, T, MED={}):
  if (S == ""):
    return ('-' * len(T),T)
  elif (T == ""):
    return ('-' * len(S), S)
  else: 
    if (S[0] == T[0]):
      x = fast_align_MED(S[1:], T[1:], MED)
      return (S[0] + x[0], T[0] + x[1])
    else:
      opt1 = fast_MED(S, T[1:], MED) + 1
      opt2 = fast_MED(S[1:], T, MED) + 1
      opt3 = fast_MED(S[1:], T[1:], MED) + 1
      med = min(opt1, opt2, opt3)

      if med == opt1:
        return ('-' + (fast_align_MED(S, T[1:], MED))[0], T[0] + (fast_align_MED(S, T[1:], MED))[1])
      elif med == opt2:
        return (S[0] + (fast_align_MED(S[1:], T, MED))[0], '-' + (fast_align_MED(S[1:], T, MED))[1])
      else:
        return (S[0] + (fast_align_MED(S[1:], T[1:], MED))[0], T[0] + (fast_align_MED(S[1:], T[1:], MED))[1])
        
        
        
    

  
    # TODO - keep track of alignment
    pass

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
