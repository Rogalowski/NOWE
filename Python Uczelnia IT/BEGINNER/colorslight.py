inputRed = bool(input('red on? switch if yes:'))
inputGreen =  bool(input('green on? switch if yes:'))
inputBlue =  bool(input('blue on? switch if yes:'))

light = {
    
    (True, False, False): 'red light on',
    (False, True, False): 'green light on',
    (False, False, True): 'blue light on',
    (True, True, False): 'yellow light on',
    (False, True, True): 'teal light on',
    (True, True, True): 'white light on',
    (False, False, False): 'light off',
    
}

print(light[inputRed, inputGreen, inputBlue])

