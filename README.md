
I. Giới thiệu
Trong thế giới hiện đại, việc quản lý giao thông ngày càng trở nên quan trọng hơn do sự gia tăng mật độ phương tiện. Một phần quan trọng trong việc quản lý giao thông là khả năng xử lý và phân tích ảnh phương tiện giao thông để thu thập thông tin và đưa ra các quyết định hiệu quả. Đề tài này tập trung vào việc phát triển một ứng dụng phần mềm sử dụng công nghệ xử lý ảnh và nhận diện đối tượng để nâng cấp chất lượng ảnh và phân tích các chỉ số ảnh của phương tiện giao thông. Ứng dụng này được xây dựng bằng Python, kết hợp với các thư viện mạnh mẽ như Tkinter cho giao diện người dùng, OpenCV cho xử lý ảnh, NumPy và SciPy cho các phép toán số học, scikit-image cho phân tích ảnh, và PIL (Python Imaging Library) cho xử lý ảnh.
II. Mục tiêu
Nâng cấp chất lượng ảnh:
Mục tiêu: Cải thiện chất lượng của ảnh phương tiện giao thông bằng cách làm rõ các chi tiết quan trọng. Chất lượng ảnh ảnh hưởng trực tiếp đến khả năng nhận diện và phân tích các phương tiện trong ảnh.
Phương pháp: Sử dụng các kỹ thuật xử lý ảnh như làm sắc nét (sharpening) và cân bằng histogram để làm nổi bật các chi tiết và cải thiện độ sáng của ảnh.
Phân tích chỉ số ảnh:
Mục tiêu: Đánh giá chất lượng của ảnh dựa trên các chỉ số quan trọng như độ sáng, độ tương phản, độ sắc nét và thông tin ảnh. Những chỉ số này giúp đánh giá và điều chỉnh chất lượng ảnh để đạt được kết quả tối ưu.
Phương pháp: Tính toán các chỉ số ảnh bằng cách sử dụng các phép toán số học và phân tích histogram của ảnh để đo lường độ sáng, độ tương phản, và độ sắc nét, cùng với thông tin ảnh.
Nhận diện và phân loại phương tiện giao thông:
Mục tiêu: Phát hiện và phân loại các loại phương tiện giao thông trong ảnh để cung cấp thông tin chi tiết về tình hình giao thông. Việc nhận diện chính xác các phương tiện giúp cải thiện khả năng quản lý và điều phối giao thông.
Phương pháp: Sử dụng mô hình YOLOv3 (You Only Look Once version 3), một mô hình nhận diện đối tượng tiên tiến, để phát hiện và phân loại các phương tiện như ô tô, xe máy, xe bus, và xe tải trong ảnh.
III. Phương pháp
Giao diện người dùng:
                        
