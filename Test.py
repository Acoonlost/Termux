import speedtest

def testar_velocidade():
    # Criar um objeto Speedtest
    st = speedtest.Speedtest()
    
    # Testar a velocidade do download
    print("Testando velocidade de download...")
    velocidade_download = st.download() / 1024 / 1024  # Convertendo para Mbps
    print(f"Velocidade de download: {velocidade_download:.2f} Mbps")
    
    # Testar a velocidade do upload
    print("Testando velocidade de upload...")
    velocidade_upload = st.upload() / 1024 / 1024  # Convertendo para Mbps
    print(f"Velocidade de upload: {velocidade_upload:.2f} Mbps")
    
    # Testar a latência (ping)
    print("Testando latência (ping)...")
    latencia = st.results.ping
    print(f"Latência (ping): {latencia} ms")

if __name__ == "__main__":
    testar_velocidade()
