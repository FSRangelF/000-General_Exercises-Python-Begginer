def notas(*num, sit=False):
    """
    => Função para analisar notas de varios alunos e situação da turma
    :param num: umaou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve incluir a situação da turma
    :return: dicionario com várias informações sobre a turma
    """
    resumo = dict()
    maior = menor = media = 0
    if len(num) != 0:
        maior = max(num)
        menor = min(num)
        media = sum(num) / len(num)
    resumo['total'] = len(num)
    resumo['maior'] = maior
    resumo['menor'] = menor
    resumo['média'] = media
    if sit:
        if media < 5:
            resumo['situação'] = 'RUIM'
        elif 5 <= media < 7:
            resumo['situação'] = 'RAZOÁVEL'
        else:
            resumo['situação'] = 'BOA'
    return resumo


#
resp = notas(1, 5, 6, 8, 9, 8.5, 10, 5, 7, sit=True)
print(resp)
help(notas)