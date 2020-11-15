def user_input():
    '''
    Takes user inputs for setting up durations of pomodoro session
    interval: Pomodoro interval duration specified
    break_duration: break time duration specified
    total_duration: total number of sessions 
    Returns integers for each variable
    '''
    interval = int(input('Please Enter duration (mins) of interval: '))
    break_duration = int(input('Please Enter break duration(mins) of interval: '))
    total_duration = int(input('Please enter number of sessions: '))
    return interval, total_duration, break_duration

def countdown(interval):
    '''
    Dynamic minute and second countdown
    '''
    
    for j in range(interval-1,-1,-1):
        for i in range(59,-1,-1):
            if i <= 9: 
                #sys.stdout.write("Duration: Minutes "+str(j)+ "Seconds 0"+str(i)+ "to go")
                #sys.stdout.write('{:02d}:{:02d}'.format(j, i))
                print("Duration: Minutes "+ str(j) + " Seconds: 0" +str(i),end="\r")
            else:
                #sys.stdout.write('{:02d}:{:02d}'.format(j, i))
                print("Duration: Minutes "+ str(j) + " Seconds: " + str(i),end="\r")
            sys.stdout.flush()
            time.sleep(1)

if __name__ == "__main__":
    session_count = 0
    interval, total_duration, break_duration = user_input()
    print("interval: ",interval)
    print("total breaks: ", total_duration)
    print("break duration: ", break_duration)
    
    
    while session_count < total_duration:
        
        countdown(interval)
        
        print('\nBreak time!')
        countdown(break_duration)
        session_count += 1
        print('\nsession number: ',session_count,end='\r')
    
    print('\nEnd of Session!')
