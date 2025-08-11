import speech_recognition as sr
from testeselenium2 import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações iniciais
print("Iniciando o sistema de voz para Libras...")

# 1. Configuração do Reconhecimento de Voz
def capturar_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Fale agora (aguarde o sinal)...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"✅ Texto reconhecido: {texto}")
            return texto
        except sr.UnknownValueError:
            print("❌ Não foi possível entender a fala")
            return None
        except sr.RequestError:
            print("❌ Erro no serviço de reconhecimento")
            return None

# 2. Configuração do Selenium
def configurar_navegador():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Permissão automática do microfone
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("\n🌐 Navegador configurado com sucesso!")
        return driver
    except Exception as e:
        print(f"\n❌ Erro ao configurar o navegador: {str(e)}")
        return None

# 3. Função principal
def main():
    # Configura o navegador
    driver = configurar_navegador()
    if not driver:
        return

    try:
        # Abre o VLibras
        driver.get("https://vlibras.gov.br/app/")
        time.sleep(5)  # Espera o site carregar

        # Captura a voz
        texto = capturar_voz()
        if not texto:
            return

        # Envia para o VLibras
        try:
            campo = driver.find_element(By.XPATH, '//div[@role="textbox"]')
            campo.clear()
            campo.send_keys(texto)
            print("\n🔄 Enviando para o VLibras...")
            time.sleep(3)  # Tempo para a tradução
            
            print("\n🎉 Tradução em Libras concluída!")
            print("O vídeo em Libras está sendo exibido na janela do navegador.")
            
            # Mantém o navegador aberto
            input("\nPressione ENTER para sair...")
            
        except Exception as e:
            print(f"\n❌ Erro ao enviar para o VLibras: {str(e)}")
            print("Verifique se o XPath do campo de texto está atualizado.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
