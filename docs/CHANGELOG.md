# CHANGELOG

### 2026-04-23

- Cập nhật `01_Crawl_Data.ipynb` để gọi API comment riêng của FPTShop (`bff-before-order/comment/list`) thay vì chỉ đọc khối comment đầu tiên trong HTML.
- Bổ sung phân trang comment bằng `skipCount` và `maxResultCount`, giúp thu thập thêm phản hồi ở các trang 1, 2, 3, ... khi sản phẩm có nhiều bình luận.
- Bổ sung trích xuất phản hồi của quản trị viên vào các cột `reply_content`, `reply_created_at`, `reply_user_id`, `reply_is_admin` và `reply_like_count` khi có dữ liệu trả lời.
- Đồng bộ mô tả trong `README.md` và `docs/architecture.md` để phản ánh luồng crawl comment theo API có phân trang.

- Bắt đầu triển khai chuyển nguồn thu thập dữ liệu từ Shopee sang FPTShop theo hướng thay thế hoàn toàn.
- Cập nhật `01_Crawl_Data.ipynb` để crawl HTTP thuần từ FPTShop: thu URL sản phẩm từ trang tìm kiếm, đọc dữ liệu đánh giá hiển thị trong HTML trang chi tiết, chuẩn hóa schema và đổi `source` thành `FPTShop`.
- Cập nhật `01_Crawl_Data.ipynb` để bỏ giới hạn max thủ công: `max_products=None` và `max_reviews=None` trong luồng chạy chính.
- Bổ sung cơ chế dừng tự nhiên khi thu URL sản phẩm: dừng khi nhiều trang liên tiếp không có link mới, thay vì dừng theo ngưỡng số lượng cố định.
- Mở rộng schema dữ liệu thô trong `01_Crawl_Data.ipynb`: bổ sung `product_name`, `brand`, `price`, `final_price`, `rating_count_total`, `review_title`, `verified_purchase`, `image_product`, `image_review` (nếu có).
- Bổ sung parser metadata sản phẩm từ JSON nhúng trong HTML trang FPTShop để hỗ trợ phân tích theo hãng, giá và mức độ đại diện dữ liệu.
- Đổi đầu ra dữ liệu thô từ `data/shopee_laptop_raw.csv` sang `data/fptshop_laptop_raw.csv`.
- Cập nhật `02_EDA_Preprocessing.ipynb` để đọc dữ liệu thô mới và thêm kiểm tra các cột bắt buộc trước khi tiền xử lý.
- Cập nhật `03_Report_Artifacts.ipynb` để đồng bộ mô tả data dictionary với nguồn dữ liệu FPTShop và chỉnh lại thông báo tiếng Việt có dấu.
- Đồng bộ `README.md` và `docs/architecture.md` theo kiến trúc mới dựa trên FPTShop.

### 2026-04-14

- Khởi tạo pipeline triển khai cho đề tài phân tích đánh giá laptop Shopee theo phạm vi không Machine Learning.
- Tạo notebook `01_Crawl_Data.ipynb` để thu thập dữ liệu review từ Shopee theo cơ chế phân trang, chống trùng và bắt lỗi.
- Tạo notebook `02_EDA_Preprocessing.ipynb` để làm sạch dữ liệu tiếng Việt, tính thống kê mô tả và sinh biểu đồ.
- Tạo notebook `03_Report_Artifacts.ipynb` để tổng hợp bảng biểu phục vụ viết báo cáo Word.
- Tạo `README.md` mô tả cách chạy dự án và các tệp đầu ra chính.
- Tạo `docs/architecture.md` mô tả kiến trúc hệ thống, luồng dữ liệu và sơ đồ Mermaid.
- Xóa thư mục `TH5_C2` sau khi hoàn tất tái sử dụng mã nguồn và xác nhận notebook mới hoạt động độc lập.
- Tạo `.vscode/settings.json` để đặt interpreter mặc định về `.venv`, giúp môi trường chạy notebook nhất quán với dự án.
