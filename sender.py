import os
import socket
import struct
from des_socket_utils import encrypt_des_cbc, build_packet

SERVER_IP = os.getenv('SERVER_IP', '127.0.0.1')
SERVER_PORT = int(os.getenv('SERVER_PORT', '6000'))
MESSAGE_ENV = os.getenv('MESSAGE')
LOG_FILE = os.getenv('SENDER_LOG_FILE', '')


def get_message() -> bytes:
    if MESSAGE_ENV is not None:
        return MESSAGE_ENV.encode('utf-8')
    plain = input("Nhập bản tin: ")
    return plain.encode('utf-8')


def main() -> None:
    plain = get_message()
    key, iv, cipher_bytes = encrypt_des_cbc(plain)
    #Start Ca 2
    # fake_length = len(cipher_bytes) + 100 
    # header_sai = key + iv + struct.pack('!I', fake_length)
    # overall_sai = header_sai + cipher_bytes
    #End Ca 2
    overall = build_packet(key, iv, cipher_bytes)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        # Start Ca 3
        # truncated_data = overall[:22] 
        # s.sendall(truncated_data)
        # print("[!] Đã gửi dữ liệu bị cắt cụt (Truncated).")
        # End Ca 3
        s.sendall(overall)

    lines = [
        "[+] Đã gửi bản mã.",
        f"Key: {key.hex()}",
        f"IV: {iv.hex()}",
        f"Ciphertext: {cipher_bytes.hex()}",
    ]
    for line in lines:
        print(line)

    if LOG_FILE:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
