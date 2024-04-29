import psutil,time,os

def discord_info():
    discord_processes = [p for p in psutil.process_iter() if p.name() == "Discord.exe"]
    if discord_processes:
        process = discord_processes[0]
        process_exe = process.exe()
        monitor_discord(process_exe)
    else:
        print("where discord :(")

def monitor_discord(discord_location:str):
    while True:
        discord_processes = [p for p in psutil.process_iter() if p.name() == 'Discord.exe']
        if not discord_processes:
            os.system(discord_location)
        time.sleep(10)

if __name__ == "__main__":
    discord_info()