document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("searchInput");
    if (!input) return;

    const form = input.closest('form');
    let timeout = null;

    input.addEventListener("input", function () {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            let val = this.value.trim();
            if (val.length > 0) {
                sessionStorage.setItem('focus_search', 'true');
                form.submit();
            } else {
                sessionStorage.setItem('focus_search', 'true');
                window.location.href = "/";
            }
        }, 500);
    });

    // Agar /search/ sahifasida bo'lsak, input o'zida kursor turishi uchun:
    // Sahifa yuklanganda fokusni tiklash
    if (window.location.pathname.includes('/search/') || sessionStorage.getItem('focus_search') === 'true') {
        input.focus();
        let val = input.value;
        input.value = '';
        input.value = val; // Kursorni oxiriga suramiz
        sessionStorage.removeItem('focus_search');
    }
});
