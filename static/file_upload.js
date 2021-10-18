const button = document.getElementById('button');
button.addEventListener('click', () => {
  const input = document.getElementById('files');
  putFile(input.files[0]);
  alert('사진이 업로드 되었습니다!')
})