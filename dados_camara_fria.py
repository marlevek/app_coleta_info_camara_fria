import streamlit as st
import pandas as pd
from datetime import date, datetime

# Função formatar data padrão brasileiro
def formatar_data(data):
   return data.strftime("%d/%m/%Y")

# Configurar página e ícone
st.set_page_config('Levantamento de Dados Câmara Fria', page_icon=':material/severe_cold:')

# Título
st.title('Coleta de Informações - Câmara Fria :material/warehouse:')

# Cliente e queixa
cliente = st.text_input('Cliente:')
queixa = st.text_input('Queixa:')

# Seção Câmara:
st.subheader('Câmara')
tipo_camara = st.radio('Tipo:', ['Resfriados', 'Congelados'])

# Seção Evaporador e dreno
st.subheader('Evaporador e Dreno')
modelo_evaporador = st.text_input('Modelo do Evaporador:')
serpentina_limpa = st.radio('Serpentina Limpa?', ['Sim', 'Não'])
dreno_limpo = st.radio('Dreno Limpo?', ['Sim', 'Não'])
material_dreno = st.radio('Material do Dreno', ['PVC', 'Mangueira'])

# Seção Sistema de Expansão
st.subheader('Sistema de Expansão')
sistema_expansao = st.radio('Sistema de Expansão', ['Tubo Capilar', 'Válvula de Expansão'])
if sistema_expansao == 'Válvula de Expansão':
    tipo_valvula = st.radio('Tipo de Válvula de Expansão', ['Manual', 'Termostática', 'Eletrônica'])

# Seção Controlador Digital
st.subheader('Controlador Digital')
marca_controlador = st.text_input('Marca:')
modelo_controlador = st.text_input('Modelo:')
sem_controlador = st.checkbox('Não tem')

# Seção Condensador e Compressor
st.subheader('Condensador e Compressor')
modelo_unidade_condensadora = st.text_input('Modelo da Unidade Condensadora:')
modelo_compressor = st.text_input('Modelo do Compressor:')
serpentina_cond_limpa = st.radio('Serpentina Suja?', ['Sim', 'Não'])
rla_compressor = st.number_input('RLA Compressor:', min_value=0.0)
corrente_funcionamento = st.number_input('Corrente de Funcionamento:', min_value=0.0)
tensao = st.number_input('Tensão (V):', min_value=0)

# Seção Componentes
st.subheader('Componentes')
solenoide = st.radio('Solenoide:', ['Sim', 'Não'])
if solenoide == 'Sim':
    tensao_solenoide = st.number_input('Tensão Solenoide (V):', min_value=0)
visor_liquido = st.radio('Visor de Líquido?', ['Sim', 'Não'])
separador_liquido = st.radio('Separador de Líquido?', ['Sim', 'Não'])
tanque_liquido = st.radio('Tanque de Líquido?', ['Sim', 'Não'])
separador_oleo = st.radio('Separador de Óleo?', ['Sim', 'Não'])
pressostato = st.radio('Pressostato?', ['Sim', 'Não'])
if pressostato == 'Sim':
    modelo_pressostato = st.text_input('Modelo Pressostato:')
    tipo_pressostato = st.radio('Tipo do Pressostato', ['Baixa', 'Alta', 'Conjugado'])
filtro_secador = st.radio('Filtro Secador?', ['Sim', 'Não'])
if filtro_secador == 'Sim':
    conexao_filtro = st.radio('Conexaõ do Filtro Secador:', ['Solda', 'Flange'])

# Seção de Pressões e Temperaturas
st.subheader('Pressões e Temperaturas')
fluido_refrigerante = st.text_input('Fluido Refrigerante:')
pressao_succao = st.number_input('Pressão de Sucção (Psi):', min_value=0.0)
pressao_condensacao = st.number_input('Pressão de Condensação (Psi):', min_value=0.0)
temp_succao = st.number_input('Temperatura de Sucção:', min_value=0.0)
temp_condensacao = st.number_input('Temperatura de Condensação:', min_value=0.0)
superaquecimento = st.number_input('Superaquecimento (k):', min_value=0.0)
subresfriamento = st.number_input('Subresfriamento (k):', min_value=0.0)

# Observaçõe
observacoes = st.text_area('Observações:')

# Data
data_atual = date.today()
data = data_atual
data_formatada = formatar_data(data)
st.write(f'Data: {data_formatada}')


# Botão para salvar as informações
if st.button("Salvar Informações"):
    # Coletando todos os dados em um dicionário
    dados = {
        "Cliente": cliente,
        "Queixa": queixa,
        "Tipo de Câmara": tipo_camara,
        "Modelo Evaporador": modelo_evaporador,
        "Serpentina Limpa": serpentina_limpa,
        "Dreno Limpo": dreno_limpo,
        "Material Dreno": material_dreno,
        "Sistema de Expansão": sistema_expansao,
        "Tipo Válvula Expansão": tipo_valvula if sistema_expansao == "Válvula de Expansão" else None,
        "Marca Controlador": marca_controlador,
        "Modelo Controlador": modelo_controlador,
        "Sem Controlador": sem_controlador,
        "Modelo Unidade Condensadora": modelo_unidade_condensadora,
        "Modelo Compressor": modelo_compressor,
        "Serpentina Limpa": serpentina_cond_limpa,
        "RLA Compressor": rla_compressor,
        "Corrente de Funcionamento": corrente_funcionamento,
        "Tensão": tensao,
        "Solenoide": solenoide,
        "Tensão Solenoide": tensao_solenoide if solenoide == "Sim" else None,
        "Visor Líquido": visor_liquido,
        "Separador de Líquido": separador_liquido,
        "Tanque de Líquido": tanque_liquido,
        "Filtro Secador": filtro_secador,
        "Conexão Filtro": conexao_filtro if filtro_secador == "Sim" else None,
        "Pressostato": pressostato,
        "Fluido Refrigerante": fluido_refrigerante,
        "Pressão Sucção": pressao_succao,
        "Pressão Condensação": pressao_condensacao,
        "Temperatura Sucção": temp_succao,
        "Temperatura Condensação": temp_condensacao,
        "Superaquecimento": superaquecimento,
        "Subresfriamento": subresfriamento,
        "Observações": observacoes,
        "Data": data_formatada,
    }
    
    # Transformando em DataFrame para salvar como CSV
    df = pd.DataFrame([dados])
    csv = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    
    # Botão de download
    st.download_button(
        label="Baixar Informações",
        data=csv,
        file_name="informacoes_camara.csv",
        mime="text/csv",
    )
    st.success("Informações salvas e prontas para download!")