import datetime
import pandas as pd
hora_atual  = datetime.datetime.now()

hora_atual, minuto = datetime.datetime.time(hora_atual).hour, datetime.datetime.time(hora_atual).minute

#print('hora atual',hora_atual)
#print('minuto',minuto)

data_atual = datetime.datetime.now()
#print('data atual',data_atual)


planilha_agenda = 'D:\\app\\ProjectPython\\assitenteMaria\\agenda.xlsx'

agenda = pd.read_excel(planilha_agenda)
#print('***agenda***')
#print(agenda)


descricao, responsavel, hora_agenda = [], [], []
#print(descricao, responsavel, hora_agenda)

for index, row in agenda.iterrows():
    data = datetime.datetime.date(row['data'])

    hora_completa = row['hora'].strftime('%H:%M:%S')

    # Converte a string formatada para um objeto datetime.time
    hora_obj = datetime.datetime.strptime(hora_completa, '%H:%M:%S').time()

    # Extrai a hora do objeto datetime.time
    hora = hora_obj.hour

    #print('data, hora completa, hora obj, horas', data, hora_completa, hora_obj, hora)

#Buscar atividade maior que a data e hora atual
    if data_atual.date() <= data:
        if hora >= hora_atual:
            descricao.append(row['descricao'])
            responsavel.append(row['responsavel'])
            hora_agenda.append(row['hora'])


#print(row['descricao'])
#print(row['responsavel'])
#print(row['hora'])
#print(descricao)
#print(responsavel)
#print(hora_agenda)

#mostrar se
def carrega_agenda():
    if descricao:
        return descricao, responsavel, hora_agenda;
    else:
        return False