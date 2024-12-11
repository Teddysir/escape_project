document.addEventListener("mousemove", (event) => {
    const lightEffect = document.getElementById("light-effect");
    const button = document.querySelector(".main-button");

    lightEffect.style.left = `${event.pageX}px`;
    lightEffect.style.top = `${event.pageY}px`;

    const rect = button.getBoundingClientRect();
    const x = event.clientX;
    const y = event.clientY;

    if (x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom) {
        button.style.opacity = 1; // 버튼 나타나기
    } else {
        button.style.opacity = 0; // 버튼 숨기기
    }
});
