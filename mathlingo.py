# -*- coding: utf-8 -*-
"""
Created on Fri May 29 02:33:45 2020

@author: FFernandes
"""

#MATHLINGO

import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)


'''
print('Olá! Qual seu nome?')
nome = input()
print('Bom ver você de novo, {}!'.format(nome))


def fase1():
    times = 1
    grade = []
    for time in range(times):
        num1 = np.random.randint(low = 0, high = 10)
        num2 = np.random.randint(low = 0, high = 10)
        print('Qual a soma de {:d} mais {:d}?'.format(num1, num2))
        answer = input()
        if (int(answer) == num1 + num2):
            grade.append(1)
            print('Resposta certa!!')
        else:
            grade.append(0)
            print('Resposta errada')
            
    finalgrade = np.array(grade).sum()
    print('{}, você fez {:d} pontos na fase 1!'.format(nome, finalgrade))
    
    return finalgrade
    
def fase2():
    times = 1
    grade = []
    for time in range(times):
        num1 = np.random.randint(low = 10, high = 100)
        num2 = np.random.randint(low = 0, high = 100)
        print('Qual a soma de {:d} mais {:d}?'.format(num1, num2))
        answer = input()
        if (int(answer) == num1 + num2):
            grade.append(1)
            print('Resposta certa!!')
        else:
            grade.append(0)
            print('Resposta errada')
            
    finalgrade = np.array(grade).sum()
    print('{}, você fez {:d} pontos na fase 2!'.format(nome, finalgrade))
    
    return finalgrade
    

def fase3():
    times = 1
    grade = []
    for time in range(times):
        num1 = np.random.randint(low = 100, high = 10000)
        num2 = np.random.randint(low = 0, high = 10000)
        print('Qual a soma de {:d} mais {:d}?'.format(num1, num2))
        answer = input()
        if (int(answer) == num1 + num2):
            grade.append(1)
            print('Resposta certa!!')
        else:
            grade.append(0)
            print('Resposta errada')
            
    finalgrade = np.array(grade).sum()
    print('{}, você fez {:d} pontos na fase 3!'.format(nome, finalgrade))
    
    return finalgrade

def fase4():
    times = 10
    grade = []
    for time in range(times):
        num1 = np.random.randint(low = 5, high = 10)
        num2 = np.random.randint(low = 0, high = num1)
        print('Qual é a subtração de {:d} menos {:d}?'.format(num1, num2))
        answer = input()
        if (int(answer) == num1 - num2):
            grade.append(1)
            print('Resposta certa!!')
        else:
            grade.append(0)
            print('Resposta errada')
            
    finalgrade = np.array(grade).sum()
    print('{}, você fez {:d} pontos na fase 4!'.format(nome, finalgrade))
    
    return finalgrade


functions = [fase1, fase2, fase3, fase4]
output = []
for fase in functions:
    output.append(fase())

overall_grade = np.array(output).sum()
print('{}, você fez no total {:d} pontos no jogo!'.format(nome, overall_grade))
'''    


