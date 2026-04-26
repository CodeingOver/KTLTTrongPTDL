# CHANGELOG

### 2026-04-26

- Cập nhật `01_Crawl_Data.ipynb` để giảm bắt nhầm metadata khi fallback regex: giới hạn vùng quét quanh `productAdvanceInfo` trước khi đọc `brand`/`price`/`final_price`.
- Bổ sung hàm suy luận hãng từ `product_name` và `product_url`, dùng làm lớp kiểm tra chéo khi metadata trả về hãng không khớp nhận diện sản phẩm.
- Thêm cơ chế tự sửa `brand` khi phát hiện lệch giữa brand trích xuất và brand suy luận (ví dụ tránh dồn sai về một hãng duy nhất ở các dòng cuối dữ liệu thô).
- Cập nhật luồng `fetch_product_reviews` để truyền `product_url` vào `extract_product_metadata`, phục vụ kiểm tra nhất quán metadata theo đúng sản phẩm đang crawl.

### 2026-04-24

- Cập nhật `01_Crawl_Data.ipynb` để chỉ thu URL sản phẩm có `sku`, giữ nguyên query trên link sản phẩm và lưu thêm `product_url` vào từng dòng dữ liệu thô.
- Sửa lỗi lấy nhầm nhánh/đường dẫn sản phẩm bằng cách loại bỏ các link breadcrumb/danh mục không phải trang sản phẩm trong luồng thu thập URL.
- Chuyển bộ thu URL sang nhận diện thẻ sản phẩm thực tế trên trang tìm kiếm qua cặp `title + href`, vì FPTShop không còn gắn `?sku=` trong href của product card.
- Ưu tiên khối `detail-product-script` khi trích metadata sản phẩm để tránh lấy nhầm `brand`/`product_name` từ các khối JSON-LD hoặc nội dung liên quan khác trên trang.
- Cập nhật `02_EDA_Preprocessing.ipynb` để giữ lại review thiếu `rating_star` trong `cleaned_reviews.csv`, chỉ loại các giá trị rating hỏng hoặc ngoài khoảng hợp lệ.
- Khôi phục cell nạp dữ liệu đầu vào của notebook EDA và xác nhận lại pipeline làm sạch chạy ổn trên dữ liệu hiện có.
- Bổ sung biểu đồ mới trong `02_EDA_Preprocessing.ipynb`: boxplot độ dài review theo số sao và bar chart Top 15 từ khóa xuất hiện nhiều nhất.
- Bổ sung biểu đồ mới trong `03_Report_Artifacts.ipynb`: Top 12 sản phẩm theo số lượng review và biểu đồ tròn cơ cấu nhóm cảm xúc theo số sao.
- Tinh chỉnh biểu đồ tròn sentiment trong `03_Report_Artifacts.ipynb`: đổi nhãn sang tiếng Việt có dấu, cải thiện bảng màu và bổ sung hiển thị đồng thời tỷ lệ phần trăm + số lượng để dễ đọc hơn.
- Tối ưu chống chồng nhãn cho biểu đồ tròn sentiment: ẩn nhãn trực tiếp ở lát cắt nhỏ, chuyển chi tiết sang legend kèm tỷ lệ/số lượng và tách nhẹ các lát nhỏ bằng `explode`.

- Dọn `01_Crawl_Data.ipynb` bằng cách xóa cell định nghĩa hàm trùng lặp để tránh ghi đè logic crawl comment theo phân trang khi chạy `Run All`.
- Xác nhận notebook chỉ còn một cell định nghĩa hàm crawl chính và không còn thông báo cũ về việc "chưa phân trang sâu".
- Cập nhật `crawl_product_reviews` trong `01_Crawl_Data.ipynb`: tăng độ ổn định phân trang bằng cách tính `skipCount` theo số item thực nhận, thêm retry khi trang kế tiếp trả rỗng bất thường.
- Điều chỉnh thông báo cuối để phân biệt trường hợp `totalCount` bao gồm cả phản hồi con (`children`) với trường hợp API ẩn dữ liệu theo trạng thái hiển thị.
- Xác minh bằng Playwright rằng giao diện dùng phân trang số (`1`, `2`) và request trang 2 gửi `skipCount=6` với `content.id` riêng của hệ comment.
- Sửa `extract_product_code` để ưu tiên trích `content.id` 12 chữ số mà frontend dùng cho comment API, thay vì mã hiển thị sản phẩm; nhờ đó crawl sản phẩm MSI Modern 15 đã lấy đủ `10/10` comment (trang 1: 6, trang 2: 4).

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
