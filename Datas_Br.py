from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=30, minutes=20,seconds=30)
        return agora - self.data_cadastro

    def mes_cadastro(self):
        meses_do_ano=[
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.data_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terca", "quarta", "quinta",
            "sexta", "sabado", "domingo"
        ]
        dia_semana = self.data_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada