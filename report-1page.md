# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Đồng Đỗ Bảo - 1871020073
- Thành viên 2: Đào Văn Minh - 1871020390

## Mục tiêu
Mục tiêu của bài lab là xây dựng hệ thống gửi và nhận dữ liệu mã hóa DES qua TCP socket bằng Python. Hệ thống gồm Sender và Receiver hoạt động theo mô hình client-server. Sender thực hiện mã hóa DES-CBC với IV và PKCS#7 padding trước khi gửi dữ liệu qua socket. Receiver nhận packet, giải mã và hiển thị lại plaintext. Ngoài ra bài lab còn giúp hiểu về protocol truyền dữ liệu, xử lý lỗi mạng, và các vấn đề bảo mật liên quan đến DES và truyền khóa.

## Phân công thực hiện
- Thành viên 1 phụ trách chính phần Sender, mã hóa DES-CBC và xử lý packet gửi.
- Thành viên 2 phụ trách chính phần Receiver, giải mã và xử lý nhận dữ liệu.
- Cả hai cùng thực hiện kiểm thử, ghi log, viết threat model, README và báo cáo.

## Cách làm
Hệ thống được xây dựng bằng Python sử dụng TCP socket. Sender tạo DES key 8 byte và IV 8 byte, sau đó mã hóa plaintext bằng DES-CBC kết hợp PKCS#7 padding. Dữ liệu được đóng gói theo thứ tự key + IV + length header + ciphertext rồi gửi qua socket.

Receiver mở cổng lắng nghe kết nối TCP, nhận packet theo đúng thứ tự, tách key, IV và ciphertext để giải mã. Hệ thống có bổ sung kiểm tra lỗi như nhận thiếu ciphertext, lỗi padding và lỗi kết nối.

Các ca kiểm thử gồm:
- Happy path.
- Truncated ciphertext.
- Invalid padding.
- Wrong length header.
- Connection closed unexpectedly.

## Kết quả
Hệ thống Sender và Receiver chạy thành công trên localhost. Receiver nhận và giải mã đúng plaintext trong trường hợp hợp lệ. Các kiểm thử lỗi cho thấy hệ thống có thể phát hiện lỗi nhận thiếu dữ liệu, lỗi padding và lỗi kết nối.

Minh chứng được lưu trong thư mục `logs/`, bao gồm:
- log happy path;
- log truncated ciphertext;
- log padding error.

## Kết luận
Qua bài lab, nhóm hiểu rõ hơn về cơ chế hoạt động của TCP socket, DES-CBC, IV và PKCS#7 padding. Bài lab cũng cho thấy việc truyền khóa DES dạng plaintext là không an toàn và cần có cơ chế trao đổi khóa tốt hơn trong hệ thống thực tế.

Ngoài ra, nhóm rút ra được tầm quan trọng của kiểm thử lỗi, xử lý exception và threat model trong quá trình phát triển hệ thống mạng và bảo mật thông tin.