Thiết kế giao diện: Sử dụng thư viện Tkinter để tạo một giao diện đồ họa người dùng (GUI) cho phép người dùng tương tác với ứng dụng một cách dễ dàng. Giao diện bao gồm các khung chức năng được thiết kế để đơn giản hóa các thao tác xử lý ảnh và phân tích dữ liệu.
Khung thao tác với tệp: Cung cấp các nút để thực hiện các thao tác liên quan đến tệp như tải tệp YOLO, tải ảnh từ hệ thống và lưu các kết quả xử lý.
Khung xử lý ảnh: Cung cấp các nút để thực hiện các thao tác xử lý ảnh như xử lý ảnh, phát hiện phương tiện, phân tích ảnh và làm sắc nét ảnh. Các chức năng này giúp người dùng dễ dàng áp dụng các kỹ thuật xử lý ảnh.
Khung trạng thái: Hiển thị thông tin trạng thái và kết quả của các thao tác xử lý ảnh, giúp người dùng theo dõi tiến trình và kết quả một cách rõ ràng và hiệu quả.
Khung hiển thị ảnh: Hiển thị ảnh gốc và ảnh đã xử lý để người dùng có thể so sánh và đánh giá chất lượng ảnh. Việc hiển thị ảnh giúp người dùng kiểm tra các thay đổi và cải thiện chất lượng ảnh.
Xử lý ảnh:
Tải tệp YOLO:
Kiểm tra sự tồn tại của tệp: Trước khi tải tệp, ứng dụng kiểm tra xem các tệp cần thiết cho mô hình YOLOv3 đã tồn tại trên hệ thống chưa. Điều này giúp tiết kiệm thời gian và tài nguyên.
Tải xuống tệp: Nếu các tệp không tồn tại, ứng dụng tự động tải chúng từ các nguồn trực tuyến. Các tệp này bao gồm mô hình YOLOv3 và cấu hình của nó, cũng như danh sách các lớp (coco.names).
Tải ảnh:
Chọn ảnh: Cho phép người dùng chọn và tải ảnh từ hệ thống bằng hộp thoại chọn tệp. Điều này giúp người dùng linh hoạt trong việc chọn ảnh từ nhiều nguồn khác nhau.
Xử lý ảnh:
Chuyển đổi ảnh sang xám: Ảnh được chuyển từ không gian màu RGB sang không gian màu xám để chuẩn bị cho các bước xử lý tiếp theo. Việc chuyển đổi này giúp đơn giản hóa các phép toán xử lý ảnh.
Cân bằng histogram: Áp dụng cân bằng histogram để cải thiện độ tương phản của ảnh, làm nổi bật các chi tiết và làm cho ảnh dễ nhìn hơn.
Lưu ảnh đã xử lý: Lưu ảnh đã qua xử lý vào hệ thống để sử dụng cho các bước tiếp theo, giúp lưu trữ các kết quả và duy trì quá trình làm việc.
Nhận diện phương tiện:
Tải mô hình YOLOv3: Tải mô hình YOLOv3 và cấu hình của nó từ hệ thống để sử dụng trong việc nhận diện đối tượng.
Tiền xử lý ảnh: Chuyển ảnh thành blob, một định dạng phù hợp với đầu vào của mô hình YOLOv3. Blob là một tensor bốn chiều chứa các giá trị pixel của ảnh.
Nhận diện đối tượng: Sử dụng mô hình YOLOv3 để phát hiện và phân loại các phương tiện giao thông trong ảnh. Mô hình YOLOv3 phân tích ảnh và xác định các đối tượng, sau đó vẽ các hình chữ nhật và gán nhãn cho các phương tiện.
Lưu kết quả: Lưu ảnh với các đối tượng đã phát hiện và hiển thị nó trên giao diện người dùng, cung cấp thông tin chi tiết về các phương tiện trong ảnh.
Nâng cấp ảnh:
                            
