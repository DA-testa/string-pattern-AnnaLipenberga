# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    try:
        
        # replace input_string with the input that you want to provide
        #input_string = input()
        
        input_type = input().strip()
        if input_type == 'I':
            pattern = input().strip()
            text = input().strip()
        elif input_type == 'F':
            file_path = "test/" + "06"
            with open(file_path, 'r') as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        else:
            raise ValueError("Invalid input type")
        
        return (pattern, text)
    
    except EOFError:
        print("Error: Input source is empty")
        return None
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
   # return (input().rstrip(), input().rstrip()) -----

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)
    q = 997
    d = 256
    h = pow(d, p-1) % q
    p_hash = 0
    t_hash = 0
    occurrences = []
    
    for i in range(p):
        p_hash = (d*p_hash+ord(pattern[i])) % q
        t_hash = (d*t_hash+ord(text[i])) % q
        
    for s in range(t-p+1):
        if p_hash == t_hash:
            match = True
            for i in range(p):
                if text[s+i] != pattern[i]:
                    match = False
                    break
            if match:
                occurrences.append(s)
        if s < t-p:
            t_hash = (d*(t_hash - ord(text[s])*h) + ord(text[s+p])) % q
            
    return occurrences
            

    # and return an iterable variable
   # return [0]


# this part launches the functions
if __name__ == '__main__':
    inputs = read_input()
    if inputs is not None:
        print_occurrences(get_occurrences(*inputs))

