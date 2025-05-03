import requests
import json
from time import sleep

def capta_dados_IBGE():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Falha ao acessar a API - Código de status -> Capt: {response.status_code}")

def rankeando(municipal_id):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={municipal_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar a API - Código de status -> Rank: {response.status_code}")
    return response.json()

def process_municipalities():
    municipios = capta_dados_IBGE()
    gabriel_results = {}
    gabriel_top1_count = 0  # contador de municípios onde Gabriel é o 1º nome

    for mun in municipios:
        mun_id = mun["id"]
        mun_nome = mun["nome"]

        print(f"Processando: {mun_nome}")
        sleep(0.5)

        try:
            ranking_data = rankeando(mun_id)
        except Exception as e:
            print(f"Erro em {mun_nome}: {e}")
            continue

        if ranking_data and len(ranking_data) > 0:
            ranking = ranking_data[0].get('res', [])
            for idx, item in enumerate(ranking[:10]):
                nome = item['nome'].upper()
                if nome == 'GABRIEL':
                    gabriel_results[mun_nome] = item['frequencia']
                    if idx == 0:  # se for o 1º da lista (índice 0)
                        gabriel_top1_count += 1
                    break

    return gabriel_results, gabriel_top1_count

def save_to_json(data, filename='gabriel_top10.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    try:
        results, top1_count = process_municipalities()
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        save_to_json(sorted_results)

        print("\nProcesso concluído! Resultados salvos em gabriel_top10.json")
        print(f"Total de municípios com Gabriel no top 10: {len(sorted_results)}")
        print(f"Gabriel foi o nome MAIS popular (1º lugar) em {top1_count} municípios.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

main()