Kỹ thuật làm sắc nét: Áp dụng bộ lọc làm sắc nét để cải thiện độ rõ nét của ảnh. Bộ lọc này làm tăng độ tương phản của các cạnh trong ảnh, giúp làm nổi bật các chi tiết và thông tin quan trọng.
Lưu ảnh nâng cấp: Lưu ảnh đã nâng cấp vào hệ thống và hiển thị nó trên giao diện người dùng để người dùng có thể so sánh với ảnh gốc và đánh giá hiệu quả của các thao tác nâng cấp.
Phân tích chỉ số ảnh:
Độ sáng: Tính toán giá trị trung bình của cường độ sáng trong ảnh để đánh giá mức độ sáng tổng thể. Giá trị này giúp xác định nếu ảnh quá tối hoặc quá sáng, từ đó điều chỉnh để cải thiện khả năng nhìn rõ.
Độ tương phản: Đo lường sự biến thiên của cường độ sáng trong ảnh để xác định mức độ tương phản. Độ tương phản cao làm cho các chi tiết nổi bật hơn và dễ nhìn hơn.
Thông tin ảnh: Tính toán entropy của histogram ảnh để đánh giá mức độ thông tin và sự phong phú của ảnh. Entropy cao cho thấy ảnh chứa nhiều thông tin và chi tiết, giúp cải thiện khả năng phân tích.
Độ sắc nét: Sử dụng bộ lọc Sobel để xác định độ sắc nét của ảnh. Đo lường độ nhấn mạnh của các cạnh giúp đánh giá mức độ rõ ràng của các chi tiết trong ảnh. Độ sắc nét cao giúp cải thiện khả năng phân tích và nhận diện.
IV. Kết quả
Nâng cấp ảnh:
Cải thiện chất lượng ảnh: Sau khi áp dụng các kỹ thuật nâng cấp, ảnh phương tiện giao thông trở nên rõ ràng hơn với các chi tiết sắc nét và dễ nhìn. Các phương pháp như làm sắc nét và điều chỉnh độ sáng đã giúp làm nổi bật các chi tiết quan trọng, giúp người dùng dễ dàng nhận diện và phân tích các phương tiện.
Tăng cường khả năng nhận diện: Với chất lượng ảnh được cải thiện, khả năng nhận diện và phân tích các phương tiện trở nên chính xác hơn. Điều này giúp nâng cao hiệu quả của các hệ thống quản lý và điều phối giao thông.
Phân tích chỉ số ảnh:
Độ sáng: Các giá trị độ sáng cung cấp cái nhìn về mức độ sáng của ảnh, cho phép điều chỉnh để đạt được sự cân bằng tốt nhất cho việc nhận diện và phân tích.
Độ tương phản: Đo lường sự khác biệt giữa các mức sáng cho biết độ rõ nét của ảnh. Độ tương phản cao làm cho các chi tiết nổi bật hơn và dễ nhìn hơn, cải thiện khả năng phân tích.
Thông tin ảnh: Entropy giúp đánh giá mức độ thông tin trong ảnh, cho biết nếu ảnh chứa nhiều chi tiết và thông tin hữu ích. Entropy cao cho thấy ảnh có chất lượng tốt hơn về mặt thông tin.
Độ sắc nét: Đo lường mức độ sắc nét giúp xác định sự rõ ràng của các chi tiết trong ảnh. Độ sắc nét cao giúp làm nổi bật các chi tiết quan trọng, cải thiện khả năng nhận diện và phân tích.
Nhận diện phương tiện:
Kết quả phát hiện phương tiện: Mô hình YOLOv3 đã thực hiện việc phát hiện và phân loại các phương tiện trong ảnh với độ chính xác cao. Các loại phương tiện như ô tô, xe máy, xe bus và xe tải được phát hiện và gán nhãn chính xác.
Thông tin chi tiết: Kết quả nhận diện cung cấp thông tin chi tiết về tình hình giao thông, giúp nâng cao khả năng quản lý và điều phối giao thông. Các phương tiện được đánh dấu và gán nhãn giúp người dùng dễ dàng theo dõi và phân tích tình hình giao thông.
V. Kết luận
Ứng dụng phần mềm được phát triển đã chứng minh khả năng trong việc nâng cấp chất lượng ảnh và phân tích các chỉ số ảnh một cách hiệu quả. Các kỹ thuật xử lý ảnh như làm sắc nét và điều chỉnh độ sáng đã giúp cải thiện rõ rệt chất lượng ảnh, làm nổi bật các chi tiết quan trọng và nâng cao khả năng nhận diện. Phân tích các chỉ số ảnh cung cấp cái nhìn sâu sắc về chất lượng ảnh, giúp đánh giá và điều chỉnh để đạt được kết quả tối ưu. Mô hình YOLOv3 đã đạt được kết quả chính xác trong việc phát hiện và phân loại các phương tiện giao thông, cung cấp thông tin hữu ích cho việc quản lý và điều phối giao thông. Kết quả này có thể được áp dụng trong các hệ thống giao thông thông minh, hệ thống giám sát và các ứng dụng quản lý giao thông khác, góp phần nâng cao hiệu quả và an toàn giao thông.
Link source code git hub : https://github.com/hatrungtien/xu_ly_anh
