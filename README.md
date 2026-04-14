# Phân Tích Ý Kiến Người Dùng Về Laptop Trên Shopee

Đây là dự án môn **Kỹ thuật lập trình trong phân tích dữ liệu** với phạm vi:

- Thu thập dữ liệu đánh giá sản phẩm laptop từ Shopee.
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

1. Mở `01_Crawl_Data.ipynb`, điền danh sách URL sản phẩm Shopee laptop vào biến `product_urls`, sau đó chạy toàn bộ notebook.
2. Mở `02_EDA_Preprocessing.ipynb` để làm sạch dữ liệu và tạo biểu đồ, bảng thống kê.
3. Mở `03_Report_Artifacts.ipynb` để gom các bảng CSV dùng trực tiếp cho báo cáo Word.

## Đầu ra chính

- `data/shopee_laptop_raw.csv`: dữ liệu thô sau crawl.
- `data/cleaned_reviews.csv`: dữ liệu đã làm sạch.
- `outputs/eda_summary.csv`: thống kê mô tả tổng quan.
- `outputs/chart_rating_distribution.png`: biểu đồ phân bố số sao.
- `outputs/chart_monthly_trend.png`: biểu đồ xu hướng review theo tháng (nếu có dữ liệu thời gian).
- `outputs/report/*.csv`: bộ bảng dùng cho phần báo cáo.

## Lưu ý khi crawl Shopee

- API có thể giới hạn truy cập tùy thời điểm hoặc theo mạng.
- Nên crawl số lượng vừa phải mỗi lần, có độ trễ giữa các request.
- Nếu gặp lỗi liên tiếp, thử đổi mạng hoặc giảm số sản phẩm trong một lượt chạy.
