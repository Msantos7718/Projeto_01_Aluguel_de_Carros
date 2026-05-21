import streamlit as st 
st.title ("Motorsney- Aluguel de carros")
st.subheader("O lugar aonde as lendas compram")
st.sidebar.title("Escolha um modelo")
st.sidebar.image('logo.png')


carros = ['BMW','Mustang','Porsche','Fusca','Toro']
opcao = st.sidebar.selectbox("Escolha o carro que deseja alugar",carros)


st.image(f"{opcao}.png")
st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("---")


dias= st.text_input(f' por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'quantos km voce rodou com o {opcao}')

if opcao == 'BMW' :
    diaria = 450

elif opcao =='Mustang':
    diaria = 500

elif opcao == 'Porsche':
    diaria = 500

elif opcao == ' fusca':
    diaria = 250

elif opcao == 'toro':
    diaria= 550


if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Vocé alugou o {dias} dias e rodou {km}. o valor total a pagar é R${aluguel_total:.2f}')