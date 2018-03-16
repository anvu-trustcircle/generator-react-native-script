def yes_no_question(question):
  answer = raw_input(question + (' (y/n) '))
  
  simple_answer = answer.lower()
  if simple_answer in ['yes', 'y']:
    return True
  elif simple_answer in ['no', 'n']:
    return False
  else:
    return yes_no_question(question)

def yes_question(question):
  answer = raw_input(question + (' (yes/no) no: '))
  
  simple_answer = answer.lower()
  if simple_answer in ['yes', 'y']:
    return True
  elif simple_answer in ['', 'no', 'n']:
    return False
  else:
    return yes_question(question)