import streamlit as st
import google.generativeai as genai
import time

# 1. Configuração inicial da página (DEVE ser a primeira linha do Streamlit)
st.set_page_config(page_title="Motor SEO Pro", page_icon="⚡", layout="centered")

# --- INJEÇÃO DE CSS PARA MOTION DESIGN E ESTÉTICA ---
st.markdown("""
<style>
    /* Fundo escuro premium */
    .stApp {
        background-color: #0A0A0B;
    }
    
    /* Efeito de Gradiente no Título Principal com Animação */
    .titulo-glow {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: fadeInDown 1s ease-out;
        margin-bottom: 0px;
    }
    
    .subtitulo {
        text-align: center;
        color: #A0AEC0;
        font-size: 1.1rem;
        margin-bottom: 40px;
        animation: fadeInDown 1.2s ease-out;
    }

    /* O Efeito de Vidro (Glassmorphism) para os resultados */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 30px;
        margin-top: 30px;
        color: #E2E8F0;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(0, 201, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Keyframes para Motion Design de entrada */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Escondendo a marca d'água do Streamlit para ficar profissional */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- FIM DO CSS ---

# Configuração da Inteligência Artificial
CHAVE_API = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=CHAVE_API)
modelo = genai.GenerativeModel('gemini-3.5-flash')

# Interface Visual (Frontend)
st.markdown('<p class="titulo-glow">Motor SEO Inteligente</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Gere títulos de alta conversão e tags ocultas em segundos.</p>', unsafe_allow_html=True)

# Campo de digitação
produto_usuario = st.text_input("Qual produto vamos ranquear hoje?", placeholder="Ex: Calça jeans bootcut lavagem escura...")

# Botão de ação
if st.button("Gerar Estratégia de Ranqueamento 🚀", use_container_width=True):
    if produto_usuario:
        # Barra de carregamento estilizada
        with st.spinner("Analisando o algoritmo dos marketplaces..."):
            
            comando_para_ia = f"""
            Atue como um especialista em copy para e-commerce focado em alta conversão.
            O meu produto é: {produto_usuario}
            
            Formate a resposta em HTML limpo (apenas tags <h3>, <ul>, <li>, <p>, <strong>), sem marcações de markdown (` ```html `).
            
            Crie:
            <h3>🔥 Títulos Agressivos (Máx 60 caracteres)</h3>
            [Lista de 3 títulos usando cauda longa]
            
            <h3>🏷️ Tags Ocultas (As mais pesquisadas)</h3>
            [Lista separada por vírgulas com as 15 melhores tags]
            
            <h3>✍️ Descrição Magnética (Quebra de Objeções)</h3>
            [Crie a descrição do produto estritamente em formato de TÓPICOS usando as tags <ul> e <li>. 
            Em vez de apenas descrever, use cada tópico para antecipar e MATAR uma objeção comum do cliente ao comprar roupas online (exemplo de focos: não fica transparente, costura reforçada para não abrir, modelagem que valoriza sem apertar, tecido que não encolhe ou desbota na lavagem). Destaque a qualidade premium e passe extrema segurança para o comprador.]
            """
            
            # Chama a IA
            resposta = modelo.generate_content(comando_para_ia)
            
            # Exibe o resultado dentro do nosso Card de Vidro com animação
            st.markdown(f'<div class="glass-card">{resposta.text}</div>', unsafe_allow_html=True)
            
            st.success("SEO gerado com sucesso!")
            st.balloons() # Uma pequena animação de comemoração
    else:
        st.warning("Por favor, descreva o produto antes de gerar.")
