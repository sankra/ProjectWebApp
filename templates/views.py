from django.shortcuts import render
from .forms import UserInputForm

def process_input(user_input):
    # Example processing: reverse the string
    add_string = user_input[::-1] + ' VIJAY'
    return add_string

def game(request):
    if request.method == 'GET':
        return render(request, 'input_processor/game.html')

def user_input_view(request):
    result = ''
    form = UserInputForm(request.POST)
    print(request.POST)
    if form.is_valid():
        user_input = form.cleaned_data['user_input']
        result = process_input(user_input)
    return render(request, 'input_processor/user_input.html', {'form': form, 'result': result})

















'''
# Main view for the user input form
def user_input_view(request):
    result = None  # Placeholder for the processed result
    if request.method == 'POST':
        form = UserInputForm(request.POST)  # Bind data from POST request
        if form.is_valid():  # Validate the form
            user_input = form.cleaned_data['user_input']  # Get the input
            result = process_input(user_input)  # Process the input
    else:
        form = UserInputForm()  # Display an empty form for GET requests

    # Render the form and the result
    return render(request, 'input_processor/user_input.html', {'form': form, 'result': result})
'''