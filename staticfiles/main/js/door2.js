document.addEventListener("DOMContentLoaded", () => {
    const door = document.querySelector(".door");
    const originalSrc = door.src; // 기본 문 이미지 경로
    const hoverSrc = originalSrc.replace("door1.png", "door2.png"); // 열리는 문 이미지 경로

    // 문에 커서 올리면 이미지 변경
    door.addEventListener("mouseover", () => {
        door.src = hoverSrc; // 열리는 문 이미지로 변경
    });

    // 문에서 커서 나가면 이미지 복구
    door.addEventListener("mouseout", () => {
        door.src = originalSrc; // 기본 문 이미지로 복구
    });

    // 문 클릭 시 메인 페이지로 이동
    door.addEventListener("click", () => {
        const mainUrl = door.getAttribute("data-main-url"); // HTML 속성에서 URL 가져오기
        window.location.href = mainUrl; // 메인 페이지로 이동
    });
});
