let slides = document.querySelector(".slides");
let slideImg = document.querySelectorAll(".slides div");
currentIdx = 0;
slideCount = slideImg.length;
prev = document.querySelector(".prev");
next = document.querySelector(".next");

slideWidth = 300;
slideMargin = 100;
slides.style.width = (slideWidth + slideMargin)*slideCount + "px";

function moveSlide(num){
    // 왼쪽으로 400px씩 이동
    slides.style.left = -num * 400 + "px";
    currentIdx = num; }

prev.addEventListener('click', function(){
    // 첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해
// currentIdx !==0일때만 moveSlide 함수 불러옴
    if(currentIdx !== 0) moveSlide(currentIdx - 1); });

next.addEventListener('click', function(){
    // 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해
// currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴
    if(currentIdx !== slideCount - 1) moveSlide(currentIdx + 1); })
