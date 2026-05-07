# Peer Review Response

## Thông tin nhóm
- Thành viên 1: Đồng Đỗ Bảo - 1871020073
- Thành viên 2: Đào Văn Minh - 1871020390

## Thành viên 1 góp ý cho thành viên 2
- Receiver ban đầu chưa kiểm tra đầy đủ trường hợp nhận thiếu dữ liệu.
- Cần bổ sung xử lý exception và log lỗi rõ ràng hơn.
- Nên kiểm tra padding khi giải mã để tránh lỗi dữ liệu.

## Thành viên 2 góp ý cho thành viên 1
- Sender cần bổ sung thêm các ca kiểm thử lỗi.
- README còn thiếu phần phân công công việc và ethics.
- Cần ghi log rõ hơn để làm minh chứng cho bài lab.

## Nhóm đã sửa gì sau góp ý
- Bổ sung kiểm tra lỗi khi nhận thiếu ciphertext.
- Thêm xử lý lỗi decode và padding trong receiver.
- Hoàn thiện README.md với phân công công việc và Ethics & Safe use.
- Bổ sung threat-model-1page.md và report-1page.md đầy đủ.
- Thêm log minh chứng và các test case trong thư mục tests/.