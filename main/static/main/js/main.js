// CSRF 토큰 가져오기 함수
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie("csrftoken"); // CSRF 토큰 가져오기

// 모든 문 요소 가져오기
document.querySelectorAll(".door").forEach((door) => {
    const img = door.querySelector(".door-img"); // 문 이미지
    const originalSrc = img.src; // 기본 문 이미지 경로
    const hoverSrc = originalSrc.replace("door1.png", "door2.png"); // 열리는 문 이미지 경로

    // 문 위에 커서가 올라갈 때
    door.addEventListener("mouseover", () => {
        console.log("문 위로 커서 이동"); // 디버깅용 로그
        img.src = hoverSrc; // 열리는 문 이미지로 변경
    });

    // 문에서 커서가 나갈 때
    door.addEventListener("mouseout", () => {
        console.log("문 밖으로 커서 이동"); // 디버깅용 로그
        img.src = originalSrc; // 기본 문 이미지로 복구
    });

    // 문 클릭 이벤트
    door.addEventListener("click", () => {
        const url = door.getAttribute("data-url"); // 문에 설정된 URL 가져오기
        console.log(`문 클릭됨, 이동할 URL: ${url}`); // 디버깅용 로그
        window.location.href = url; // 해당 URL로 이동
    });
});
