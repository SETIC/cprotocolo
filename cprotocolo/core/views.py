from django.shortcuts import render
import requests, json
from django.conf import settings as con


def new_search(request):
    return empty_form(request)


def empty_form(request):
    return render(request, 'index.html')


def error_form(request, try_search):
    return render(request, 'index.html', {'numero': try_search, 'error': True})


def search(request):
    number_protocolo = request.GET.get('numProtocolo')
    response = requests.get(con.SERVER_PATH, params={'numero': number_protocolo})
    data = json.loads(response.content.decode("utf-8"))

    if data:
        return render(request, 'index.html', {'numero': data[0]['numero'],
                                              'justificativa': data[0]['descricao_situacao'],
                                              'interessado': data[0]['interessado'],
                                              'status_protocolo': data[0]['status_protocolo'],
                                              'numProtocolo': data})
    return error_form(request, number_protocolo)
