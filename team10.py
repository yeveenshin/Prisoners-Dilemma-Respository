

team_name = 'AprilMac'
strategy_name = 'Infinite Betrayal'
strategy_description = 'Start nice, betray to win'
    
def move(my_history, their_history, my_score, their_score):
   
    if len(my_history) == 0:
        return 'b'
    elif len(my_history) == 1:
        return 'c'
    else:
        return 'b'


    
    
  
