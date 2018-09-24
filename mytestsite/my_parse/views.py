from django.shortcuts import render

def index(request):
    """View function for home page of site."""

    alpha = []
    bravo = []
    charlie = []
    delta = []
    echo = []
    anomalous = []
    total_all_messages = []

    char = ''

    with open ('data.txt', 'rt') as f:
        lines = f.readlines()

        for char in lines:
            if char[5] == "A":
                alpha.append(char)
            elif char[5] == "B":
                bravo.append(char)
            elif char[5] == "C":
                charlie.append(char)
            elif char[5] == "D":
                delta.append(char)
            elif char[5] == "E":
                echo.append(char)
            else:
                anomalous.append(char)

    for line in lines:
        total_all_messages.append(line)

    context = {
        'alpha': alpha,
        'bravo': bravo,
        'charlie': charlie,
        'delta': delta,
        'echo': echo,
        'anomalous': anomalous,
        'total_all_messages': total_all_messages,
        }
    
    return render(request, 'index.html', context=context)
    
    

    
