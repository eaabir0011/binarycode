import speedtest

def check_speed():
    st=speedtest.Speedtest()
    download_speed=st.download()/10**6 
    upload_speed=st.upload()/10**6
    print(f"download_Speed:{download_speed:.2f} MBPS")
    print(f"upload_Speed:{upload_speed:.2f} MBPS")

check_speed()