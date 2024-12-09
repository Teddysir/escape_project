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

// 첫 번째 문 클릭 이벤트
document.getElementById("door1").addEventListener("click", () => {
    document.getElementById("input-container1").style.display = "block"; // 첫 번째 문제 입력란 표시
    document.getElementById("input-container2").style.display = "none"; // 두 번째 문제 입력란 숨기기
    document.getElementById("input-container3").style.display = "none"; // 세 번째 문제 입력란 표시

});

// 두 번째 문 클릭 이벤트
document.getElementById("door2").addEventListener("click", () => {
    document.getElementById("input-container2").style.display = "block"; // 두 번째 문제 입력란 표시
    document.getElementById("input-container1").style.display = "none"; // 첫 번째 문제 입력란 숨기기
    document.getElementById("input-container3").style.display = "none"; // 세 번째 문제 입력란 표시
});

document.getElementById("door3").addEventListener("click", () => {
    document.getElementById("input-container3").style.display = "block"; // 세 번째 문제 입력란 표시
    document.getElementById("input-container1").style.display = "none"; // 첫 번째 문제 입력란 숨기기
    document.getElementById("input-container2").style.display = "none"; // 두 번째 문제 입력란 숨기기
});

// 첫 번째 제출 버튼 클릭 이벤트
document.getElementById("submit-answer1").addEventListener("click", () => {
    const userAnswer1 = document.getElementById("answer1").value.trim(); // 첫 번째 입력값
    const feedback1 = document.getElementById("feedback1");
    if (userAnswer1 === "32") {
        window.location.href = document.getElementById("door1").getAttribute("data-url"); // 정답일 경우 door1.html로 이동
    } else {
        feedback1.textContent = "오답입니다."; // 오답 메시지 표시
        feedback1.style.display = "block";
    }
});

// 두 번째 제출 버튼 클릭 이벤트
document.getElementById("submit-answer2").addEventListener("click", () => {
    const userAnswer2 = document.getElementById("answer2").value.trim(); // 두 번째 입력값
    const feedback2 = document.getElementById("feedback2");
    if (userAnswer2 === "solved김성훈") {
        window.location.href = document.getElementById("door2").getAttribute("data-url"); // 정답일 경우 door2.html로 이동
    } else {
        feedback2.textContent = "오답입니다. 1번 문을 먼저 해결해주세요. "; // 오답 메시지 표시
        feedback2.style.display = "block";
    }
});

document.getElementById("submit-answer3").addEventListener("click", () => {
    const userAnswer3 = document.getElementById("answer3").value.trim(); // 세 번째 입력값
    const feedback3 = document.getElementById("feedback3");
    if (userAnswer3 === "cleardjango") {
        window.location.href = document.getElementById("door3").getAttribute("data-url"); // 정답일 경우 door3.html로 이동
    } else {
        feedback3.textContent = "오답입니다. 2번 문을 먼저 해결해주세요. "; // 오답 메시지 표시
        feedback3.style.display = "block";
    }
});

// 엔터 키로 제출 버튼 클릭 처리 (첫 번째 문제)
document.getElementById("answer1").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        document.getElementById("submit-answer1").click(); // 제출 버튼 클릭 이벤트 실행
    }
});

// 엔터 키로 제출 버튼 클릭 처리 (두 번째 문제)
document.getElementById("answer2").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        document.getElementById("submit-answer2").click(); // 제출 버튼 클릭 이벤트 실행
    }
});

document.getElementById("answer3").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        document.getElementById("submit-answer3").click(); // 제출 버튼 클릭 이벤트 실행
    }
});
