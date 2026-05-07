# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Đồng Đỗ Bảo_1871020073 
- Thành viên 2: Đào Văn Minh_1871020390

## Assets
1. Assets

Các tài sản quan trọng của hệ thống bao gồm:

Plaintext (bản rõ) do người dùng nhập.
DES key được dùng để mã hóa và giải mã dữ liệu.
IV (Initialization Vector) sử dụng trong chế độ DES-CBC.
Ciphertext được truyền qua socket.
Log hệ thống ghi lại thông tin kết nối và kết quả xử lý.
Địa chỉ IP và cổng dịch vụ của receiver.
Mã nguồn sender và receiver.
2. Attacker model

Kẻ tấn công có thể:

Nghe lén dữ liệu trong cùng mạng LAN.
Chặn và sửa đổi dữ liệu trên đường truyền.
Gửi gói tin giả mạo hoặc dữ liệu lỗi tới receiver.
Làm gián đoạn hoặc đóng kết nối bất ngờ.
Quan sát log hoặc dữ liệu debug nếu máy bị truy cập trái phép.
3. Threats
Threat 1: Lộ khóa DES

Hệ thống gửi DES key cùng kênh truyền dưới dạng plaintext. Nếu attacker nghe lén mạng, họ có thể lấy được khóa và giải mã toàn bộ dữ liệu.

Threat 2: Sửa đổi ciphertext

Attacker có thể thay đổi ciphertext trong quá trình truyền, làm dữ liệu sau giải mã bị sai hoặc gây lỗi padding.

Threat 3: Giả mạo độ dài dữ liệu

Attacker có thể thay đổi length header khiến receiver đọc sai số byte cần nhận, dẫn tới lỗi xử lý hoặc treo chương trình.

Threat 4: Đóng kết nối bất ngờ

Kết nối có thể bị đóng giữa chừng khiến receiver nhận thiếu dữ liệu và xử lý không chính xác.

4. Mitigations

Để giảm thiểu rủi ro, hệ thống có thể áp dụng:

Không truyền khóa DES dưới dạng plaintext.
Sử dụng cơ chế trao đổi khóa an toàn hơn như RSA hoặc Diffie-Hellman.
Kiểm tra tính hợp lệ của header và độ dài dữ liệu nhận được.
Thêm xử lý exception và timeout cho socket.
Kiểm tra padding khi giải mã dữ liệu.
Hạn chế log dữ liệu nhạy cảm trong môi trường thực tế.
Có thể bổ sung cơ chế kiểm tra toàn vẹn như HMAC.
5. Residual risks

Một số rủi ro vẫn còn tồn tại:

Máy người dùng có thể bị compromise hoặc cài malware.
Log có thể làm lộ dữ liệu nhạy cảm nếu bị truy cập trái phép.
Trong môi trường mạng nội bộ, attacker vẫn có khả năng sniffing dữ liệu.
DES là thuật toán cũ và không còn đủ mạnh cho môi trường thực tế hiện nay.


