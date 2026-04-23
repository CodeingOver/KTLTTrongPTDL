# Phân Tích Ý Kiến Người Dùng Về Laptop Trên FPTShop

Đây là dự án môn **Kỹ thuật lập trình trong phân tích dữ liệu** với phạm vi:

- Thu thập dữ liệu đánh giá sản phẩm laptop từ FPTShop.
- Làm sạch dữ liệu văn bản tiếng Việt.
- Phân tích dữ liệu mô tả và trực quan hóa.
- Tổng hợp bảng biểu để chèn vào báo cáo.

Dự án **không sử dụng Machine Learning** theo yêu cầu phạm vi hiện tại.

## Cấu trúc thư mục

```text
.
├─ 01_Crawl_Data.ipynb
├─ 02_EDA_Preprocessing.ipynb
├─ 03_Report_Artifacts.ipynb
├─ data/
├─ outputs/
└─ docs/
```

## Quy trình chạy

1. Mở `01_Crawl_Data.ipynb`, chạy toàn bộ notebook để tự động thu danh sách URL sản phẩm laptop từ FPTShop và crawl dữ liệu đánh giá qua API comment có phân trang (1, 2, 3, ...).
2. Mở `02_EDA_Preprocessing.ipynb` để làm sạch dữ liệu và tạo biểu đồ, bảng thống kê.
3. Mở `03_Report_Artifacts.ipynb` để gom các bảng CSV dùng trực tiếp cho báo cáo Word.

## Đầu ra chính

- `data/fptshop_laptop_raw.csv`: dữ liệu thô sau crawl (bao gồm thêm metadata như `product_name`, `brand`, `price`, `final_price`, `rating_count_total`, `review_title`, `verified_purchase`, `image_product`, `image_review` nếu có).
- `data/cleaned_reviews.csv`: dữ liệu đã làm sạch.
- `outputs/eda_summary.csv`: thống kê mô tả tổng quan.
- `outputs/chart_rating_distribution.png`: biểu đồ phân bố số sao.
- `outputs/chart_monthly_trend.png`: biểu đồ xu hướng review theo tháng (nếu có dữ liệu thời gian).
- `outputs/report/*.csv`: bộ bảng dùng cho phần báo cáo.

## Lưu ý khi crawl FPTShop

- Crawler hiện chạy theo hướng HTTP thuần (`requests`) và lấy comment từ API `bff-before-order/comment/list` của FPTShop, sau đó lặp `skipCount`/`maxResultCount` để đi qua các trang comment.
- FPTShop có thể thay đổi cấu trúc dữ liệu theo thời điểm, nên cần theo dõi log số lượng review thu được ở mỗi sản phẩm.
- Nếu gặp lỗi liên tiếp hoặc dữ liệu thu được thấp, tăng độ trễ giữa các request và giảm số lượng sản phẩm mỗi lượt chạy.
- Một số phản hồi của quản trị viên có thể đi kèm trong `reply_content` nếu sản phẩm có comment được trả lời trực tiếp.
