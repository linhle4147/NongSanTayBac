document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chanhThuForm');
    const status = document.getElementById('statusMsg');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const btn = form.querySelector('.btn-submit');

        // Hiệu ứng nút
        btn.innerHTML = "ĐANG GỬI...";
        btn.style.opacity = "0.7";
        btn.disabled = true;

        // Giả lập gửi dữ liệu
        setTimeout(() => {
            status.innerHTML = `<p style="color: green; margin-top: 15px;">Chào ${name}, tin nhắn của bạn đã được gửi tới Chánh Thu!</p>`;
            form.reset();
            btn.innerHTML = "GỬI TIN NHẮN";
            btn.style.opacity = "1";
            btn.disabled = false;
        }, 2000);
    });
});