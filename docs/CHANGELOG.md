# CHANGELOG

### 2026-04-14

- Khởi tạo pipeline triển khai cho đề tài phân tích đánh giá laptop Shopee theo phạm vi không Machine Learning.
- Tạo notebook `01_Crawl_Data.ipynb` để thu thập dữ liệu review từ Shopee theo cơ chế phân trang, chống trùng và bắt lỗi.
- Tạo notebook `02_EDA_Preprocessing.ipynb` để làm sạch dữ liệu tiếng Việt, tính thống kê mô tả và sinh biểu đồ.
- Tạo notebook `03_Report_Artifacts.ipynb` để tổng hợp bảng biểu phục vụ viết báo cáo Word.
- Tạo `README.md` mô tả cách chạy dự án và các tệp đầu ra chính.
- Tạo `docs/architecture.md` mô tả kiến trúc hệ thống, luồng dữ liệu và sơ đồ Mermaid.
- Xóa thư mục `TH5_C2` sau khi hoàn tất tái sử dụng mã nguồn và xác nhận notebook mới hoạt động độc lập.
- Tạo `.vscode/settings.json` để đặt interpreter mặc định về `.venv`, giúp môi trường chạy notebook nhất quán với dự án.
