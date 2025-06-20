import socket

target = input("🔍 أدخل IP لفحصه: ")
ports = [21, 22, 80, 443, 8080]

print(f"\nبدء الفحص على {target}...\n")

for port in ports:
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ المنفذ {port} مفتوح")
    else:
        print(f"❌ المنفذ {port} مغلق")
    sock.close()

